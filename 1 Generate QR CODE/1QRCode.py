
import qrcode

data = "URL_LINK"

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10 
)

qr.add_data(data)
qr.make(fit=True)  

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code1.png")

print("QR code generated successfully!")

