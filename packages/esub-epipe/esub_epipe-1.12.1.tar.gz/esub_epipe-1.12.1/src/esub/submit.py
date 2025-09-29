#! /usr/bin/env python

# Copyright (C) 2019 ETH Zurich,
# Institute for Particle Physics and Astrophysics
# Author: Dominik Zuercher, adapted by Silvan Fischbacher

# System imports
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse

# package imports
import os
import shlex
import subprocess
import sys
import time

from ekit import logger as logger_utils

from esub import utils

LOGGER = logger_utils.init_logger(__name__)

# parse all the submitter arguments
parser = argparse.ArgumentParser()
parser.add_argument("--job_name", type=str, required=True)
parser.add_argument("--source_file", type=str, required=True)
parser.add_argument("--main_memory", type=float, required=True)
parser.add_argument("--main_time", type=float, required=True)
parser.add_argument("--main_scratch", type=float, required=True)
parser.add_argument("--main_gpu", type=int, required=True)
parser.add_argument("--main_gpu_memory", type=float, required=True)
parser.add_argument("--function", type=str, required=True)
parser.add_argument("--executable", type=str, required=True)
parser.add_argument("--tasks", type=str, required=True)
parser.add_argument("--n_jobs", type=int, required=True)
parser.add_argument("--main_n_cores", type=int, required=True)
parser.add_argument("--log_dir", type=str, required=True)
parser.add_argument("--system", type=str, required=True)
parser.add_argument("--main_name", type=str, required=True)
parser.add_argument("--mode", type=str, required=True)
parser.add_argument("--main_mode", type=str, required=True)
parser.add_argument("--batchsize", type=int, required=True)
parser.add_argument("--max_njobs", type=int, required=True)
parser.add_argument("--discard_output", action="store_true", default=False)
parser.add_argument("--esub_verbosity", type=int, default=3)
parser.add_argument("--additional_bsub_args", type=str, default="")
parser.add_argument("--additional_slurm_args", type=str, default="")
parser.add_argument("--test", action="store_true", default=False)
parser.add_argument("--keep_submit_files", action="store_true", default=False)
parser.add_argument("--nodes", type=int, default=1)
parser.add_argument("--MPI_tasks_per_core", type=int, default=1)
parser.add_argument("--MPI_tasks_per_node", type=int, default=1)
parser.add_argument("--OpenMP_threads_per_task", type=int, default=1)

args, function_args = parser.parse_known_args()
function = args.function
source_file = args.source_file
job_name = args.job_name
log_dir = args.log_dir
exe = args.executable
tasks = args.tasks
n_jobs = args.n_jobs
main_n_cores = args.main_n_cores
main_memory = args.main_memory
main_time = args.main_time
main_scratch = args.main_scratch
main_gpu = args.main_gpu
main_gpu_memory = args.main_gpu_memory
system = args.system
main_name = args.main_name
mode = args.mode
main_mode = args.main_mode

if mode == "mpi":
    try:
        from mpi4py import MPI

        is_master = MPI.COMM_WORLD.rank == 0
    except ImportError:
        if args.test:
            is_master = False
        else:
            raise ImportError(
                "You are attempting to run a MPI job. This requires a local "
                "MPI environement as well as the mpi4py package"
            )
else:
    is_master = True

logger_utils.set_logger_level(LOGGER, args.esub_verbosity)

# get path of log file and of file containing finished indices
path_log = utils.get_path_log(log_dir, job_name)
path_finished = utils.get_path_finished_indices(log_dir, job_name)

TIMEOUT_MESSAGE = (
    "Maximum number of pending jobs reached, will sleep for 30 minutes and retry"
)

# get rank of the processor
try:
    msg_limit_reached = "Pending job threshold reached."
    pipe_limit_reached = "stderr"
    if system == "bsub":
        rank = int(os.environ["LSB_JOBINDEX"])
    elif system == "slurm":
        rank = int(os.environ["SLURM_ARRAY_TASK_ID"])
    elif system == "daint":
        rank = 1
    rank -= 1
except KeyError:
    LOGGER.warning(
        "Unable to get current Job array index. Are you on a slurm or bsub "
        "system? Setting it to 0"
    )
    rank = 0

is_first = rank == 0

# Import the executable
executable = utils.import_executable(exe)

if is_master:
    if function == "main":
        LOGGER.info(f"Running the function {main_name} specified in executable")
    else:
        LOGGER.info("Running the function {} specified in executable".format(function))

if (function == "rerun_missing") | (function == "check_missing"):
    if is_master:
        LOGGER.info("Checking if all main jobs terminated correctly...")

    indices_all = utils.get_indices(tasks)
    if function == "rerun_missing":
        indices_missing = utils.check_indices(
            indices_all,
            path_finished,
            executable,
            function_args,
            verbosity=args.esub_verbosity,
        )
    elif function == "check_missing":
        indices_missing = utils.check_indices(
            indices_all,
            path_finished,
            executable,
            function_args,
            check_indices_file=False,
            verbosity=args.esub_verbosity,
        )

    if is_master:
        utils.write_to_log(
            path_log, "Found {} missing indices".format(len(indices_missing))
        )

        if len(indices_missing) == 0:
            LOGGER.info("Nothing to resubmit. All jobs ended.")
        else:
            if len(indices_missing) > 1:
                # submit jobs
                tasks = ",".join(map(str, indices_missing[:-1]))
                n_jobs = len(indices_missing) - 1
                LOGGER.info("Re-Submitting tasks {} as {} jobs".format(tasks, n_jobs))
                jobid = utils.submit_job(
                    tasks=tasks,
                    mode=main_mode,
                    exe=args.executable,
                    log_dir=log_dir,
                    function_args=function_args,
                    function="main_rerun",
                    source_file=source_file,
                    n_jobs=n_jobs,
                    job_name=job_name,
                    main_memory=main_memory,
                    main_time=main_time,
                    main_scratch=main_scratch,
                    main_n_cores=main_n_cores,
                    main_gpu=main_gpu,
                    main_gpu_memory=main_gpu_memory,
                    dependency="",
                    system=system,
                    main_name=main_name,
                    batchsize=args.batchsize,
                    discard_output=args.discard_output,
                    max_njobs=args.max_njobs,
                    verbosity=args.esub_verbosity,
                    add_bsub=args.additional_bsub_args,
                    add_args=args.additional_slurm_args,
                    keep_submit_files=args.keep_submit_files,
                    nodes=args.nodes,
                    MPI_tasks_per_core=args.MPI_tasks_per_core,
                    MPI_tasks_per_node=args.MPI_tasks_per_node,
                    OpenMP_threads_per_task=args.OpenMP_threads_per_task,
                    test=args.test,
                    main_mode=main_mode,
                )

                utils.write_to_log(
                    path_log,
                    "Job id rerun_missing extended: {}".format(jobid[0]),
                )
            else:
                jobid = None

            # Change to local scratch if set; this has to be done
            # after submission,
            # s.t. that the pwd at submission time is
            # the original directory where the submission starts
            utils.cd_local_scratch(args.esub_verbosity)

            # run last job locally to not waste any resources
            index = indices_missing[-1]
            if is_master:
                LOGGER.info(
                    "##################### Starting Task {}\
                    #####################".format(index)
                )
            try:
                for index in getattr(executable, main_name)([index], function_args):
                    if is_master:
                        utils.write_index(index, path_finished)
                if is_master:
                    LOGGER.info(
                        "##################### Finished Task {}\
                        #####################".format(index)
                    )
            except Exception as err:
                LOGGER.error("Error ocurred in rerun: {}".format(err))

            if is_master:
                if len(indices_missing) == 1:
                    utils.write_to_log(path_log, "First index is done")

            if is_master:
                # wait until all jobs are done
                if jobid is not None:
                    if system == "bsub":
                        while True:
                            while True:
                                output = dict(stdout=[], stderr=[])
                                with subprocess.Popen(
                                    shlex.split("bjobs {}".format(jobid[0])),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    bufsize=1,
                                    universal_newlines=True,
                                ) as proc:
                                    # check for limit for maximum number
                                    # of pending jobs
                                    pending_limit_reached = False
                                    for line in getattr(proc, pipe_limit_reached):
                                        pending_limit_reached = (
                                            msg_limit_reached in line
                                        )
                                        if pending_limit_reached:
                                            break
                                        else:
                                            output[pipe_limit_reached].append(line)

                                    # if the limit has been reached,
                                    # kill process and sleep
                                    if pending_limit_reached:
                                        proc.kill()
                                        LOGGER.warning(TIMEOUT_MESSAGE)
                                        time.sleep(60 * 30)
                                        continue

                                    # read rest of the output
                                    for line in proc.stdout:
                                        output["stdout"].append(line)
                                    for line in proc.stderr:
                                        output["stderr"].append(line)

                                    break

                            # check if process terminated successfully
                            if proc.returncode != 0:
                                raise RuntimeError(
                                    'Running the command "{}" failed with'
                                    "exit code {}. Error: \n{}".format(
                                        "bjobs {}".format(jobid[0]),
                                        proc.returncode,
                                        "\n".join(output["stderr"]),
                                    )
                                )

                            # check jobstate
                            jobstate = output["stdout"][-1].split()[2]
                            # for slurm either COMPLETED or FAILED?
                            if (jobstate == "DONE") | (jobstate == "EXIT"):
                                break
                            time.sleep(60)

                    else:
                        while True:
                            proc = subprocess.check_output(
                                shlex.split(f"sacct -j {jobid[0]} -o State")
                            ).decode()
                            proc = proc.replace(" ", "")
                            proc = proc.replace("State", "")
                            proc = proc.replace("-", "")
                            proc = proc.split("\n")
                            if ("RUNNING" not in proc) & ("PENDING" not in proc):
                                break
                            time.sleep(60)

elif function == "merge_log_files":
    LOGGER.info("Merge all log files")
    indices_all = utils.get_indices(tasks)
    indices_missing = utils.check_indices(
        indices_all,
        path_finished,
        executable,
        function_args,
        verbosity=args.esub_verbosity,
    )
    completed = len(indices_all) - len(indices_missing)

    stdout_log_tot, stderr_log_tot = utils.get_log_filenames(
        log_dir, job_name, "main", system="tot"
    )
    # store previous log file without header
    # (e.g. when running rerun_missing independently from main)
    with open(stdout_log_tot, "r") as o:
        log_main = o.read().splitlines(True)[8:-10]
    with open(stderr_log_tot, "r") as e:
        log_err = e.read()

    # empty files
    open(stdout_log_tot, "w").close()
    open(stderr_log_tot, "w").close()

    message = (
        "#######################################################\n"
        "This is the merged main log file\n"
        f"{completed} / {len(indices_all)} jobs were successfully completed\n"
        f"Still missing are \n {indices_missing}\n"
        "#######################################################\n"
    )
    utils.save_write(stdout_log_tot, message)
    mainlog = (
        "#######################################################\n"
        "MAIN LOG FILES\n"
        "#######################################################\n"
    )
    utils.save_write(stdout_log_tot, mainlog)

    LOGGER.info("Start merging main files")
    utils.save_write(stdout_log_tot, "".join(log_main))
    utils.save_write(stderr_log_tot, "".join(log_err))
    for i in range(1, len(indices_all) + 1):
        stdout_log, stderr_log = utils.get_log_filenames(
            log_dir, job_name, "main", system
        )
        try:
            log_o = open(stdout_log % i, "r")
            log_e = open(stderr_log % i, "r")
            utils.save_write(stdout_log_tot, log_o.read())
            utils.save_write(stderr_log_tot, log_e.read())
            log_o.close()
            log_e.close()
            os.remove(stdout_log % i)
            os.remove(stderr_log % i)
        except Exception as err:
            LOGGER.error("Logfile for index {} not found".format(i))
            LOGGER.error("error message: {}".format(err))

    rer_log = (
        "#######################################################\n"
        "Rerun LOG FILES\n"
        "Note that the log of the last rerun index can be found \n"
        "in the rerun_missing log file.\n"
        "#######################################################\n"
    )
    utils.save_write(stdout_log_tot, rer_log)
    LOGGER.info("Start merging rerun files")
    LOGGER.info("This is also done when rerun_missing was not called")
    for i in range(1, len(indices_all) + 1):
        stdout_log, stderr_log = utils.get_log_filenames(
            log_dir, job_name, "main_r", system
        )
        try:
            log_o = open(stdout_log % i, "r")
            log_e = open(stderr_log % i, "r")
            utils.save_write(stdout_log_tot, log_o.read())
            utils.save_write(stderr_log_tot, log_e.read())
            log_o.close()
            log_e.close()
            os.remove(stdout_log % i)
            os.remove(stderr_log % i)
        except Exception as err:
            LOGGER.warning("Logfile for index {} not found".format(i))
            LOGGER.warning("error message: {}".format(err))
    utils.save_write(stdout_log_tot, message)
    LOGGER.info("Merged the log files")

else:
    # Change to local scratch if set
    utils.cd_local_scratch(args.esub_verbosity)

    # getting index list based on jobid
    indices = utils.get_indices_splitted(tasks, n_jobs, rank)

    if function == "main":
        is_first = rank == 0

        if is_master:
            LOGGER.info("Running on tasks: {}".format(indices))
        if system == "daint":
            try:
                for index in getattr(executable, main_name)(indices, function_args):
                    if is_master:
                        utils.write_index(index, path_finished)
                        LOGGER.info(
                            "##################### Finished Task {}\
                            #####################".format(index)
                        )

                    if is_first:
                        utils.write_to_log(path_log, "First index is done")
                        is_first = False
            except TypeError:
                # MPI does not terminate properly, therefore kill it
                sys.exit(0)
        else:
            for index in getattr(executable, main_name)(indices, function_args):
                if is_master:
                    utils.write_index(index, path_finished)
                    LOGGER.info(
                        "##################### Finished Task {}\
                        #####################".format(index)
                    )

                if is_first:
                    utils.write_to_log(path_log, "First index is done")
                    is_first = False
    else:
        if is_master:
            utils.write_to_log(path_log, "Running {}".format(function))
            LOGGER.info(
                "Running {}, {} task(s), \
                        first: {}, last: {}".format(
                    function, len(indices), indices[0], indices[-1]
                )
            )
        getattr(executable, function)(indices, function_args)
        if is_master:
            utils.write_to_log(path_log, "Finished running {}".format(function))
