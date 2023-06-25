#Generador de triangulos rellenos

# el usuario nos da el numero de filas: n
# el numero de espacios antes de los asteriscos es de n-1
# el numero de asteriscos 2n-1 (si n empieza en 1) ó 2n+1 (si n empieza en 0)

#Version con el contador del bucle empezando en 1 (numero de asteriscos = 2n-1)

n = int(input("Introduzca el numero de filas: "))

for fila_actual in range(1, n+1, 1):		
	print(' '*(n-fila_actual), end ='')				
	print('*'*(2*fila_actual-1))

#Version con el contador del bucle empezando en 0 (numero de asteriscos = 2n+1)

n = int(input("Introduzca el numero de filas: "))

for fila_actual in range(0, n, 1):						
	print(' '*(n-fila_actual), end ='')				
	print('*'*(2*fila_actual+1))