#imports
from tkinter import *
from tkinter import *
import qrcode
from PIL import ImageTk,Image 

#creating the window
root = Tk()
root.title("QrCodeGenerator")
root.minsize(width=400,height=400)
root.geometry("500x500")
root.mainloop()

#Create QR from text stored in Clipboard
def createQr():
    input_data = root.clipboard_get()
    qr = qrcode.QRCode(
            version=5,
            box_size=10,
            border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('QR.png')