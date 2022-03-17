# Calculadora con Tkinter

# Pantalla "LCD" donde escribir y mostrar resultados
# Matriz de 9 botones del 1 al 9
# Debajo tres botones mas: el 0, el punto '.' y el igual '='
# A la derecha, en una columna de 4, los simbolos +, -, x, % de arriba abajo

import tkinter as tk

root = tk.Tk()
root.title('Calculadora')
root.geometry('300x200')

entrada = [] 				# Lista que almacena la secuencia de teclas que pulsa el usuario para poder interpretarla despues 
iconos_operaciones = ['+','-','x','%']		# Lista con los simbolos matematicos principales en formato de caracteres
iconos_numeros = ['0','1','2','3','4','5','6','7','8','9'] # Lista con los numeros del 0 al 9 para poner en las teclas de la calculadora como caracteres
resultado = 0

def calcularResultado():
	primernum = int(entrada[0])
	print(primernum) #esta linea se podra quitar
	segundonum = 0
	
	i = 1
	while entrada[i].isdigit() :							# Construimos el primer numero con las cifras que haya en la lista entrada hasta toparnos con un simbolo de operacion
		print (entrada[i])
		primernum = primernum*10 + int(entrada[i])
		i += 1

	operacion = entrada[i]	# Guardamos el simbolo de operacion
	i += 1
	
	print(operacion)				#esta linea se podra quitar
	print("Ahora i = " + str(i))

	while entrada[i].isdigit() :							# Construimos el segundo numero de la misma forma
		segundonum = segundonum*10 + int(entrada[i])
		if i < len(entrada) - 1:
			i += 1
		else:
			break	

	if operacion == '+':					 # Teniendo ya ambos numeros interpretamos que operacion desea el usuario y la hacemos
		resultado = primernum + segundonum
	elif operacion == '-':
		resultado = primernum - segundonum
	elif operacion == '*':
		resultado = primernum * segundonum
	elif operacion == '/' and segundonum != 0: 
		resultado = primernum/segundonum

	pantalla.configure(text = str(resultado)) # Volcamos el resultado en la pantalla
	print(resultado) #esta linea se podra quitar

def setnumero(simbolo):			# Funcion que añade todos los simbolos que el usuario pulsa a una lista
	numero = 0
	salida = ''
	
	if simbolo == '=':			# Si el simbolo pulsado es un '=', pasamos a interpretar la lista de comandos y calcular el resultado
		calcularResultado()
		return 0 				# Volvemos al programa principal devolviendo un cero que nadie recoge.

	entrada.append(simbolo)		# Si no era un '=', metemos el simbolo en la lista
	
	for elem in range (0, len(entrada) ):
		salida += str(entrada[elem])
		pantalla.configure(text = salida)		# Y volcamos esa lista en la etiqueta "pantalla" que se mostrara en la calculadora "en tiempo real"
	
	print(entrada) # Esto luego se podra quitar

def borrarpantalla():
	pantalla.configure(text = '')
	entrada.clear()
	resultado = 0


pantalla = tk.Label(root, text = '', height=1, width = 15)
pantalla.grid(row = 0, column = 0)
pantalla.configure(background = "LightBlue2")

framebotones = tk.Frame(root)
framebotones.grid(row=1, column= 0)

# FORMA CHUSCA
boton0 = tk.Button(framebotones, text = iconos_numeros[0], command = lambda: setnumero('0'))
boton0.grid(row = 4, column = 1)
boton1 = tk.Button(framebotones, text = iconos_numeros[1], command = lambda: setnumero('1'))
boton1.grid(row = 3, column = 0)
boton2 = tk.Button(framebotones, text = iconos_numeros[2], command = lambda: setnumero('2'))
boton2.grid(row = 3, column = 1)
boton3 = tk.Button(framebotones, text = iconos_numeros[3], command = lambda: setnumero('3'))
boton3.grid(row = 3, column = 2)
boton4 = tk.Button(framebotones, text = iconos_numeros[4], command = lambda: setnumero('4'))
boton4.grid(row = 2, column = 0)
boton5 = tk.Button(framebotones, text = iconos_numeros[5], command = lambda: setnumero('5'))
boton5.grid(row = 2, column = 1)
boton6 = tk.Button(framebotones, text = iconos_numeros[6], command = lambda: setnumero('6'))
boton6.grid(row = 2, column = 2)
boton7 = tk.Button(framebotones, text = iconos_numeros[7], command = lambda: setnumero('7'))
boton7.grid(row = 1, column = 0)
boton8 = tk.Button(framebotones, text = iconos_numeros[8], command = lambda: setnumero('8'))
boton8.grid(row = 1, column = 1)
boton9 = tk.Button(framebotones, text = iconos_numeros[9], command = lambda: setnumero('9'))
boton9.grid(row = 1, column = 2)

botonborrar =  tk.Button(framebotones, text = 'AC ', command = lambda: borrarpantalla())
botonborrar.grid(row = 1, column = 3)

botonsuma = tk.Button(framebotones, text = '+', command = lambda: setnumero('+'))
botonsuma.grid(row = 2, column = 3)

botonresta = tk.Button(framebotones, text = '-', command = lambda: setnumero('-'))
botonresta.grid(row = 3, column = 3)

botonmultiplicacion = tk.Button(framebotones, text = 'x', command = lambda: setnumero('*'))
botonmultiplicacion.grid(row = 2, column = 4)

botondivision = tk.Button(framebotones, text = '/', command = lambda: setnumero('/'))
botondivision.grid(row = 3, column = 4)

botonigual = tk.Button(framebotones, text = '=', command = lambda: setnumero('='))
botonigual.grid(row = 4, column = 3)

root.mainloop()


"""
# FORMA BIEN DE CREAR BOTONES CON BUCLE PERO NO CONSIGO QUE CADA UNO PASE UN PARAMETRO CUANDO SE PULSE. ******** SE HACE USANDO partial PARA LLAMAR A LA FUNCION COMPLETA EN VEZ DE A UNA SOLA PARTE
fila = 2
col = 0

for i in range(1,10): # Del 1 al 9
	
	boton = tk.Button(root, text = numeros[i-1], command = lambda: setnumero(i))
	boton.grid(row = fila, column = col)
	col +=1
	if col == 3:
		col = 0
		fila -= 1
"""



# nota: ¿se le podrá pasar como parametro al command esto?: self.text (para que le pase el titulin del boton sin complicarnos mas)