import qrcode
from PIL import Image

qr_obj = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr_obj.add_data("https://vanshsadadiwala.github.io/Portfolio/")
qr_obj.make(fit=True)

# Create colored QR
img = qr_obj.make_image(fill_color="purple", back_color="white").convert("RGB")


img.save("portfolio_qr_colored.jpg")
