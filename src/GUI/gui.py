from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")
bgimg= ImageTk.PhotoImage(file = "D:/Algeo02-21021/src/GUI/background.jpg")
#Specify the file name present in the same directory or else
#specify the proper path for retrieving the image to set it as background image.
limg= Label(root, i=bgimg)
limg.pack()

label=Label(root, text="Face Recognition", font='Helvetica 30 bold', bg="navy", fg="white", width=20, height=2, borderwidth=3, relief="solid")
label.place(relx=0.5, y=30, anchor=CENTER)

canvas=Canvas(root, width=900, height=5, bg="black")
canvas.pack()
canvas.place(relx=0.5, y=75, anchor=CENTER)

frame_left=Frame(root, width=270, height=380, bg="grey81", borderwidth=2, relief="solid")
frame_left.place(x=50, y=120)

label=Label(root, text="Insert Your Dataset", font='Helvatica 15', bg="grey81")
label.place(x=70, y=130)

img1 = Image.open("D:/Algeo02-21021/src/GUI/button.png")
img1 = img1.resize((70,50), Image.ANTIALIAS)
login_btn1 = ImageTk.PhotoImage(img1)
button1 = Button(image = login_btn1, borderwidth = 0, height=20, bg="grey81", activebackground='grey81')
button1.pack()
button1.place(x=70, y=165)

label=Label(root, text="Insert Your Image", font='Varela 15', bg="grey81")
label.place(x=70, y=210)

img2 = Image.open("D:/Algeo02-21021/src/GUI/button.png")
img2 = img2.resize((70,50), Image.ANTIALIAS)
login_btn2 = ImageTk.PhotoImage(img2)
button2 = Button(image = login_btn2, borderwidth = 0, height=20, bg="grey81", activebackground='grey81')
button2.pack()
button2.place(x=70, y=245)

label=Label(root, text="Result", font='Varela 15', bg="grey81")
label.place(x=70, y=310)

frame_right=Frame(root, width=575, height=380, bg="grey81", borderwidth=2, relief="solid")
frame_right.place(x=370, y=120)

root.mainloop()