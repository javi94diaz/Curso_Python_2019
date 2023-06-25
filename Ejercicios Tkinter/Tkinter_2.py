# Ventana con una etiqueta de texto

import tkinter as tk
root = tk.Tk()
w = tk.Label(root, text="Hello Tkinter!")
w.pack() 			# The pack method tells Tk to fit the size of the window to the given text.

root.mainloop()		# The window won't appear until we enter the Tkinter event loop "mainloop"
 					# Our script will remain in the event loop until we close the window.