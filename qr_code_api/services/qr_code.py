import base64
from io import BytesIO

from fastapi import UploadFile
from PIL import Image
from pyqrcode import create as create_qr
from pyzbar.pyzbar import decode as decode_qr_image


class QRCodeService:
    def generate_qr_image(self, data: str) -> bytes:
        qr_code = create_qr(data)
        base64_string = qr_code.png_as_base64_str()
        return base64.b64decode(base64_string.encode("ascii"))

    async def read_from_image(self, file_upload: UploadFile) -> str:
        image_bytes = BytesIO(await file_upload.read())
        data = decode_qr_image(Image.open(image_bytes))

        return data[0][0]
