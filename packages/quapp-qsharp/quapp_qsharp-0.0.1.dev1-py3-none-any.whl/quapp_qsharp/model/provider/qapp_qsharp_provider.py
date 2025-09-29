"""
    QApp Platform Project
    qapp_pennylane_provider.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from quapp_common.config.logging_config import logger
from quapp_common.enum.provider_tag import ProviderTag
from quapp_common.model.provider.provider import Provider

import qsharp

class QAppQsharpProvider(Provider):
    def __init__(self, ):
        logger.debug('[QAppQsharpProvider] get_backend()')
        super().__init__(ProviderTag.QUAO_QUANTUM_SIMULATOR)

    def get_backend(self, device_specification):
        logger.debug('[QAppQsharpProvider] get_backend()')

        try:
            print(device_specification)
            return qsharp
        except Exception as e:
            print(e)
            raise ValueError('[QAppQsharpProvider] Unsupported device')

    def collect_provider(self):
        logger.debug('[QAppQsharpProvider] collect_provider()')
        return None