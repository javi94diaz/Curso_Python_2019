# Boton que muestra un magikarp normal o uno shiny al azar

import tkinter as tk
import random

root = tk.Tk()

root.geometry('300x120')											# Dar tamaño, color y titulo a la ventana
root.configure(background = "Light blue")
root.title("Magikarp.exe")

imagen_normal = tk.PhotoImage(file="regular_magikarp.png") 			# Creamos los objetos imagenes para mostrarlas despues
imagen_shiny = tk.PhotoImage(file="shiny_magikarp.png")
imagen_interr = tk.PhotoImage(file="mi_interrogacion.png")

etiq_intro = tk.Label(root, text = "Descubre si tu Magikarp es shiny") 	# Frase de introduccion
etiq_intro.pack(side = 'top')

etiq_imagen = tk.Label(root, image = imagen_interr ) 				# Etiqueta con una imagen de una '?' donde luego ira magikarp
etiq_imagen.pack(side = 'top')

texto_prob = str(0)
etiq_prob = tk.Label(root, text = texto_prob )
etiq_prob.pack(side = 'left')

def vershiny():
	
	#etiq_intro.config(text = "Cambiado")
	probabilidad = random.randint(0,10)
	if probabilidad == 0:
		etiq_imagen.config(image=imagen_shiny)
	else:
		etiq_imagen.config(image=imagen_normal)
	
	texto_prob = str(probabilidad)
	etiq_prob.config(text = texto_prob)


boton = tk.Button(root, text="Quiero mi carpa dorada!", command = vershiny)	# Boton que al pulsarlo pone la imagen de magikarp normal o shiny
boton.pack(side='bottom')

root.mainloop()

"""
# Codigo que ahora vuelvo a meter

image=imagen_interr

image=imagen_shiny

image=imagen_normal

"""