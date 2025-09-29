"""
    QApp Platform Project pennylane_invocation.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from quapp_common.component.backend.invocation import Invocation
from quapp_common.config.thread_config import circuit_exporting_pool
from quapp_common.data.async_task.circuit_export.backend_holder import BackendDataHolder
from quapp_common.data.async_task.circuit_export.circuit_holder import CircuitDataHolder
from quapp_common.data.request.invocation_request import InvocationRequest
from quapp_common.model.provider.provider import Provider

from ...async_tasks.qsharp_circuit_export_task import QsharpCircuitExportTask
from ...factory.qsharp_device_factory import QsharpDeviceFactory
from ...factory.qsharp_provider_factory import QsharpProviderFactory

class QsharpInvocation(Invocation):

    def __init__(self, request_data: InvocationRequest, **kwargs):
        super().__init__(request_data)
        self.num_qubits = kwargs.get('num_qubits')

    def _export_circuit(self, circuit):
        self.logger.info("[QsharpInvocation] _export_circuit()")

        circuit_export_task = QsharpCircuitExportTask(
            circuit_data_holder=CircuitDataHolder(circuit, self.circuit_export_url),
            backend_data_holder=BackendDataHolder(
                self.backend_information, self.authentication.user_token
            ),
            project_header=self.project_header,
            workspace_header=self.workspace_header
        )
        circuit_exporting_pool.submit(circuit_export_task.do)

    def _create_provider(self):
        self.logger.info('[QsharpInvocation] _create_provider()')

        return QsharpProviderFactory.create_provider(
            provider_type=self.backend_information.provider_tag, sdk=self.sdk,
            authentication=self.backend_information.authentication)

    def _create_device(self, provider: Provider):
        self.logger.info('[QsharpInvocation] Creating device')
        return QsharpDeviceFactory.create_device(provider=provider,
                                                    device_specification=self.backend_information.device_name,
                                                    authentication=self.backend_information.authentication,
                                                    sdk=self.sdk, num_qubits=self.num_qubits,
                                                    input=self.input)

    def _get_qubit_amount(self, circuit):
        # no method to get qubit amount in qsharp
        return 1