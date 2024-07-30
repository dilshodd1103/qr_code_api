from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import Response

from .container import Container
from .services import QRCodeService

router = APIRouter()


@router.post("/generate_qr/")
@inject
async def create_qr(
    data: str,
    qr_code_service: QRCodeService = Depends(Provide[Container.qr_code_service]),
):
    file_content = qr_code_service.generate_qr_image(data)
    return Response(content=file_content, media_type="image/png")


@router.post("/read_qr/")
@inject
async def read_qr(
    file: UploadFile = File(),
    qr_code_service: QRCodeService = Depends(Provide[Container.qr_code_service]),
):
    text = await qr_code_service.read_from_image(file)
    return {"text": text}
