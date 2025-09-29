"""
    QApp Platform Project
    qapp_pennylane_provider.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from quapp_common.config.logging_config import logger
from quapp_common.enum.provider_tag import ProviderTag
from quapp_common.model.provider.provider import Provider

from azure.quantum import Workspace 


class AzureQuantumQsharpProvider(Provider):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        logger.debug('[AzureQuantumQsharpProvider] get_backend()')
        super().__init__(ProviderTag.AZURE_QUANTUM)

    def get_backend(self, device_specification) -> any:
        logger.debug('[AzureQuantumQsharpProvider] get_backend()')

        try:
            workspace = Workspace.from_connection_string(self.connection_string)
            return workspace.get_targets(device_specification)
        except Exception as e:
            print(e)
            raise ValueError('[AzureQuantumQsharpProvider] Unsupported device')

    def collect_provider(self):
        logger.debug('[AzureQuantumQsharpProvider] collect_provider()')
        return None