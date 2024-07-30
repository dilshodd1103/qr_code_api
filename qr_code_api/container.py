from dependency_injector import containers, providers

from .services import QRCodeService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    qr_code_service = providers.Factory(QRCodeService)
