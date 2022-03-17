# Programa para multiplicar matrices


def crearMatriz (orden):
	fila = []
	A = []

	for i in range (0, orden):
		fila.append(i)
		#print("Esta es la fila actualmente" + str(fila))
		A.append(fila)
		#print(A)
	print(A)

	return (A)

def multiplica(A,B):
	
	operaciones = len(A)*len(B)
	print(operaciones)

	res = []

	for i in range (0, operaciones):
		res[i]


#A = crearMatriz(3)
#B = crearMatriz(3)
#multiplica(A,B)

def badmatrix(n,m):
 a = [0]*m
 matriz = [a]*n
 return matriz

def creaMatrizDato(n,m, dato):
	'''
	Esta función crea una matríz con n filas y n columnas.
	Cada celda contiene el valor "dato"
	@param n : Número de filas.
	@param m : Número de columnas
	@param dato: Un valor
	@type n: entero
	@type m: entero
	@type dato: tipo simple
	@return: devuelve una matriz n por m
	@rtype: matriz (lista de listas)
	'''
	matriz = []
	for i in range(n):
		a = [dato]*m
		matriz.append(a)
	return(matriz)

M = badmatrix(2,2)
print(M)

Q = creaMatrizDato(3,3,9)
print(Q)
