# Cuadrados magicos base 4x4
# Sus filas, columnas y diagonales suman la misma cantidad
# Se crean a partir de un cuadrado con los numeros ordenados, e invirtiendo sus diagonales principal y secundaria.
# El algoritmo consiste en extraer todos los numeros que estan en una diagonal principal o secundaria y meterlos en una lista
# Despues esa lista la colocamos en orden decreciente y devolvemos los numeros a las posiciones diagonales de las que fueron extraidos,
# pero a la inversa. De esa manera conseguimos dar la vuelta a ambas diagonales y conseguir la propiedad de un cuadrado magico.

# Para mas informacion, consultar  http://www.ehu.eus/~mtpalezp/descargas/magiacuadrada.pdf



def imprime_cuadrado(un_cuadrado):
	# Imprimimos el cuadrado ordenado
	for i in range (0,4):
		for j in range(0,4):
			print(str(un_cuadrado[i][j]).zfill(3), end=' ')	# zfill da el formato con ceros a la izquierda hasta tener tantas cifras como se le indique
			if j == 3:
				print('\n', end = '')
	print('\n', end = '')

mi_cuadrado = []
fila = []
nums_diagonal = []

# Generamos un cuadrado base ordenado
for i in range (1, 17):
	fila.append(i)
	if i%4 == 0:
		mi_cuadrado.append(fila)
		fila= []

print("Cuadrado ordenado:")
imprime_cuadrado(mi_cuadrado)

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

print("Cuadrado magico:")
imprime_cuadrado(mi_cuadrado)