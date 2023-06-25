# Ventana que utiliza el widget Message (con formato) en lugar de una etiqueta de texto

import tkinter as tk

root = tk.Tk()
texto = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

msg = tk.Message(root, text = texto)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

tk.mainloop()