#Generador de triangulos vacios

# el usuario nos da el numero de filas del triangulo vacio: n
# nosotros le restamos dos, ya que usamos n-2 para construir el triangulo de huecos interiores
# ese dos viene de la primera y ultima filas, que las añadimos nosotros para completar el triangulo de la altura pedida
# En la instruccion print(' '*(2*fila_actual-1), end='*\n') el caracter ' ' que imprimimos es un hueco interior. Se puede cambiar por
# cualquier otro caracter para ver mejor el triangulo interior (por ejemplo una letra 'a'): print('a'*(2*fila_actual-1), end='*\n')

n = int(input("Introduzca el numero de filas: \n")) - 2

print(' '*(n+1), end='')	# Creamos la primera fila
print('*')

for fila_actual in range(1, n+1, 1):				# Este bucle se encarga de generar el triangulo de huecos interiores				
	print(' '*(n+1-fila_actual), end ='*')  		# Y tambien añade un asterisco antes...
	
	print(' '*(2*fila_actual-1), end='*\n')			# ...y despues de cada fila de huecos

	if fila_actual == n:							# Finalmente creamos la ultima fila llena de asteriscos
		print('*'*(2*(fila_actual+2)-1), end='')