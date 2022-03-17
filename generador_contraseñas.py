# Generador de contraseñas automatico
# Tenemos 4 listas con los tipos de caracteres que puede haber en la contraseña (minusculas, )
# Se pregunta al usuario cuales quiere, y se añaden los grupos elegidos a "total"
# Para generar la contraseña, primero se coge al azar uno de los grupos elegidos con la variable "cual_grupo".
# Una vez elegido el grupo, elegimos una posicion de ese grupo tambien al azar y añadimos el caracter de esa posicion a la contraseña
# El proceso se repite hasta crear una contraseña con tantos caracteres como el usuario haya pedido

import random
import string

#string.printable #El 10 es la 'a', el 35 es la 'z', el 36 es la 'A', el 61 es la 'Z'. Hay 26 letras minus y 26 mayus.

contraseña=""

char_especiales = list("&%@.ç<>$/*-")
minusculas = list(string.printable[10:36]) # letras a-z
mayusculas = list(string.printable[36:62]) # letras A-Z
numeros = list(string.printable[0:10]) # numeros 0-9

grupos_elegidos = 0 # Pueden ser hasta cuatro: las minusculas, las mayusculas, los numeros y los caracteres especiales
					# Cuando el usuario pida un caracter de este grupo, esta variable aumenta en uno para luego poder elegir al azar
					# de que grupo será el siguiente caracter de la contraseña generada

total=[] # Lista que almacena los grupos de caracteres elegidos por el usuario
nombres_grupos = ['minusculas', 'mayusculas', 'numeros', 'caracteres especiales']	# Para hacer las preguntas al usuario con un bucle

print(" *** GENERADOR AUTOMATICO DE CONTRASEÑAS *** ")

longitud = int(input(" Introduzca longitud de la contraseña: "))

# Consultamos al usuario que tipos de caracteres quiere en su contraseña con un bucle, porque son cuatro preguntas muy similares
for i in range (0, 4):
	if ('s' == input(" ¿Desea incluir {}? (s/n): ".format(nombres_grupos[i])) ):
		if i == 0:
			total.append(minusculas)
			grupos_elegidos+=1
		elif i == 1:
			total.append(mayusculas)
			grupos_elegidos+=1
		elif i == 2:
			total.append(numeros)
			grupos_elegidos+=1
		elif i == 3:
			total.append(char_especiales)
			grupos_elegidos+=1


if grupos_elegidos != 0:
	while len(contraseña) < longitud:
	
		cual_grupo = random.randint(0, grupos_elegidos-1)
		#print(cual_grupo)
		#print(total[cual_grupo])
		posicion =  random.randint(0, len(total[cual_grupo])-1 ) 
		#print("posicion: " + str(posicion))
		#print( total[cual_grupo][posicion])
		contraseña += str( total[cual_grupo][posicion] )

	print("Clave generada: "+ contraseña)
else:
	print("\n Contraseña vacia")
