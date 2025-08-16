# Making QR code

import qrcode
from PIL import Image
qr=qrcode.QRCode(version =1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=40, border=4)

qr.add_data("https://drive.google.com/file/d/1zBAgjsZ1xBrGfqhAiV6FCyatxwr5INvP/view?usp=drivesdk")
#qr.make(fit=True)
image=qr.make_image(fill_color="red",back_color="pink")
image.save("INK2BYTE.png")