"""
    QApp Platform Project
    pennylane_device_factory.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from quapp_common.config.logging_config import logger
from quapp_common.enum.provider_tag import ProviderTag
from quapp_common.enum.sdk import Sdk
from quapp_common.factory.device_factory import DeviceFactory
from quapp_common.model.provider.provider import Provider
from ..model.device.quapp_qsharp_device import QuappQsharpDevice
from ..model.device.azure_quantum_qsharp_device import AzureQuantumQsharpDevice

class QsharpDeviceFactory(DeviceFactory):

    @staticmethod
    def create_device(provider: Provider, device_specification: str, authentication: dict, sdk: Sdk,
                      **kwargs):
        logger.info("[QsharpDeviceFactory] create_device()")

        provider_type = ProviderTag.resolve(provider.get_provider_type().value)

        logger.info("[QsharpDeviceFactory] provider type:" + str(provider_type))

        match provider_type:
            case ProviderTag.QUAO_QUANTUM_SIMULATOR:
                if Sdk.QSHARP == sdk:
                    logger.debug('[QsharpDeviceFactory] Creating QuappQsharpDevice')
                    return QuappQsharpDevice(provider, device_specification)
            case ProviderTag.AZURE_QUANTUM:
                if Sdk.QSHARP == sdk:
                    logger.debug('[QsharpDeviceFactory] Creating AzureQuantumQsharpDevice')
                    return AzureQuantumQsharpDevice(provider, device_specification)
            case _:
                raise ValueError(f"Unsupported provider type: {provider_type}")