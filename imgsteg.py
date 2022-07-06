from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Image Steganography")
root.geometry("1200x900")
root.resizable(False,False)
root.configure(bg="#14141f")


def loadImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd,title="Select Image File",filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All Files","*.txt")))
    selImg=Image.open(filename)
    selImg=selImg.resize((550, 350))
    selImg=ImageTk.PhotoImage(selImg)
    imgLbl.configure(image=selImg)
    imgLbl.image=selImg

def writeData():
    global sus
    msg=textBox.get(1.0,END)
    sus=lsb.hide(str(filename),msg)
    messagebox.showinfo("Data Written!", "Data has been hidden inside the image successfully...")

def storeImage():
    fName=fileText.get(1.0,END)
    fName=fName.strip('\n')
    sus.save(str(fName)+".png")
    savedFilePath = str(os.getcwd())+"/"+str(fName)+".png"
    messagebox.showinfo("File saved!", "File has been saved in the location "+savedFilePath+" successfully...")


def readData():
    secMsg=lsb.reveal(str(filename))
    textBox.delete(1.0,END)
    textBox.insert(END,secMsg)



iconImg=PhotoImage(file="logo.png")
root.iconphoto(False,iconImg)

mainImg=PhotoImage(file="main.png")
mainImg=mainImg.subsample(3)
Label(root,image=mainImg,bg="#14141f").place(x=30,y=10)
Label(root,text="Image Steganography",font="Calibri 56 bold italic",bg="#14141f",fg="red").place(x=400,y=50)
Label(root,text="Selected Image:",font="Calibri 20 bold italic",bg="#14141f",fg="red").place(x=30,y=170)
Label(root,text="Data:",font="Calibri 20 bold italic",bg="#14141f",fg="red").place(x=700,y=170)


#frames
f1=Frame(root,bd=3,bg="grey",width=600,height=400,relief=GROOVE).place(x=30,y=200)
f2=Frame(root,bd=3,bg="white",width=400,height=400,relief=GROOVE).place(x=700,y=200)
f3=Frame(root,bd=3,bg="#14141f",width=500,height=200,relief=GROOVE).place(x=30,y=650)
f4=Frame(root,bd=3,bg="#14141f",width=500,height=200,relief=GROOVE).place(x=630,y=650)


#labels and textbox
imgLbl=Label(f1,bg="grey")
imgLbl.place(x=60,y=220)

textBox=Text(f2,font="Calibri 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
textBox.place(x=700,y=200,width=400,height=400)

Label(f3,text="(New filename)",font="Calibri 14 italic",bg="#14141f",fg="red").place(x=320,y=700)
fileText=Text(f3,font="Calibri 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
fileText.place(x=300,y=660,width=200,height=40)

scrollBar = Scrollbar(f2)
scrollBar.place(x=1090,y=200,height=400)
scrollBar.configure(command=textBox.yview)
textBox.configure(yscrollcommand=scrollBar.set)


#buttons
Button(f3,text="Load File",width=15,height=3,font="arial 15 italic",command=loadImage).place(x=70,y=730)
Button(f3,text="Store File",width=15,height=3,font="arial 15 italic",command=storeImage).place(x=300,y=730)
Label(f3,text="Image file",font="Calibri 24 bold italic",bg="#14141f",fg="red").place(x=40,y=660)

Button(f4,text="Read data",width=15,height=3,font="arial 15 italic",command=readData).place(x=670,y=730)
Button(f4,text="Write data",width=15,height=3,font="arial 15 italic",command=writeData).place(x=900,y=730)
Label(f4,text="Secret Message!",font="Calibri 24 bold italic",bg="#14141f",fg="red").place(x=640,y=660)

root.mainloop()
