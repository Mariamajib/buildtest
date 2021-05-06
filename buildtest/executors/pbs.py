"""This module implements PBSExecutor class that defines how executors submit
job to PBS Scheduler"""
import logging
import json
import os


from buildtest.executors.base import BaseExecutor
from buildtest.exceptions import ExecutorError
from buildtest.executors.job import Job
from buildtest.utils.command import BuildTestCommand
from buildtest.utils.file import read_file
from buildtest.utils.tools import deep_get

logger = logging.getLogger(__name__)


class PBSExecutor(BaseExecutor):
    """The PBSExecutor class is responsible for submitting jobs to PBS Scheduler.
    The class implements the following methods:

    load: load PBS executors from configuration file
    dispatch: submit PBS job to scheduler
    poll: poll PBS job via qstat and retrieve job state
    gather: gather job result
    cancel: cancel job if it exceeds max pending time
    """

    type = "pbs"
    poll_cmd = "qstat"

    def __init__(self, name, settings, site_configs, max_pend_time=None):

        self.maxpendtime = max_pend_time
        super().__init__(name, settings, site_configs)

    def load(self):
        """Load the a Cobalt executor configuration from buildtest settings."""

        self.launcher = self._settings.get("launcher") or deep_get(
            self._buildtestsettings.target_config, "executors", "defaults", "launcher"
        )
        self.launcher_opts = self._settings.get("options")

        self.queue = self._settings.get("queue")
        self.account = self._settings.get("account") or deep_get(
            self._buildtestsettings.target_config, "executors", "defaults", "account"
        )

        self.max_pend_time = (
            self.maxpendtime
            or self._settings.get("max_pend_time")
            or deep_get(
                self._buildtestsettings.target_config,
                "executors",
                "defaults",
                "max_pend_time",
            )
        )

    def dispatch(self, builder):
        """This method is responsible for dispatching PBS job, get JobID
        and start record metadata in builder object. If job failed to submit
        we check returncode and exit with failure. After we submit job, we
        start timer and record when job was submitted and poll job once to get
        job details and store them in builder object.

        :param builder: builder object
        :type builder: BuilderBase, required
        """

        self.load()

        os.chdir(builder.stage_dir)

        batch_cmd = [self.launcher]

        if self.queue:
            batch_cmd += [f"-q {self.queue}"]

        if self.account:
            batch_cmd += [f"-P {self.account}"]

        if self.launcher_opts:
            batch_cmd += [" ".join(self.launcher_opts)]

        batch_cmd += [builder.metadata["testpath"]]
        builder.metadata["command"] = " ".join(batch_cmd)
        self.logger.debug(f"Running Test via command: {builder.metadata['command']}")
        command = BuildTestCommand(builder.metadata["command"])
        command.execute()
        # record start time in builder object
        self.start_time(builder)
        builder.start()

        # if qsub job submission returns non-zero exit that means we have failure, exit immediately
        if command.returncode != 0:
            err = f"[{builder.metadata['name']}] failed to submit job with returncode: {command.returncode} \n"
            err += (
                f"[{builder.metadata['name']}] running command: {' '.join(batch_cmd)}"
            )
            raise ExecutorError(err)

        parse_jobid = command.get_output()
        self.job_id = " ".join(parse_jobid).strip()

        builder.metadata["jobid"] = self.job_id

        builder.job = PBSJob(builder.metadata["jobid"])

        msg = f"[{builder.metadata['name']}] JobID: {builder.metadata['jobid']} dispatched to scheduler"
        print(msg)
        self.logger.debug(msg)

        """
        qstat_cmd = f"{self.poll_cmd} -f -F json {builder.metadata['jobid']}"
        cmd = BuildTestCommand(qstat_cmd)
        cmd.execute()
        output = cmd.get_output()
        output = " ".join(output)
        job_data = json.loads(output)

        # output in the form of <server>:<file>
        builder.metadata["outfile"] = job_data["Jobs"][self.job_id][
            "Output_Path"
        ].split(":")[1]
        builder.metadata["errfile"] = job_data["Jobs"][self.job_id]["Error_Path"].split(
            ":"
        )[1]
        """

    def poll(self, builder):
        """This method is responsible for polling Cobalt job, we check the
        job state and existence of output file. If file exists or job is in
        'exiting' stage we set job to 'done' stage and gather results. If job
        is in 'pending' stage we check if job exceeds 'max_pend_time' time limit
        by checking with builder timer attribute using ``start`` and ``stop`` method.
        If job exceeds the time limit job is cancelled.

        :param builder: builder object
        :type builder: BuilderBase, required
        """

        builder.job.poll()

        builder.metadata["outfile"] = builder.job.output_file()
        builder.metadata["errfile"] = builder.job.error_file()

        # if job in pending state (Q) check if it exceeds max_pend_time if so cancel job
        if builder.job.is_pending() or builder.job.is_suspended():
            builder.stop()
            self.logger.debug(f"Time Duration: {builder.duration}")
            self.logger.debug(f"Max Pend Time: {self.max_pend_time}")

            # if timer time is more than requested pend time then cancel job
            if int(builder.duration) > self.max_pend_time:
                builder.job.cancel()
                builder.job_state = "CANCELLED"
                print(
                    "Cancelling Job because duration time: {:f} sec exceeds max pend time: {} sec".format(
                        builder.duration, self.max_pend_time
                    )
                )

            builder.start()

        """
        self.logger.debug(f"Query Job: {builder.metadata['jobid']}")
        # run qstat -f -F json <jobid>
        qstat_cmd = f"{self.poll_cmd} -x -f -F json {builder.metadata['jobid']}"
        self.logger.debug(f"Executing command: {qstat_cmd}")
        cmd = BuildTestCommand(qstat_cmd)
        cmd.execute()
        output = cmd.get_output()
        output = " ".join(output)

        job_data = json.loads(output)

        self.logger.debug("Job record")
        self.logger.debug(json.dumps(job_data, indent=2))
        
        job_state = job_data["Jobs"][builder.metadata["jobid"]]["job_state"]

        if job_state:
            builder.job_state = job_state

        self.logger.debug(
            "[%s]: JobID %s in %s state ",
            builder.metadata["name"],
            builder.metadata["jobid"],
            builder.job_state,
        )
      
        # if job in pending state (Q) check if it exceeds max_pend_time if so cancel job
        if builder.job_state == "Q":
            builder.stop()
            self.logger.debug(f"Time Duration: {builder.duration}")
            self.logger.debug(f"Max Pend Time: {self.max_pend_time}")

            # if timer time is more than requested pend time then cancel job
            if int(builder.duration) > self.max_pend_time:
                self.cancel(builder)
                builder.job_state = "CANCELLED"
                print(
                    "Cancelling Job because duration time: {:f} sec exceeds max pend time: {} sec".format(
                        builder.duration, self.max_pend_time
                    )
                )

            builder.start()
          """

    def gather(self, builder):
        """This method is responsible for getting output of job using `qstat -x -f -F json <jobID>`
        and storing the result in builder object. We retrieve specific fields such as exit status,
        start time, end time, runtime and store them in builder object. We read output and error file
        and store the content in builder object.

        :param builder: builder object
        :type builder: BuilderBase, required
        """

        qstat_cmd = f"{self.poll_cmd} -x -f -F json {builder.metadata['jobid']}"

        self.logger.debug(f"Executing command: {qstat_cmd}")
        cmd = BuildTestCommand(qstat_cmd)
        cmd.execute()
        output = cmd.get_output()
        output = " ".join(output)

        job_data = json.loads(output)

        builder.metadata["result"]["returncode"] = job_data["Jobs"][
            builder.metadata["jobid"]
        ]["Exit_status"]

        # record endtime in builder object
        self.end_time(builder)

        builder.metadata["job"] = job_data

        builder.metadata["output"] = read_file(builder.metadata["outfile"])
        builder.metadata["error"] = read_file(builder.metadata["errfile"])

        self.check_test_state(builder)

    def cancel(self, builder):
        """Cancel Cobalt job using qdel, this operation is performed if job exceeds its max_pend_time.

        :param builder: builder object
        :type builder: BuilderBase, required
        """

        query = f"qdel {builder.metadata['jobid']}"

        cmd = BuildTestCommand(query)
        cmd.execute()
        msg = f"Cancelling Job: {builder.metadata['name']} running command: {query}"
        print(msg)
        self.logger.debug(msg)


class PBSJob(Job):
    """See https://www.altair.com/pdfs/pbsworks/PBSReferenceGuide2021.1.pdf section 8.1 for Job State Codes"""

    def __init__(self, jobID):
        super().__init__(jobID)

    def is_pending(self):
        return self._state == "Q"

    def is_running(self):
        return self._state == "R"

    def is_complete(self):
        return self._state == "F"

    def is_suspended(self):
        return self._state in ["H", "U", "S"]

    def success(self):
        """This method determines if job was completed successfully. According to https://www.altair.com/pdfs/pbsworks/PBSAdminGuide2021.1.pdf
        section 14.9 Job Exit Status Codes we have the following:
            Exit Code:  X < 0         - Job could not be executed
            Exit Code: 0 <= X < 128   -  Exit value of Shell or top-level process
            Exit Code: X >= 128       - Job was killed by signal

            Exit Code 0 is a success
        """
        return self._exitcode == 0

    def fail(self):
        return not self.success()

    def poll(self):
        query = f"qstat -x -f -F json {self.jobid}"

        logger.debug(query)
        cmd = BuildTestCommand(query)
        cmd.execute()
        output = " ".join(cmd.get_output())
        job_data = json.loads(output)

        self._state = job_data["Jobs"][self.jobid]["job_state"]
        # output in the form of pbs:<path>
        self._outfile = job_data["Jobs"][self.jobid]["Output_Path"].split(":")[1]
        self._errfile = job_data["Jobs"][self.jobid]["Error_Path"].split(":")[1]

        # The Exit_status property will be available when job is finished
        self._exitcode = job_data["Jobs"][self.jobid].get("Exit_status")

    def cancel(self):
        query = f"qdel {self.jobid}"
        logger.debug(f"Cancelling job {self.jobid} by running: {query}")
        cmd = BuildTestCommand(query)
        cmd.execute()

    def output_file(self):
        return self._outfile

    def error_file(self):
        return self._errfile

    def exitcode(self):
        return self._exitcode
