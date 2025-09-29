"""
    QApp Platform Project
    pennylane_provider_factory.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from quapp_common.config.logging_config import logger
from quapp_common.enum.provider_tag import ProviderTag
from quapp_common.enum.sdk import Sdk
from quapp_common.factory.provider_factory import ProviderFactory

from ..model.provider.azure_quantum_qsharp_provider import AzureQuantumQsharpProvider
from ..model.provider.qapp_qsharp_provider import QAppQsharpProvider

class QsharpProviderFactory(ProviderFactory):

    @staticmethod
    def create_provider(provider_type: ProviderTag, sdk: Sdk, authentication: dict):
        logger.info("[QsharpProviderFactory] create_provider()")
        logger.debug(f"provider_type: {provider_type}, sdk: {sdk}, authentication: {authentication}")

        match provider_type:
            case ProviderTag.QUAO_QUANTUM_SIMULATOR:
                if Sdk.QSHARP.__eq__(sdk):
                    return QAppQsharpProvider()
                raise ValueError(f'Unsupported SDK for provider type: {provider_type}')
            case ProviderTag.AZURE_QUANTUM:
                if Sdk.QSHARP.__eq__(sdk):
                    return AzureQuantumQsharpProvider(
                       connection_string=authentication.get("connectionString")
                    )
                raise ValueError(f'Unsupported SDK for provider type: {provider_type}')

            case _:
                raise ValueError(f'Unsupported provider type: {provider_type}')