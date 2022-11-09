from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")
bgimg= ImageTk.PhotoImage(file = "src/GUI/background.jpg")
limg= Label(root, i=bgimg)
limg.pack()

label=Label(root, text="Face Recognition", font='Helvetica 30 bold', bg="midnightblue", fg="white", width=20, height=2, borderwidth=3, relief="solid")
label.place(relx=0.5, y=30, anchor=CENTER)

canvas=Canvas(root, width=900, height=5, bg="black")
canvas.pack()
canvas.place(relx=0.5, y=75, anchor=CENTER)

frame_left=Frame(root, width=270, height=410, bg="grey81", borderwidth=2, relief="solid")
frame_left.place(x=50, y=120)

label=Label(frame_left, text="Insert Your Dataset", font='Helvatica 15', bg="grey81")
label.place(x=20, y=10)

img1 = Image.open("src/GUI/button.png")
img1 = img1.resize((70,50), Image.ANTIALIAS)
login_btn1 = ImageTk.PhotoImage(img1)
button1 = Button(frame_left, image = login_btn1, borderwidth = 0, height=20, bg="grey81", activebackground='grey81')
button1.pack()
button1.place(x=20, y=45)

label=Label(frame_left, text="No File Chosen", font='Helvatica 12', bg="grey81")
label.place(x=100, y=45)

label=Label(frame_left, text="Insert Your Image", font='Helvatica 15', bg="grey81")
label.place(x=20, y=90)

img2 = Image.open("src/GUI/button.png")
img2 = img2.resize((70,50), Image.ANTIALIAS)
login_btn2 = ImageTk.PhotoImage(img2)
button2 = Button(frame_left, image = login_btn2, borderwidth = 0, height=20, bg="grey81", activebackground='grey81')
button2.pack()
button2.place(x=20, y=125)

label=Label(frame_left, text="No File Chosen", font='Helvatica 12', bg="grey81")
label.place(x=100, y=125)

label=Label(frame_left, text="Result", font='Helvatica 15', bg="grey81")
label.place(x=20, y=200)

label=Label(frame_left, text="None", font='Helvatica 12', bg="grey81", fg="green4")
label.place(x=50, y=235)

frame_right=Frame(root, width=575, height=310, bg="grey81", borderwidth=2, relief="solid")
frame_right.place(x=370, y=120)

label=Label(frame_right, text="Test Image", font='Helvatica 12', bg="grey81", fg="black")
label.place(x=10, y=10)

img3 = Image.open("src/GUI/example.png")
img3 = img3.resize((256,256), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
label = Label(frame_right, image = img3)
label.place(x=10, y=40)

label=Label(frame_right, text="Closest Image", font='Helvatica 12', bg="grey81", fg="black")
label.place(x=300, y=10)

img4 = Image.open("src/GUI/example.png")
img4 = img4.resize((256,256), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img4)
label = Label(frame_right, image = img4)
label.place(x=300, y=40)

frame_bot=Frame(root, width=575, height=80, bg="grey81", borderwidth=2, relief="solid")
frame_bot.place(x=370, y=450)

label=Label(frame_bot, text="Execution Time :", font='Helvatica 12', bg="grey81", fg="black")
label.place(x=10, y=25)

label=Label(frame_bot, text="00:00", font='Helvatica 12', bg="grey81", fg="green4")
label.place(x=130, y=25)

root.mainloop()