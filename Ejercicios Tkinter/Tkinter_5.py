# Ventana con dos frames, el primero con dos botones y el segundo con una etiqueta de texto que cambia al pulsar uno de los botones

import tkinter as tk
    

def write_slogan():
    # print("Tkinter is easy to use!")
    label.config(text='Tkinter is easy to use!')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=root.quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

frame2 = tk.Frame(root)
frame2.pack()
label = tk.Label(frame2, text="Hello Tkinter!")
label.pack()

root.mainloop()