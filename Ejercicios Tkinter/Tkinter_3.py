# Ventana con una imagen local a la derecha y una etiqueta de texto con algo de formato

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="image.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vivamus iaculis diam a imperdiet faucibus.
Aliquam varius lectus non urna maximus, sit amet sodales ipsum pretium."""


# The "justify" parameter can be used to justify a text on the LEFT, RIGHT or CENTER.
# padx can be used to add additional horizontal padding around a text label.
# The default padding is 1 pixel. pady is similar for vertical padding. 

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 25, 
              text=explanation).pack(side="left")


root.mainloop()