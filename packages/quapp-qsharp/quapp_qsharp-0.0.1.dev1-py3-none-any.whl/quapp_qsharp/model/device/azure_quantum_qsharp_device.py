"""
    QApp Platform Project
    qapp_qsharp_device.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from quapp_common.data.response.authentication import Authentication
from quapp_common.data.response.custom_header import CustomHeader
from quapp_common.model.device.device import Device
from quapp_common.data.device.circuit_running_option import CircuitRunningOption
from quapp_common.model.provider.provider import Provider
from quapp_common.data.response.job_response import JobResponse

from quapp_common.component.callback.update_job_metadata import update_job_metadata
from quapp_common.enum.status.job_status import JobStatus
from quapp_common.enum.media_type import MediaType
from quapp_common.enum.status.status_code import StatusCode
from quapp_common.data.callback.callback_url import CallbackUrl

from datetime import datetime


class AzureQuantumQsharpDevice(Device):
    def __init__(self, provider: Provider, device_specification: str):
        super().__init__(provider, device_specification)
        self.logger.debug('[AzureQuantumQsharpDevice] Initializing device specification')
        self.device_specification = device_specification
        self.execution_time = 0
        self.job = None

    def _create_job(self, circuit, options: CircuitRunningOption):
        self.logger.debug(
            '[AzureQuantumQsharpDevice] Creating job with {0} shots'.format(
                options.shots))

        job = self.device.submit(circuit,
                                 "quapp" + str(datetime.now().timestamp()),
                                 shots=options.shots)

        job.wait_until_completed()
        self.job = job
        return job

    def _is_simulator(self) -> bool:
        self.logger.debug('[AzureQuantumQsharpDevice] is quantum machine')
        return False

    def _get_provider_job_id(self, job) -> str:
        self.logger.debug('[QsharpDevice] Getting job id')

        return job.id

    def _get_job_status(self, job) -> str:
        self.logger.debug('[QsharpDevice] Getting job status')

        return "DONE"

    def _calculate_execution_time(self, job_result):
        self.logger.debug('[QsharpDevice] Getting execution time {}',job_result)

        # the time unit is miliseconds
        return (self.job.details.end_execution_time- self.job.details.begin_execution_time).total_seconds() * 1000.0

    def _get_job_result(self, job):
        
        return job.get_results()

    def _produce_histogram_data(self, job_result) -> dict | None:
        self.logger.info('[QsharpDevice] Producing histogram data')

        return None


    def _on_execution(self, authentication: Authentication,
                      project_header: CustomHeader,
                      workspace_header: CustomHeader,
                      execution_callback: CallbackUrl, circuit,
                      options: CircuitRunningOption):
        """

        @param authentication: authentication information
        @param project_header: project header information
        @param execution_callback: execution step callback urls
        @param circuit: circuit will be run
        @param options: options will use for running
        @return: job and job response
        """
        self.logger.debug("On execution started")

        job_response = JobResponse(authentication=authentication,
                                   project_header=project_header,
                                   workspace_header=workspace_header,
                                   status_code=StatusCode.DONE)

        update_job_metadata(job_response=job_response,
                            callback_url=execution_callback.on_start)
        try:
            job = self._create_job(circuit=circuit, options=options)
            job_response.provider_job_id = self._get_provider_job_id(job)
            job_response.job_status = self._get_job_status(job)

            job_result = self._get_job_result(job)
            job_response.job_result = job_result
            original_job_result = job_result

            update_job_metadata(job_response=job_response,
                                callback_url=execution_callback.on_done)

            return original_job_result, job_response

        except Exception as exception:
            self.logger.debug(
                    "Execute job failed with error {}".format(str(exception)))

            job_response.status_code = StatusCode.ERROR
            job_response.content_type = MediaType.APPLICATION_JSON
            job_response.job_status = JobStatus.ERROR.value
            job_response.job_result = {"error": str(exception)}

            update_job_metadata(job_response=job_response,
                                callback_url=execution_callback.on_error)
            return None, None