# Copyright (C) 2019 ETH Zurich,
# Institute for Particle Physics and Astrophysics
# Author: Dominik Zuercher, adapted by Silvan Fischbacher

import datetime
import math
import multiprocessing
import os
import shlex
import shutil
import subprocess
import sys
import time
from functools import partial

import numpy as np
import portalocker
from ekit import logger as logger_utils

LOGGER = logger_utils.init_logger(__name__)
TIMEOUT_MESSAGE = (
    "Maximum number of pending jobs reached, will sleep for 30 minutes and retry"
)


def decimal_hours_to_str(dec_hours):
    """Transforms decimal hours into the hh:mm format

    :param dec_hours: decimal hours, float or int
    :return: string in the format hh:mm
    """

    full_hours = math.floor(dec_hours)
    minutes = math.ceil((dec_hours - full_hours) * 60)

    if minutes == 60:
        full_hours += 1
        minutes = 0

    if minutes < 10:
        time_str = "{}:0{}".format(full_hours, minutes)
    else:
        time_str = "{}:{}".format(full_hours, minutes)

    return time_str


def make_resource_string(
    function,
    main_memory,
    main_time,
    main_scratch,
    main_n_cores,
    main_gpu,
    main_gpu_memory,
    watchdog_memory,
    watchdog_time,
    watchdog_scratch,
    watchdog_n_cores,
    watchdog_gpu,
    watchdog_gpu_memory,
    merge_memory,
    merge_time,
    merge_scratch,
    merge_n_cores,
    merge_gpu,
    merge_gpu_memory,
    system,
    verbosity=3,
):
    """
    Creates the part of the submission string which handles
    the allocation of ressources

    :param function: The name of the function defined
                     in the executable that will be submitted
    :param main_memory: Memory per core to allocate for the main job
    :param main_time: The Wall time requested for the main job
    :param main_scratch: Scratch per core to allocate for the main job
    :param main_n_cores: Number of cores to allocate for the main job
    :param main_gpu: Number of GPUs to allocate for the main job
    :param main_gpu_memory: Memory per GPU to allocate for the main job
    :param watchdog_memory: Memory per core to allocate for the watchdog job
    :param watchdog_time: The Wall time requested for the watchdog job
    :param watchdog_scratch: Scratch to allocate for the watchdog job
    :param watchdog_n_cores: Number of cores to allocate for the watchdog job
    :param watchdog_gpu: Number of GPUs to allocate for the watchdog job
    :param watchdog_gpu_memory: Memory per GPU to allocate for the watchdog job
    :param merge_memory: Memory per core to allocate for the merge job
    :param merge_time: The Wall time requested for the merge job
    :param merge_scratch: Scratch to allocate for the merge jo
    :param merge_n_cores: Number of cores to allocate for the merge job
    :param merge_gpu: Number of GPUs to allocate for the merge job
    :param merge_gpu_memory: Memory per GPU to allocate for the merge job
    :param system: The type of the queing system of the cluster
    :param verbosity: Verbosity level (0 - 4).
    :return: A string that is part of the submission string and the gpu string that
                needs to added to srun
    """

    logger_utils.set_logger_level(LOGGER, verbosity)

    gpu_cmd = ""

    if function == "main":
        mem = main_memory
        time = main_time
        scratch = main_scratch
        n_cores = main_n_cores
        gpu = main_gpu
        gpu_memory = main_gpu_memory
    elif function == "watchdog":
        mem = watchdog_memory
        time = watchdog_time
        scratch = watchdog_scratch
        n_cores = watchdog_n_cores
        gpu = watchdog_gpu
        gpu_memory = watchdog_gpu_memory
    elif function == "merge":
        mem = merge_memory
        time = merge_time
        scratch = merge_scratch
        n_cores = merge_n_cores
        gpu = merge_gpu
        gpu_memory = merge_gpu_memory
    elif function == "rerun_missing":
        mem = main_memory
        time = main_time
        scratch = main_scratch
        n_cores = main_n_cores
        gpu = main_gpu
        gpu_memory = main_gpu_memory
    elif function == "merge_log_files":
        mem = main_memory
        time = 4
        scratch = main_scratch
        n_cores = 1
        gpu = 0
        gpu_memory = 0
    if system == "bsub":
        resource_string = (
            "-W {} -R rusage[mem={}] " "-R rusage[scratch={}] " "-n {}".format(
                decimal_hours_to_str(time), mem, scratch, n_cores
            )
        )
    elif system == "slurm":
        resource_string = (
            "#SBATCH --time={}:00 \n"
            "#SBATCH --mem-per-cpu={} \n"
            "#SBATCH --tmp={} \n"
            "#SBATCH --cpus-per-task={} \n".format(
                decimal_hours_to_str(time), int(mem), int(scratch), n_cores
            )
        )
        if gpu > 0:
            resource_string += "#SBATCH --gpus={} \n".format(gpu)
            gpumem_in_gb = gpu_memory / 1024
            resource_string += f"#SBATCH --gres=gpumem:{gpumem_in_gb:.0f}g \n"
            # slurm needs the gpus and gres argument to be passed to srun and sbatch
            gpu_cmd = f"--gpus={gpu} --gres=gpumem:{gpumem_in_gb:.0f}g "

        resource_string += "\n"

    elif system == "daint":
        resource_string = "#SBATCH --time={}:00 \n#SBATCH --mem={} \n \n".format(
            decimal_hours_to_str(time), mem
        )
        # TODO: local scratch for slurm
        if scratch > 0:
            LOGGER.warning(
                "Not Implemented Warning: Automatic local scratch "
                "allocation not supported for DAINT system. Ignoring."
            )
    LOGGER.debug(f"Built resource string as {resource_string}")

    return resource_string, gpu_cmd


def get_log_filenames(log_dir, job_name, function, system="bsub"):
    """
    Builds the filenames of the stdout and stderr log files for a
    given job name and a given function to run.

    :param log_dir: directory where the logs are stored
    :param job_name: Name of the job that will write to the log files
    :param function: Function that will be executed
    :param system: The type of the queing system of the cluster
    :return: filenames for stdout and stderr logs
    """
    job_name_ext = job_name + "_" + function
    if system == "slurm" and (function == "main" or function == "main_r"):
        stdout_log = os.path.join(log_dir, "{}_index%a.o".format(job_name_ext))
        stderr_log = os.path.join(log_dir, "{}_index%a.e".format(job_name_ext))
    else:
        stdout_log = os.path.join(log_dir, "{}.o".format(job_name_ext))
        stderr_log = os.path.join(log_dir, "{}.e".format(job_name_ext))
    return stdout_log, stderr_log


def get_source_cmd(source_file, verbosity=3):
    """
    Builds the command to source a given file if the file exists,
    otherwise returns an empty string.

    :param source_file: path to the (possibly non-existing) source file,
                        can be relative and can contain "~"
    :param verbosity: Verbosity level (0 - 4).
    :return: command to source the file if it exists or empty string
    """

    logger_utils.set_logger_level(LOGGER, verbosity)

    source_file_abs = os.path.abspath(os.path.expanduser(source_file))

    if os.path.isfile(source_file_abs):
        source_cmd = "source {}; ".format(source_file_abs)
        LOGGER.debug(f"Running source script at {source_file_abs}")
    else:
        LOGGER.warning("Source file {} not found, skipping".format(source_file))
        source_cmd = ""

    return source_cmd


def get_dependency_string(function, jobids, ext_dependencies, system, verbosity=3):
    """
    Constructs the dependency string which handles which other jobs
    this job is dependent on.

    :param function: The type o function to submit
    :param jobids: Dictionary of the jobids for each job already submitted
    :param ext_dependencies: If external dependencies are given they get
                             added to the dependency string
                             (this happens if epipe is used)
    :param system: The type of the queing system of the cluster
    :param verbosity: Verbosity level (0 - 4).
    :return: A sting which is used as a substring for the submission string
             and it handles the dependencies of the job
    """
    logger_utils.set_logger_level(LOGGER, verbosity)

    dep_string = ""
    # no dependencies for main
    if function == "main":
        if ext_dependencies != "":
            dep_string = '-w "' + ext_dependencies + '"'
        else:
            dep_string = ""
            return dep_string
        if system == "slurm":
            dep_string = dep_string.replace("ended(", "afterany:")
            dep_string = dep_string.replace("started(", "after:")
            dep_string = dep_string.replace(") && ", ",")
            dep_string = dep_string.replace(")", "")
            dep_string = dep_string.replace('-w "', '--dependency="')
        return dep_string
    # watchdog starts along with main
    elif function == "watchdog":
        if "main" in jobids.keys():
            for id in jobids["main"]:
                dep_string += "{}({}) && ".format("started", id)
        else:
            LOGGER.warning(
                "Function {} has not been submitted -> Skipping "
                "in dependencies for {}".format("main", function)
            )
    # rerun missing starts after main
    elif function == "rerun_missing":
        if "main" in jobids.keys():
            for id in jobids["main"]:
                dep_string += "{}({}) && ".format("ended", id)
        else:
            LOGGER.warning(
                "Function {} has not been submitted -> Skipping "
                "in dependencies for {}".format("main", function)
            )
    # merge_log_files starts after main or rerun_missing
    elif function == "merge_log_files":
        if "rerun_missing" in jobids.keys():
            for id in jobids["rerun_missing"]:
                dep_string += "{}({}) && ".format("ended", id)
        elif "main" in jobids.keys():
            for id in jobids["main"]:
                dep_string += "{}({}) && ".format("ended", id)
    # merge starts after all the others
    elif function == "merge":
        if "main" in jobids.keys():
            for id in jobids["main"]:
                dep_string += "{}({}) && ".format("ended", id)
        else:
            LOGGER.warning(
                "Function {} has not been submitted -> Skipping "
                "in dependencies for {}".format("main", function)
            )
        if "watchdog" in jobids.keys():
            for id in jobids["watchdog"]:
                dep_string += "{}({}) && ".format("ended", id)
        else:
            LOGGER.warning(
                "Function {} has not been submitted -> Skipping "
                "in dependencies for {}".format("watchdog", function)
            )
        if "rerun_missing" in jobids.keys():
            for id in jobids["rerun_missing"]:
                dep_string += "{}({}) && ".format("ended", id)
        else:
            LOGGER.warning(
                "Function {} has not been submitted -> Skipping "
                "in dependencies for {}".format("rerun_missing", function)
            )
    else:
        raise ValueError("Dependencies for function" " {} not defined".format(function))
    # remove trailing &&
    if len(dep_string) > 0:
        dep_string = dep_string[:-4]
    if ext_dependencies != "":
        dep_string = dep_string + " && " + ext_dependencies
        # remove leading &&
        if dep_string[:4] == " && ":
            dep_string = dep_string[4:]
    dep_string = '-w "' + dep_string + '"'

    if system == "slurm":
        dep_string = dep_string.replace("ended(", "afterany:")
        dep_string = dep_string.replace("started(", "after:")
        dep_string = dep_string.replace(") && ", ",")
        dep_string = dep_string.replace(")", "")
        dep_string = dep_string.replace('-w "', '--dependency="')

    if len(dep_string) > 0:
        LOGGER.debug(f"Built dependency string as {dep_string}")
    return dep_string


def make_cmd_string(
    function,
    source_file,
    n_jobs,
    tasks,
    mode,
    job_name,
    function_args,
    exe,
    main_memory,
    main_time,
    main_scratch,
    main_n_cores,
    main_gpu,
    main_gpu_memory,
    rerun_missing_memory,
    rerun_missing_time,
    rerun_missing_scratch,
    rerun_missing_n_cores,
    watchdog_time,
    watchdog_memory,
    watchdog_scratch,
    watchdog_n_cores,
    watchdog_gpu,
    watchdog_gpu_memory,
    merge_memory,
    merge_time,
    merge_scratch,
    merge_n_cores,
    merge_gpu,
    merge_gpu_memory,
    log_dir,
    dependency,
    system,
    main_name="main",
    batchsize=100000,
    max_njobs=-1,
    add_args="",
    add_bsub="",
    discard_output=False,
    verbosity=3,
    main_mode="jobarray",
    # main_n_cores=1,
    nodes=1,
    MPI_tasks_per_core=1,
    MPI_tasks_per_node=1,
    OpenMP_threads_per_task=1,
    keep_submit_files=False,
):
    """
    Creates the submission string which gets submitted to the queing system

    :param function: The name of the function defined in the
                     executable that will be submitted
    :param source_file: A file which gets executed
                        before running the actual function(s)
    :param n_jobs: The number of jobs that will be requested for the job
    :param tasks: The task string, which will get parsed into the job indices
    :param mode: The mode in which the job will be
                 ran (MPI-job or as a jobarray)
    :param job_name: The name of the job
    :param function_args: The remaining arguments that
                          will be forwarded to the executable
    :param exe: The path of the executable
    :param main_memory: Memory per core to allocate for the main job
    :param main_time: The Wall time requested for the main job
    :param main_scratch: Scratch per core to allocate for the main job
    :param main_n_cores: Number of cores to allocate for the main job
    :param main_gpu: Number of GPUs to allocate for the main job
    :param main_gpu_memory: Memory per GPU to allocate for the main job
    :param rerun_missing_memory: Memory per core to allocate for the rerun job
    :param rerun_missing_time: The Wall time requested for the rerun job
    :param rerun_missing_scratch: Scratch per core to allocate for the rerun job
    :param rerun_missing_n_cores: Number of cores to allocate for the rerun job
    :param watchdog_memory: Memory per core to allocate for the watchdog job
    :param watchdog_time: The Wall time requested for the watchdog job
    :param watchdog_scratch: Scratch to allocate for the watchdog job
    :param watchdog_n_cores: Number of cores to allocate for the watchdog job
    :param watchdog_gpu: Number of GPUs to allocate for the watchdog job
    :param watchdog_gpu_memory: Memory per GPU to allocate for the watchdog job
    :param merge_memory: Memory per core to allocate for the merge job
    :param merge_time: The Wall time requested for the merge job
    :param merge_scratch: Scratch to allocate for the merge job
    :param merge_n_cores: Number of cores to allocate for the merge job
    :param merge_gpu: Number of GPUs to allocate for the merge job
    :param merge_gpu_memory: Memory per GPU to allocate for the merge job
    :param log_dir: log_dir: The path to the log directory
    :param dependency: The dependency string
    :param system: The type of the queing system of the cluster
    :param main_name: name of the main function
    :param batchsize: If not zero the jobarray gets divided into batches.
    :param max_njobs: Maximum number of jobs allowed to run at the same time.
    :param add_args: Additional cluster-specific arguments
    :param add_bsub: Additional bsub arguments to pass
    :param discard_output: If True writes stdout/stderr to /dev/null
    :param verbosity: Verbosity level (0 - 4).
    :param main_mode: The mode in which the main job will be run
    :param nodes: Number of nodes to allocate for the main job
    :param MPI_tasks_per_core: Number of MPI tasks per core
    :param MPI_tasks_per_node: Number of MPI tasks per node
    :param OpenMP_threads_per_task: Number of OpenMP threads per task
    :param keep_submit_files: If True, keeps the submit files after submission
    :return: The submission string that wil get submitted to the cluster
    """

    logger_utils.set_logger_level(LOGGER, verbosity)

    # rerun_missing should use the same resources as main, but can be overwritten
    # by the rerun_ arguments
    if (function == "rerun_missing") | (function == "main_rerun"):
        if rerun_missing_memory is not None:
            main_memory = rerun_missing_memory
        if rerun_missing_time is not None:
            main_time = rerun_missing_time
        if rerun_missing_scratch is not None:
            main_scratch = rerun_missing_scratch
        if rerun_missing_n_cores is not None:
            main_n_cores = rerun_missing_n_cores

    if function == "main_rerun":
        function = "main"
        if system == "slurm":
            # reruns should use different log files to avoid overwriting
            log_function = "main_r"
        else:
            log_function = "main"
    else:
        log_function = function

    # allocate computing resources
    resource_string, gpu_cmd = make_resource_string(
        function,
        main_memory,
        main_time,
        main_scratch,
        main_n_cores,
        main_gpu,
        main_gpu_memory,
        watchdog_memory,
        watchdog_time,
        watchdog_scratch,
        watchdog_n_cores,
        watchdog_gpu,
        watchdog_gpu_memory,
        merge_memory,
        merge_time,
        merge_scratch,
        merge_n_cores,
        merge_gpu,
        merge_gpu_memory,
        system,
        verbosity,
    )

    # get the job name for the submission system and the log files
    job_name_ext = job_name + "_" + function
    stdout_log, stderr_log = get_log_filenames(log_dir, job_name, log_function, system)

    # construct the string of arguments passed to the executable
    args_string = ""
    for arg in function_args:
        args_string += arg + " "

    # make submission string
    source_cmd = get_source_cmd(source_file, verbosity)

    if mode == "mpi":
        run_cmd = "mpirun python"
    elif mode == "jobarray":
        run_cmd = "python"
    else:
        raise ValueError(f"Run mode {mode} is not known")

    extra_args_string = (
        "--source_file={} --main_memory={} --main_time={} "
        "--main_scratch={} --function={} "
        "--executable={} --n_jobs={} "
        "--log_dir={} --system={} "
        "--main_name={} --batchsize={} --max_njobs={} "
        "--main_n_cores={} --main_gpu={} --main_gpu_memory={} "
        "--esub_verbosity={} --main_mode={} --mode={} --additional_bsub_args={}"
        "--additional_slurm_args={} --keep_submit_files={} {}".format(
            source_file,
            main_memory,
            main_time,
            main_scratch,
            function,
            exe,
            n_jobs,
            log_dir,
            system,
            main_name,
            batchsize,
            max_njobs,
            main_n_cores,
            main_gpu,
            main_gpu_memory,
            verbosity,
            main_mode,
            mode,
            add_bsub,
            add_args,
            keep_submit_files,
            args_string,
        )
    )

    if (function == "main") & (max_njobs > 0):
        max_string = "%{}".format(max_njobs)
    else:
        max_string = ""

    if system == "bsub":
        if n_jobs <= batchsize:
            cmd_string = (
                "bsub -o {} -e {} -J {}[1-{}]{} "
                "{} {} {}"
                ' "{} {} -m esub.submit --job_name={} '
                "--tasks='{}' {}".format(
                    stdout_log,
                    stderr_log,
                    job_name_ext,
                    n_jobs,
                    max_string,
                    resource_string,
                    add_bsub,
                    dependency,
                    source_cmd,
                    run_cmd,
                    job_name,
                    tasks,
                    extra_args_string,
                )
            )
        else:
            LOGGER.warning(
                "You have requested a jobarray with more "
                f"than {batchsize} cores"
                ". Euler cannot handle this. I break down this job into "
                "multiple subarrays and submit them one by one. "
                "Note that this feature currently breakes the rerun "
                "missing capability. Also note that"
                " this process needs to keep running...."
            )

            n_batches = math.ceil(n_jobs / batchsize)
            cmd_string = []
            for rank in range(n_batches):
                if rank < (n_batches - 1):
                    jobs = batchsize
                else:
                    jobs = n_jobs % batchsize
                    if jobs == 0:
                        jobs = batchsize
                first_task = get_indices_splitted(tasks, n_jobs, rank * batchsize)
                first_task = first_task[0]
                last_task = get_indices_splitted(
                    tasks, n_jobs, rank * batchsize + jobs - 1
                )
                last_task = last_task[-1]
                tasks_ = f"{first_task} > {last_task + 1}"

                jobname_ = f"{job_name}_{rank}"
                stdout_log_ = stdout_log[:-2] + f"_{rank}.o"
                stderr_log_ = stdout_log[:-2] + f"_{rank}.e"
                cs = (
                    "bsub -o {} -e {} -J {}[1-{}]{} "
                    '{} {} "{} '
                    "{} -m esub.submit --job_name={} --tasks='{}' {}".format(
                        stdout_log_,
                        stderr_log_,
                        job_name_ext,
                        jobs,
                        max_string,
                        resource_string,
                        dependency,
                        source_cmd,
                        run_cmd,
                        jobname_,
                        tasks_,
                        extra_args_string,
                    )
                )
                cmd_string.append(cs)
        if discard_output:
            if isinstance(cmd_string, list):
                for i in range(len(cmd_string)):
                    cmd_string[i] = cmd_string[i] + " --discard_output &> /dev/null"
            else:
                cmd_string += " --discard_output &> /dev/null"
    elif system == "slurm":
        # split add_args
        if len(add_args) > 0:
            add_args = add_args.split(",")
        else:
            add_args = []

        cmd_string = "sbatch {} submit_{}.slurm".format(dependency, job_name_ext)

        # write submission file
        with open(f"submit_{job_name_ext}.slurm", "w+") as f:
            f.write("#! /bin/bash \n#\n")
            if discard_output:
                f.write("#SBATCH --output=/dev/null \n")
                f.write("#SBATCH --error=/dev/null \n")
            else:
                f.write("#SBATCH --output={} \n".format(stdout_log))
                f.write("#SBATCH --error={} \n".format(stderr_log))
            f.write("#SBATCH --job-name={} \n".format(job_name_ext))
            for arg in add_args:
                f.write("#SBATCH {} \n".format(arg))
            f.write("#SBATCH --array=1-{}{} \n".format(n_jobs, max_string))
            f.write(resource_string)
            f.write(
                "srun {}bash; {} {} -m esub.submit --job_name={} "
                "--tasks='{}' {}".format(
                    gpu_cmd,
                    source_cmd,
                    run_cmd,
                    job_name,
                    tasks,
                    extra_args_string[:-1],
                )
            )
    elif system == "daint":
        # split add_args
        if len(add_args) > 0:
            add_args = add_args.split(",")
        else:
            add_args = []

        cmd_string = "sbatch {} submit_{}.slurm".format(dependency, job_name_ext)

        # write submission file
        with open(f"submit_{job_name_ext}.slurm", "w+") as f:
            f.write("#! /bin/bash \n#\n")
            if discard_output:
                f.write("#SBATCH --output=/dev/null \n")
                f.write("#SBATCH --error=/dev/null \n")
            else:
                f.write("#SBATCH --output={} \n".format(stdout_log))
                f.write("#SBATCH --error={} \n".format(stderr_log))
            f.write("#SBATCH --job-name={} \n".format(job_name_ext))
            f.write("#SBATCH --constraint=gpu \n")
            f.write("#SBATCH --nodes={} \n".format(nodes))
            f.write("#SBATCH --ntasks-per-core={} \n".format(MPI_tasks_per_core))
            f.write("#SBATCH --ntasks-per-node={} \n".format(MPI_tasks_per_node))
            f.write("#SBATCH --cpus-per-task={} \n".format(OpenMP_threads_per_task))
            for arg in add_args:
                f.write("#SBATCH {} \n".format(arg))
            f.write(resource_string)
            if len(source_cmd) > 0:
                f.write("srun {} \n".format(source_cmd))
            f.write(
                "srun python -m esub.submit --job_name={} " "--tasks='{}' {}".format(
                    job_name, tasks, extra_args_string[:-1]
                )
            )

    LOGGER.debug(f"Built total command string as {cmd_string}")
    return cmd_string


def submit_job(
    tasks,
    mode,
    exe,
    log_dir,
    function_args,
    function="main",
    source_file="",
    n_jobs=1,
    job_name="job",
    main_memory=100,
    main_time=1,
    main_scratch=1000,
    main_n_cores=1,
    main_gpu=0,
    main_gpu_memory=1000,
    rerun_missing_memory=None,
    rerun_missing_time=None,
    rerun_missing_scratch=None,
    rerun_missing_n_cores=None,
    watchdog_memory=100,
    watchdog_time=1,
    watchdog_scratch=1000,
    watchdog_n_cores=1,
    watchdog_gpu=0,
    watchdog_gpu_memory=1000,
    merge_memory=100,
    merge_time=1,
    merge_scratch=1000,
    merge_n_cores=1,
    merge_gpu=0,
    merge_gpu_memory=1000,
    dependency="",
    system="bsub",
    main_name="main",
    test=False,
    batchsize=100000,
    max_njobs=100000,
    add_args="",
    add_bsub="",
    discard_output=False,
    verbosity=3,
    main_mode="jobarray",
    keep_submit_files=False,
    nodes=1,
    MPI_tasks_per_core=1,
    MPI_tasks_per_node=1,
    OpenMP_threads_per_task=1,
):
    """
    Based on arguments gets the submission string and submits it to the cluster

    :param tasks: The task string, which will get parsed into the job indices
    :param mode: The mode in which the job will be ran
                 (MPI-job or as a jobarray)
    :param exe: The path of the executable
    :param log_dir: The path to the log directory
    :param function_args: The remaining arguments that will
                          be forwarded to the executable
    :param function: The name of the function defined in the
                     executable that will be submitted
    :param source_file: A file which gets executed before
                        running the actual function(s)
    :param n_jobs: The number of jobs that will be requested for the job
    :param job_name: The name of the job
    :param main_memory: Memory per core to allocate for the main job
    :param main_time: The Wall time requested for the main job
    :param main_scratch: Scratch per core to allocate for the main job
    :param main_n_cores: Number of cores to allocate for the main job
    :param main_gpu: Number of GPUs to allocate for the main job
    :param main_gpu_memory: Memory per GPU to allocate for the main job
    :param rerun_missing_memory: Memory per core to allocate for the rerun job, if None the
                            main_memory will be used
    :param rerun_missing_time: The Wall time requested for the rerun job, if None the
                            main_time will be used
    :param rerun_missing_scratch: Scratch per core to allocate for the rerun job, if None the
                            main_scratch will be used
    :param rerun_missing_n_cores: Number of cores to allocate for the rerun job, if None the
                            main_n_cores will be used
    :param watchdog_memory: Memory per core to allocate for the watchdog job
    :param watchdog_time: The Wall time requested for the watchdog job
    :param watchdog_scratch: Scratch to allocate for the watchdog job
    :param watchdog_n_cores: Number of cores to allocate for the watchdog job
    :param watchdog_gpu: Number of GPUs to allocate for the watchdog job
    :param watchdog_gpu_memory: Memory per GPU to allocate for the watchdog job
    :param merge_memory: Memory per core to allocate for the merge job
    :param merge_time: The Wall time requested for the merge job
    :param merge_scratch: Scratch to allocate for the merge job
    :param merge_n_cores: Number of cores to allocate for the merge job
    :param merge_gpu: Number of GPUs to allocate for the merge job
    :param merge_gpu_memory: Memory per GPU to allocate for the merge job
    :param dependency: The jobids of the jobs on which this job depends on
    :param system: The type of the queing system of the cluster
    :param main_name: name of the main function
    :param test: If True no submission but just printing submission string to
                 log
    :param batchsize: If number of cores requested is > batchsize, break up
                      jobarrays into jobarrys of size batchsize
    :param max_njobs: Maximum number of jobs allowed to run at the same time
    :param add_args: Additional cluster-specific arguments
    :param add_bsub: Additional bsub arguments to pass
    :param discard_output: If True writes stdout/stderr to /dev/null
    :param verbosity: Verbosity level (0 - 4).
    :param keep_submit_files: If True store SLURM submission files
    :return: The jobid of the submitted job
    """

    logger_utils.set_logger_level(LOGGER, verbosity)
    # assess if number of tasks is valid
    n_tasks = len(get_indices_splitted(tasks, 1, 0))
    if (n_jobs > n_tasks) & (("mpi" not in mode) & (mode != "tasks")):
        raise Exception(
            "You tried to request more jobs than you have tasks. "
            "I assume this is a mistake. Aborting..."
        )
    # get submission string
    cmd_string = make_cmd_string(
        function,
        source_file,
        n_jobs,
        tasks,
        mode,
        job_name,
        function_args,
        exe,
        main_memory,
        main_time,
        main_scratch,
        main_n_cores,
        main_gpu,
        main_gpu_memory,
        rerun_missing_memory,
        rerun_missing_time,
        rerun_missing_scratch,
        rerun_missing_n_cores,
        watchdog_time,
        watchdog_memory,
        watchdog_scratch,
        watchdog_n_cores,
        watchdog_gpu,
        watchdog_gpu_memory,
        merge_memory,
        merge_time,
        merge_scratch,
        merge_n_cores,
        merge_gpu,
        merge_gpu_memory,
        log_dir,
        dependency,
        system,
        main_name,
        batchsize,
        max_njobs,
        add_bsub=add_bsub,
        add_args=add_args,
        discard_output=discard_output,
        verbosity=verbosity,
        main_mode=main_mode,
        # main_n_cores=main_n_cores,
        nodes=nodes,
        MPI_tasks_per_core=MPI_tasks_per_core,
        MPI_tasks_per_node=MPI_tasks_per_node,
        OpenMP_threads_per_task=OpenMP_threads_per_task,
        keep_submit_files=keep_submit_files,
    )
    LOGGER.debug(cmd_string)
    if test:
        path_log = get_path_log(log_dir, job_name)
        write_to_log(path_log, cmd_string)
        return []

    # message the system sends if the
    # maximum number of pendings jobs is reached
    msg_limit_reached = "Pending job threshold reached."
    pipe_limit_reached = "stderr"

    if isinstance(cmd_string, str):
        cmd_string = [cmd_string]

    jobids = []
    for cs in cmd_string:
        LOGGER.info("Submitting command:")
        LOGGER.info(cs)
        # submit
        while True:
            output = dict(stdout=[], stderr=[])

            with subprocess.Popen(
                shlex.split(cs),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,
                universal_newlines=True,
            ) as proc:
                # check for limit concerning maximum number of pending jobs
                if system == "bsub":
                    for line in getattr(proc, pipe_limit_reached):
                        pending_limit_reached = msg_limit_reached in line
                        if pending_limit_reached:
                            break
                        else:
                            output[pipe_limit_reached].append(line)

                    # if the limit has been reached, kill process and sleep
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
                    cmd_string, proc.returncode, "\n".join(output["stderr"])
                )
            )

        # get id of submitted job
        if system == "bsub":
            jobid = output["stdout"][-1].split("<")[1]
            jobid = jobid.split(">")[0]
        elif system == "slurm":
            jobid = output["stdout"][-1].split("job ")[-1]
            if not keep_submit_files:
                for cs in cmd_string:
                    os.remove(f"{cs.split(' ')[-1]}")
        elif system == "daint":
            jobid = output["stdout"][-1].split("job ")[-1]
            if not keep_submit_files:
                for cs in cmd_string:
                    os.remove(f"{cs.split(' ')[-1]}")
        jobids.append(int(jobid))

    LOGGER.info("Submitted job and got jobid(s): {}".format(jobid))
    return jobids


def robust_remove(path):
    """
    Remove a file or directory if existing

    :param path: path to possible non-existing file or directory
    """
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    # recreate
    open(path, "a").close()


def get_path_log(log_dir, job_name):
    """
    Construct the path of the esub log file

    :param log_dir: directory where log files are stored
    :param job_name: name of the job that will be logged
    :return: path of the log file
    """
    path_log = os.path.join(log_dir, job_name + ".log")

    return path_log


def get_path_finished_indices(log_dir, job_name):
    """
    Construct the path of the file containing the finished indices

    :param log_dir: directory where log files are stored
    :param job_name: name of the job for which the indices will be store
    :return: path of the file for the finished indices
    """
    path_finished = os.path.join(log_dir, job_name + "_done.dat")
    return path_finished


def import_executable(exe):
    """
    Imports the functions defined in the executable file.

    :param exe: path of the executable
    :return: executable imported as python module
    """
    sys.path.insert(0, os.path.dirname(exe))
    to_import = os.path.basename(exe).replace(".py", "")
    try:
        executable = __import__(to_import)
    except ImportError:
        raise ImportError(f"Failed to import your executable {exe}")
    return executable


def save_write(path, str_to_write, mode="a"):
    """
    Write a string to a file, with the file being locked in the meantime.

    :param path: path of file
    :param str_to_write: string to be written
    :param mode: mode in which file is opened
    """
    with portalocker.Lock(path, mode=mode, timeout=math.inf) as f:
        # write
        f.write(str_to_write)
        # flush and sync to filesystem
        f.flush()
        os.fsync(f.fileno())


def write_index(index, finished_file):
    """
    Writes the index number on a new line of the
    file containing the finished indices

    :param index: A job index
    :param finished_file: The file to which the
                          jobs will write that they are done
    """
    save_write(finished_file, "{}\n".format(index))


def check_indices(
    indices,
    finished_file,
    exe,
    function_args,
    check_indices_file=True,
    verbosity=3,
):
    """
    Checks which of the indices are missing in
    the file containing the finished indices

    :param indices: Job indices that should be checked
    :param finished_file: The file from which the jobs will be read
    :param exe: Path to executable
    :param check_indices_file: If True adds indices from index file otherwise
                               only use check_missing function
    :param verbosity: Verbosity level (0 - 4).
    :return: Returns the indices that are missing
    """
    if check_indices_file:
        LOGGER.debug("Checking missing file for missing indices...")
        # wait for the indices file to be written
        if os.path.exists(finished_file):
            # first get the indices missing in the log file (crashed jobs)
            done = []
            with open(finished_file, "r") as f:
                for line in f:
                    # Ignore empty lines
                    if line != "\n":
                        done.append(int(line.replace("\n", "")))
            failed = list(set(indices) - set(done))
            LOGGER.debug(f"Found failed indices: {failed}")
        else:
            LOGGER.warning(
                "Did not find File {} -> None of the main functions "
                "recorded its indices. "
                "Not rerunning any jobs".format(finished_file)
            )
            failed = []
    else:
        failed = []

    # if provided use check_missing function
    # (finished jobs but created corrupted output)
    if hasattr(exe, "check_missing"):
        LOGGER.info("Found check_missing function in executable. Running...")
        corrupted = getattr(exe, "check_missing")(indices, function_args)
        LOGGER.debug(f"Found corruped indices: {corrupted}")
    else:
        corrupted = []

    missing = failed + corrupted
    missing = np.unique(np.asarray(missing))
    LOGGER.debug(f"Found failed/corrputed indices: {missing}")
    return missing


def write_to_log(path, line, mode="a"):
    """
    Write a line to a esub log file

    :param path: path of the log file
    :param line: line (string) to write
    :param mode: mode in which the log file will be opened
    """
    extended_line = "{}    {}\n".format(datetime.datetime.now(), line)
    save_write(path, extended_line, mode=mode)


def cd_local_scratch(verbosity=3):
    """
    Change to current working directory to the local scratch if set.

    :param verbosity: Verbosity level (0 - 4).
    """
    if "ESUB_LOCAL_SCRATCH" in os.environ:
        if os.path.isdir(os.environ["ESUB_LOCAL_SCRATCH"]):
            submit_dir = os.getcwd()
            os.chdir(os.environ["ESUB_LOCAL_SCRATCH"])
            os.environ["SUBMIT_DIR"] = submit_dir

            LOGGER.warning(
                "Changed current working directory to {} and "
                "set $SUBMIT_DIR to {}".format(os.getcwd(), os.environ["SUBMIT_DIR"])
            )
        else:
            LOGGER.error(
                "$ESUB_LOCAL_SCRATCH is set to non-existing "
                "directory {}, skipping...".format(os.environ["ESUB_LOCAL_SCRATCH"])
            )
    else:
        LOGGER.debug(
            "Environment variable ESUB_LOCAL_SCRATCH not set. "
            "Not chaning working directory."
        )


def run_local_mpi_job(
    exe, n_cores, function_args, logger, main_name="main", verbosity=3
):
    """
    This function runs an MPI job locally

    :param exe: Path to executable
    :param n_cores: Number of cores
    :param function_args: A list of arguments to be passed to the executable
    :param index: Index number to run
    :param logger: logger instance for logging
    :param main_name: Name of main function in executable
    :param verbosity: Verbosity level (0 - 4).
    :param main_name:
    """
    # construct the string of arguments passed to the executable
    args_string = ""
    for arg in function_args:
        args_string += arg + " "

    # make command string
    cmd_string = (
        "mpirun -np {} python -m esub.submit"
        " --executable={} --tasks='0' --main_name={} "
        "--esub_verbosity={} {}".format(n_cores, exe, main_name, verbosity, args_string)
    )
    for line in execute_local_mpi_job(cmd_string):
        line = line.strip()
        if len(line) > 0:
            logger.info(line)


def get_indices(tasks):
    """
    Parses the jobids from the tasks string.

    :param tasks: The task string, which will get parsed into the job indices
    :return: A list of the jobids that should be executed
    """
    # parsing a list of indices from the tasks argument
    if ">" in tasks:
        tasks = tasks.split(">")
        start = tasks[0].replace(" ", "")
        stop = tasks[1].replace(" ", "")
        indices = list(range(int(start), int(stop)))
    elif "," in tasks:
        indices = tasks.split(",")
        indices = list(map(int, indices))
    elif os.path.exists(tasks):
        with open(tasks, "r") as f:
            content = f.readline()
        indices = get_indices(content)
    else:
        try:
            indices = [int(tasks)]
        except ValueError:
            raise ValueError("Tasks argument is not in the correct format!")
    return indices


def get_indices_splitted(tasks, n_jobs, rank):
    """
    Parses the jobids from the tasks string.
    Performs load-balance splitting of the jobs and returns the indices
    corresponding to rank. This is only used for job array submission.

    :param tasks: The task string, which will get parsed into the job indices
    :param n_jobs: The number of cores that will be requested for the job
    :param rank: The rank of the core
    :return: A list of the jobids that should
             be executed by the core with number rank
    """

    # Parse
    indices = get_indices(tasks)

    # Load-balanced splitter
    steps = len(indices)
    size = n_jobs
    chunky = int(steps / size)
    rest = steps - chunky * size
    mini = chunky * rank
    maxi = chunky * (rank + 1)
    if rank >= (size - 1) - rest:
        maxi += 2 + rank - size + rest
        mini += rank - size + 1 + rest
    mini = int(mini)
    maxi = int(maxi)

    return indices[mini:maxi]


def function_wrapper(indices, args, func):
    """
    Wrapper that converts a generator to a function.

    :param generator: A generator
    """
    inds = []
    for ii in func(indices, args):
        inds.append(ii)
    return inds


def run_local_tasks(exe, n_jobs, function_args, tasks, function):
    """
    Executes an MPI job locally, running each splitted index list on one core.

    :param exe: The executable from where the main function is imported.
    :param n_jobs: The number of cores to allocate.
    :param function_args: The arguments that
                          will get passed to the main function.
    :param tasks: The indices to run on.
    :param function: The function name to run
    """

    LOGGER.warning(
        "NotImplementedWarning: Using run-tasks creates a multiprocessing "
        "worker pool with just one thread per job. "
        "The n_core arguments are ignored."
    )
    # get executable
    func = getattr(exe, function)

    # Fix function arguments for all walkers
    run_func = partial(function_wrapper, args=function_args, func=func)

    # get splitted indices
    nums = []
    for rank in range(n_jobs):
        nums.append(get_indices_splitted(tasks, n_jobs, rank))

    # Setup mutltiprocessing pool
    pool = multiprocessing.Pool(processes=n_jobs)
    if int(multiprocessing.cpu_count()) < n_jobs:
        raise Exception(
            "Number of CPUs available is smaller \
             than requested number of CPUs"
        )

    # run and retrive the finished indices
    out = pool.map(run_func, nums)
    out = [item for sublist in out for item in sublist]
    return out


def execute_local_mpi_job(cmd_string):
    """
    Execution of local MPI job

    :param cmd_string: The command string to run
    """
    popen = subprocess.Popen(
        shlex.split(cmd_string),
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd_string)
