from tkinter import *

root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")

label=Label(root, text="Face Recognition", font='Helvetica 30 bold')
label.place(relx=0.5, y=30, anchor=CENTER)

canvas=Canvas(root, width=900, height=5, bg="black")
canvas.pack()
canvas.create_line(100,200,200,35, fill="green", width=5)
canvas.place(relx=0.5, y=70, anchor=CENTER)

root.mainloop()