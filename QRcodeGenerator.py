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
#Function to perform refresh
def refresh():
    pass
#Display QR Code
createQr()
QRimg =Image.open("QR.png")
QRimg = QRimg.resize((350,350),Image.ANTIALIAS)
img = ImageTk.PhotoImage(QRimg)
Canvas1 = Canvas(root)
imageContainer=Canvas1.create_image(250,190,image = img)  
Canvas1.config(bg="black",width = 300, height = 300)
Canvas1.pack(expand=True,fill=BOTH)

#Button to perform refresh
RefreshBtn = Button(root,text="Refresh",bg='green', fg='black',font=('Helvetica',20,"bold"), command=refresh)
RefreshBtn.place(relx=0.35,rely=0.85, relwidth=0.27,relheight=0.1)