import DataCov
import Eigen
import EigenFace
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import Euclidian
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk
import sv_ttk


def facialrecog():
    global f1,t1,img3,result,result2,wkt,result3
    start=time.time()
    EigenFaces = EigenFace.EigenFace(f1)
    WData = Euclidian.WData(EigenFaces, f1)
    WTest = Euclidian.WTest(EigenFaces, f1, t1)
    val, index = Euclidian.MinEuclideanDistance(WData,WTest)
    print(val, index)
    print("---------------------------------------")
    threshold=750000000
    if val<threshold:
        path = r"" + f1
        dirs = os.listdir(path)
        k = 0
        for file in dirs:
            if (k==index):
                print(index)
                print(val)
                print(file)
                closeimg=f1+"/"+file
                break
            k += 1
        kemiripan=((threshold-val)/threshold)*100
        kemiripan=round(kemiripan,2)
        distance=round(val,2)
        tm=time.time()-start
        tm=round(tm,2)
        img3 = Image.open(closeimg)
        img3 = img3.resize((256,256), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        label = Label(image = img3)
        label.place(x=672, y=161)
        wkt=Label(text=str(tm)+" detik", font='century 18', fg="green", bg="peachpuff3")
        wkt.place(x=515, y=473)
        result=Label(text="kemiripan: "+str(kemiripan)+"%", font='century 14',fg="green",bg="peachpuff3")
        result.place(x=73, y=355)
        result2=Label(text="Distance: "+str(distance), font='century 14',fg="green",bg="peachpuff3")
        result2.place(x=73, y=377)
        result3=Label(text="file: "+str(file), font='century 14',fg="green",bg="peachpuff3")
        result3.place(x=73, y=400)
    else:
        tm=time.time()-start
        tm=round(tm,2)
        wkt=Label(text=str(tm)+" detik", font='century 18', fg="green", bg="peachpuff3")
        wkt.place(x=515, y=473)
        result=Label(text="kemiripan: 0%", font='century 14',fg="green",bg="peachpuff3")
        result.place(x=73, y=355)
        result2=Label(text="Distance: >750000000", font='century 14',fg="green",bg="peachpuff3")
        result2.place(x=73, y=377)
        result3=Label(text="file: -----", font='century 14',fg="green",bg="peachpuff3")
        result3.place(x=73, y=400)
        img3 = Image.open("src/GUI/Components/noimage.jpg")
        img3 = img3.resize((256,256), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        label = Label(image = img3)
        label.place(x=672, y=161)





root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")
bgimg= ImageTk.PhotoImage(file = "src/GUI/Components/final.jpg")
limg= Label(root, i=bgimg)
limg.pack()

f1="src/GUI/Components/noimage.jpg"
t1=""


nofile1=Label(text="No File Chosen", font='Helvatica 12',bg="peachpuff3")
nofile1.place(x=150, y=173)

nofile2=Label(text="No File Chosen", font='Helvatica 12',bg="peachpuff3")
nofile2.place(x=150, y=253)


result=Label(text="None", font='century 18',fg="green4",bg="peachpuff3")
result.place(x=73, y=350)

result2=Label(text="None", font='century 18',fg="green4",bg="peachpuff3")
result2.place(x=73, y=375)

result3=Label(text="None", font='century 18',fg="green4",bg="peachpuff3")
result3.place(x=73, y=400)

def choosefolder():
    global f1
    f1 = filedialog.askdirectory(initialdir="test")
    f1short=f1.split('/')[len(f1.split('/'))-1]
    nofile1["text"] = f1short
    nofile1["font"] = "century 10"


# def upload_file1():
#     global img1,f1
#     foldername = filedialog.askdirectory(initialdir="test")
#     img1 = Image.open(foldername)
#     img1 = img1.resize((256,256), Image.ANTIALIAS)
#     img1 = ImageTk.PhotoImage(img1)
#     f1=foldername


button1 = ttk.Button(text="Upload file", command=choosefolder)
button1.pack()
button1.place(x=73, y=170)


img2 = Image.open("src/GUI/Components/noimage.jpg")
img2 = img2.resize((256,256), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
label = Label( image = img2)
label.place(x=387, y=162)

img3 = Image.open(f1)
img3 = img3.resize((256,256), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
label = Label(image = img3)
label.place(x=672, y=162)

def upload_file2():
    global img2,t1
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img2 = Image.open(filename)
    img2 = img2.resize((256,256), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    label = Label(image = img2)
    label.place(x=387, y=161)
    shortfilename = filename.split('/')[len(filename.split('/'))-1]
    nofile2["text"] = shortfilename
    nofile2["font"] = "century 10"
    t1=filename

def clear():
    global img2,t1,img3,f1
    img2 = Image.open("src/GUI/Components/noimage.jpg")
    img2 = img2.resize((256,256), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    label = Label(image = img2)
    label.place(x=387, y=161)
    nofile2["text"] = "No File Chosen"
    nofile2["font"] = "century 12"
    t1=""
    img3 = Image.open("src/GUI/Components/noimage.jpg")
    img3 = img3.resize((256,256), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    label = Label(image = img3)
    label.place(x=672, y=161)



button2 = ttk.Button(text="upload file", command=upload_file2)
button2.pack()
button2.place(x=73, y=250)

button3 = ttk.Button(text="calculate", command=facialrecog)
button3.pack()
button3.place(x=135, y=325)

button4 = ttk.Button(text="clear", command=clear)
button4.pack()
button4.place(x=880, y=474)

wkt=Label(text="00:00", font='century 24', fg="green4", bg="peachpuff3")
wkt.place(x=515, y=468)

sv_ttk.set_theme("light")



root.mainloop()