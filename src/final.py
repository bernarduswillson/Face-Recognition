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


def cam():
    global img2,t1
    faceCascade = cv2.CascadeClassifier('/Users/Radit./Documents/kelas/smt3/Algeo/Algeo02-21021/src/haar.xml')
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x-60,y-60),(x+60+w,y+60+h),(255,0,0),2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            crop_img = frame[y-60:y+60+h, x-60:x+60+w]
            cv2.imwrite("muka.jpg", crop_img)
            break
    cap.release()
    cv2.destroyAllWindows()
    t1="muka.jpg"
    img2 = Image.open(t1)
    img2 = img2.resize((256,256), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    label = Label(image = img2)
    label.place(x=387, y=161)
    shortfilename = t1.split('/')[len(t1.split('/'))-1]
    nofile2["text"] = shortfilename
    nofile2["font"] = "century 10"

def facialrecog():
    global f1,t1,img3,result,result2,wkt,result3
    start=time.time()
    WTest = Euclidian.WTest(EigenFaces, f1, t1)
    val, index, t = Euclidian.MinEuclideanDistance(WData,WTest)
    print(val, index)
    print("---------------------------------------")
    threshold = 130000000
    print("Threshold: ",threshold)
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
        kemiripan=round(kemiripan,3)
        distance=round(val,2)
        tm=time.time()-start
        tm=round(tm,2)
        img3 = Image.open(closeimg)
        img3 = img3.resize((256,256), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        label = Label(image = img3)
        label.place(x=672, y=161)
        wkt.configure(text=str(tm)+" detik")
        result.configure(text="kemiripan: "+str(kemiripan)+"%",font="century 13",fg="green")
        result2.configure(text="jarak: "+str(distance),font="century 13",fg="green")
        result3.configure(text="file: "+str(file),font="century 13",fg="green")
    else:
        tm=time.time()-start
        tm=round(tm,2)
        wkt.configure(text=str(tm)+" detik")
        result.configure(text="kemiripan: 0%", font='century 14',fg="red",bg="peachpuff3")
        result2.configure(text="Distance: 0", font='century 14',fg="red",bg="peachpuff3")
        result3.configure(text="file: -", font='century 14',fg="red",bg="peachpuff3")
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
    global f1,WData,EigenFaces
    f1 = filedialog.askdirectory(initialdir="test")
    f1short=f1.split('/')[len(f1.split('/'))-1]
    nofile1["text"] = f1short
    nofile1["font"] = "century 10"
    EigenFaces = EigenFace.EigenFace(f1)
    WData = Euclidian.WData(EigenFaces, f1)


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

# def clear():
#     global img2,t1,img3,f1
#     img2 = Image.open("src/GUI/Components/noimage.jpg")
#     img2 = img2.resize((256,256), Image.ANTIALIAS)
#     img2 = ImageTk.PhotoImage(img2)
#     label = Label(image = img2)
#     label.place(x=387, y=161)
#     nofile2["text"] = "No File Chosen"
#     nofile2["font"] = "century 12"
#     t1=""
#     img3 = Image.open("src/GUI/Components/noimage.jpg")
#     img3 = img3.resize((256,256), Image.ANTIALIAS)
#     img3 = ImageTk.PhotoImage(img3)
#     label = Label(image = img3)
#     label.place(x=672, y=161)





button2 = ttk.Button(text="upload file", command=upload_file2)
button2.pack()
button2.place(x=73, y=250)

button3 = ttk.Button(text="calculate", command=facialrecog)
button3.pack()
button3.place(x=135, y=325)

button3 = ttk.Button(text="cam", command=cam)
button3.pack()
button3.place(x=73, y=280)

# button4 = ttk.Button(text="clear", command=clear)
# button4.pack()
# button4.place(x=880, y=474)

wkt=Label(text="00:00", font='century 24', fg="green4", bg="peachpuff3")
wkt.place(x=515, y=468)

sv_ttk.set_theme("light")



root.mainloop()