# import qrcode
# def qrcode_generator(text):
#     qr = qrcode.QRCode(
#         version=5,
#         error_correction= qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4
#     )

#     qr.add_data(text)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color = "black", back_color = "white")
#     img.save("qr1.png")
    
# message = input("Write some message: ")
    
# qrcode_generator(message)

import qrcode

def qr_generator(text):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=4,
        box_size=10
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "Black", back_color ="White")
    
    img.save("qr2.png")
    
message = input("Enter your message: ")

qr_generator(message)