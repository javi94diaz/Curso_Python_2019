# Cuadrados magicos 4k
# Se pide al usuario una k, y se crea un cuadrado ordenado de dimension 4k x 4k
# Despues extraemos los elementos diagonales (de todas las diagonales tanto principales
# como secundarias). A continuacion los ordenamos de mayor a menor, y los devolvemos por filas
# a esas posiciones diagonales.
# ¿Como sabemos si una posicion del cuadrado pertenece a alguna diagonal?
# El cuadrado grande que generemos, estara dividido en k cuadrados base, cada uno de dimension 4x4
# Le hemos dado unas coordenadas (fila_base, col_base) a cada uno de estos cuadrados base. De esta manera
# podemos recorrer el cuadrado grande entrando en cada cuadrado base, y una vez dentro recorrer ese cuadrado
# base con i,j para analizar sus elementos. Las filas de un cuadrado base pueden ser de dos tipos:
# Tipo 0 o 3, y Tipo 1 o 2 (las filas primera y ultima, o las dos de en medio). Esto significa que esa fila contiene elementos diagonales en las posiciones 0 y 3, 
# o en las posiciones 1 y 2. Estos numeros 0,1,2,3 son relativos al cuadrado base donde estemos. Su posicion absoluta
# en el cuadrado grande seran de la forma (0+4*fila_base , 0+4*col_base).
# Por lo tanto, si la fila en la que estamos es de tipo 0 o 3 (Lineas 53 y 70 de codigo), cogeremos como elementos diagonales el de la posicion 0 y el de la posicion 3 (los extremos)
# Sino, la fila es de tipo 1 o 2, cogeremos como elementos diagonales los centrales, los de posicion 1 y 2.
# Este sistem, que localiza las posiciones que nos interesa, lo utilizamos para recoger los elementos al principio, y para depositarlos en orden inverso despues.
# Por ultimo mostramos el cuadrado ya reordenado, que cumple la propiedad de magico.


def crear_cuadrado(dim):	# Funcion que genera un cuadrado ordenado como una lista de listas.
	mi_cuadrado = []
	fila = []

	for i in range (1, dim*dim+1):
		fila.append(i)
		if i%dim == 0:
			mi_cuadrado.append(fila)
			fila = []
	return mi_cuadrado	

def imprime_cuad (un_cuadrado, dim):	#Funcion que saca por pantalla cualquier cuadrado que sea una lista de listas, este ordenado o no.
	for i in range (0, dim):
		for j in range(0, dim):
			print( str( un_cuadrado[i][j] ).zfill(3), end=' ' ) # zfill rellena con tantos ceros a la izquierda como se indique, para que esten alineados
		if j == dim-1:
			print('\n', end= '') # Imprimimos un salto de linea, con end ='' para no imprimir dos saltos.
	print('\n', end= '') # Al final del cuadrado imprimimos otro salto de linea		

def dale_magia(un_cuadrado, dim, k): # Funcion que invierte todos los elementos de las diagonales ppales y secundarias del cuadrado para hacerlo magico
	
	#fila_base = 0 # Variables que indican las coordenadas de cada cuadrado de 4x4 (cuadrado base) en el cuadrado grande.
	#col_base = 0 # Por ejemplo, el primer cuadrado es el 00, el que tiene a la derecha el 01, y el q esta debajo del 01, es el 11. (una matriz de cuadrados)
	# Estas dos variables van de 0 a k-1. Por ejemplo en el cuadrado de 8x8 van de 0 a 1 ambas
	nums_diagonal = []
	
	# Ahora sacamos los elementos diagonales de cada cuadrado y los añadimos a una unica lista para todo el cuadrado grande
	for fila_base in range(0, k): # de 0 a k-1
		for col_base in range(0, k): # de 0 a k-1

			for i in range (0 + 4*fila_base, 4 + 4*fila_base):		# Los bucles en i y j recorren cada fila de cada cuadrado base para extraer sus elementos diagonales
				for j in range (0 + 4*col_base, 4 + 4*col_base):

					if (i-4*fila_base == 0 or i-4*fila_base == 3) and (j-4*col_base == 0 or j-4*col_base == 3):
						nums_diagonal.append(un_cuadrado[i][j])
					elif (i-4*fila_base == 1 or i-4*fila_base == 2) and (j-4*col_base == 1 or j-4*col_base == 2):
						nums_diagonal.append(un_cuadrado[i][j])

	#print(nums_diagonal)				 
	nums_diagonal.reverse()
	posicion = 0
	#print(nums_diagonal)

	# Dejamos los elementos en orden inverso
	for fila_base in range(0, k): # de 0 a k-1
		for col_base in range(0, k): # de 0 a k-1

			for i in range (0 + 4*fila_base, 4 + 4*fila_base):		# Los bucles en i y j recorren cada fila de cada cuadrado base para extraer sus elementos diagonales
				for j in range (0 + 4*col_base, 4 + 4*col_base):
				
					if (i-4*fila_base == 0 or i-4*fila_base == 3) and (j-4*col_base == 0 or j-4*col_base == 3):
						un_cuadrado[i][j] = nums_diagonal[posicion]
						posicion +=1
					elif (i-4*fila_base == 1 or i-4*fila_base == 2) and (j-4*col_base == 1 or j-4*col_base == 2):
						un_cuadrado[i][j] = nums_diagonal[posicion]
						posicion +=1

	return un_cuadrado

# PROGRAMA PRINCIPAL

cuadrado_magico = []
print("Cuadrados magicos 4K")
k = int(input("Introduzca una k: "))
dim = 4*k
cuadrado = crear_cuadrado(dim)
imprime_cuad(cuadrado, dim)
dale_magia(cuadrado, dim, k)
imprime_cuad(cuadrado, dim)
