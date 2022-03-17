#Vamos a imprimir una lista en una interfaz

from tkinter import *
from tkinter import ttk

def saca_por_ventana(un_cuadrado):
	col = 0
	fila = 0
	
	for i in range(0,4):
		for j in range (0,4):
			etiq = Label(aplic, text = str(un_cuadrado[i][j]).zfill(3))
			etiq.grid(row = fila, column = col)	# Creamos una rejilla para imprimir los numeros por filas.
			col += 1
			if col >= 4:
				col = 0
				fila += 1

# PROGRAMA PRINCIPAL

unafila = [] #variable auxiliar para crear el cuadrado ordenado
mi_cuadrado = [] # este es el cuadrado, primero ordenado, luego magico
nums_diagonal = []

aplic = Tk()

aplic.title('Cuadrados mágicos')
aplic.configure(bg = "LightBlue2")
aplic.geometry('300x200')

# Crear cuadrado ordenado como matriz 4x4 (lista de listas)
for i in range (1, 17):
	unafila.append(i)
	if i%4 == 0:
		mi_cuadrado.append(unafila)
		unafila= []

saca_por_ventana(mi_cuadrado)

ttk.Label(aplic, text = '\n')

# Sacamos los numeros de las diagonales principal y secundaria
for i in range (0,4):
	for j in range(0,4):
		if i==j or i+j == 3:
			nums_diagonal.append(mi_cuadrado[i][j])

# Reordenamos esos numeros en orden decreciente y los devolvemos a las posiciones diagonales
nums_diagonal.reverse()
posicion = 0

#Devolvemos los numeros extraidos, en orden decreciente, a las posiciones diagonales anteriormente detectadas
for i in range(0,4):
	for j in range (0,4):
		if i==j or i+j == 3:
			mi_cuadrado[i][j] = nums_diagonal[posicion]
			posicion += 1

saca_por_ventana(mi_cuadrado)

aplic.mainloop()