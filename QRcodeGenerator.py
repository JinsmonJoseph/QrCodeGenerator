#imports
from tkinter import *
import qrcode
from PIL import ImageTk,Image 

#creating the window
root = Tk()
root.title("QrCodeGenerator")
root.minsize(width=400,height=400)
root.geometry("500x550")

#Create QR from text stored in Clipboard
input_data=""
def createQr():
    global input_data
    try:
        input_data = root.clipboard_get()
    except:
        input_data="--CLIP BOARD IS EMPTY --"
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
    global img
    global input_data
    createQr()
    Canvas1.imgref = img
    QRimg =Image.open("QR.png")
    QRimg = QRimg.resize((250,250),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(QRimg)
    Canvas1.itemconfig(imageContainer,image=img)
    CopiedTextLabel.configure(text=input_data)


#Display QR Code
createQr()
QRimg =Image.open("QR.png")
QRimg = QRimg.resize((250,250),Image.ANTIALIAS)
img = ImageTk.PhotoImage(QRimg)
Canvas1 = Canvas(root)
imageContainer=Canvas1.create_image(250,190,image = img)  
Canvas1.config(bg="black",width = 300, height = 300)
Canvas1.pack(expand=True,fill=BOTH)

#Label showing clipboard text
labelFrame = Frame(root,bg="#FFFFFF")
labelFrame.place(relx=0.05,rely=0.6,relwidth=0.9,relheight=0.20)
CopiedTextLabel = Label(labelFrame, text=input_data, bg='black', fg='white', font=('Helvetica',7,"bold"))
CopiedTextLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Button to perform refresh
RefreshBtn = Button(root,text="Refresh",bg='green', fg='black',font=('Helvetica',20,"bold"), command=refresh)
RefreshBtn.place(relx=0.35,rely=0.8, relwidth=0.27,relheight=0.1)

root.mainloop()