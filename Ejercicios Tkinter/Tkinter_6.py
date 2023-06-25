import tkinter as tk
from PIL import ImageTk, Image
import urllib.request
 
root = tk.Tk()
imgURL = 'https://python-forum.io/images/python_fly.png'
img = ImageTk.PhotoImage(Image.open(urllib.request.urlopen(imgURL)))
panel = tk.Label(root, image = img)
panel.pack()
root.mainloop()