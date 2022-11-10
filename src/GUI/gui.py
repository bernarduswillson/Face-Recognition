from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")
bgimg= ImageTk.PhotoImage(file = "src/GUI/Components/background.jpg")
limg= Label(root, i=bgimg)
limg.pack()


title=Label(root, text="Face Recognition", font='Helvetica 30 bold', bg="midnightblue", fg="white", width=20, height=2, borderwidth=3, relief="solid")
title.place(relx=0.5, y=30, anchor=CENTER)


canvas=Canvas(root, width=900, height=5, bg="black")
canvas.pack()
canvas.place(relx=0.5, y=75, anchor=CENTER)


frame_left=Frame(root, width=270, height=410, bg="grey81", borderwidth=2, relief="solid")
frame_left.place(x=50, y=120)

indataset=Label(frame_left, text="Insert Your Dataset", font='Helvatica 15', bg="grey81")
indataset.place(x=20, y=10)

nofile1=Label(frame_left, text="No File Chosen", font='Helvatica 12', bg="grey81")
nofile1.place(x=100, y=45)

inimage=Label(frame_left, text="Insert Your Image", font='Helvatica 15', bg="grey81")
inimage.place(x=20, y=90)

nofile2=Label(frame_left, text="No File Chosen", font='Helvatica 12', bg="grey81")
nofile2.place(x=100, y=125)

tresult=Label(frame_left, text="Result", font='Helvatica 15', bg="grey81")
tresult.place(x=20, y=200)

result=Label(frame_left, text="None", font='Helvatica 12', bg="grey81", fg="green4")
result.place(x=50, y=235)


frame_right=Frame(root, width=575, height=310, bg="grey81", borderwidth=2, relief="solid")
frame_right.place(x=370, y=120)


def upload_file1():
    foldername = filedialog.askdirectory(initialdir="test")

imgb1 = Image.open("src/GUI/Components/button.png")
imgb1 = imgb1.resize((80,30), Image.ANTIALIAS)
login_btn1 = ImageTk.PhotoImage(imgb1)
button1 = Button(frame_left, image = login_btn1, borderwidth = 0, height=32, bg="grey81", activebackground='grey81', command=upload_file1)
button1.pack()
button1.place(x=20, y=40)


img2 = Image.open("src/GUI/Components/noimage.jpg")
img2 = img2.resize((256,256), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
label = Label(frame_right, image = img2)
label.place(x=10, y=40)

def upload_file2():
    global img2
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img2 = Image.open(filename)
    img2 = img2.resize((256,256), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    label = Label(frame_right, image = img2)
    label.place(x=10, y=40)
    filename = filename.split('/')[len(filename.split('/'))-1]
    nofile2["text"] = filename
    nofile2["font"] = "Helvatica 8"

imgb2 = Image.open("src/GUI/Components/button.png")
imgb2 = imgb2.resize((80,30), Image.ANTIALIAS)
login_btn2 = ImageTk.PhotoImage(imgb2)
button2 = Button(frame_left, image = login_btn2, borderwidth = 0, height=32, bg="grey81", activebackground='grey81', command=upload_file2)
button2.pack()
button2.place(x=20, y=120)


test=Label(frame_right, text="Test Image", font='Helvatica 12', bg="grey81", fg="black")
test.place(x=10, y=10)

close=Label(frame_right, text="Closest Image", font='Helvatica 12', bg="grey81", fg="black")
close.place(x=300, y=10)


img3 = Image.open("src/GUI/Components/noimage.jpg")
img3 = img3.resize((256,256), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
label = Label(frame_right, image = img3)
label.place(x=300, y=40)


frame_bot=Frame(root, width=575, height=80, bg="grey81", borderwidth=2, relief="solid")
frame_bot.place(x=370, y=450)

exetime=Label(frame_bot, text="Execution Time :", font='Helvatica 12', bg="grey81", fg="black")
exetime.place(x=10, y=25)

time=Label(frame_bot, text="00:00", font='Helvatica 12', bg="grey81", fg="green4")
time.place(x=130, y=25)

root.mainloop()