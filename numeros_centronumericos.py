# Programa que encuentra los n primeros numeros centronumericos.
# Numeros centronumericos: aquellos numeros que cumplen que la suma de sus anteriores da lo mismo que la suma de unos cuantos superiores al numero centronumerico.
# El primero es el 6, el siguiente es el 35

# 1+2+3+4+5 = 15				Numero: 6			7+8 = 15
# 1+2+3+...+34 = 595			Numero: 35			36+37+...+49 = 595
# 1+2+...+203 = 20706			Numero: 204			205+206+...+288 = 20706
# 1+2+...+1188 = 706266			Numero: 1189		1190+1191+...+1681 = 706266
# 1+2+...+6929 = 24008985		Numero: 6930		6931+6932+...+9800 = 24008985
# 1+2+...+40390 = 815696245 	Numero: 40391		40392+40393+...+ 57121= 815696245

cuantos = int(input("Introduce cuantos numeros centronumericos quieres saber: "))
cont = 0 # contador que marca cuantos numeros centronumericos hemos encontrado en cada iteracion
num = 1  # num son todos los numeros naturales (empezando por el 1), que se evaluan en orden creciente para ver si son centronumericos o no

while cont < cuantos:
	suma_anteriores = 0
	for i in range (1, num):
		suma_anteriores += i
	#print (suma_anteriores)
	#print("La suma de los anteriores es " + str(suma_anteriores))
	suma_izq = suma_anteriores
	k = 1
	while suma_anteriores > 0:
		suma_anteriores -= num+k
		k += 1
		if suma_anteriores == 0:
			print ("El {} es un numero centronumerico".format(num))
			print("\tLa suma de los anteriores es " + str(suma_izq))
			cont +=1
	num +=1