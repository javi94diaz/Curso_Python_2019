from tkinter import *
 
root = Tk()
 
root.title("Welcome to LikeGeeks app")
 
root.geometry('350x200')
 
lbl = Label(root, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(root,width=10)
 
txt.grid(column=1, row=0)
 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
 
btn = Button(root, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)
 
root.mainloop()