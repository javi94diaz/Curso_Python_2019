# Juego del ahorcado en Python

import os

letra_jugador = '' # Variable global que contiene la letra que introducira el jugador en cada turno

class horca:	# Muestra la horca y las partes del cuerpo del ahorcado que aparecen con cada fallo
	
	def __init__(self):
		self.nfallos = 0	# Inicialmente no se han cometido fallos

	def add_cuerpo(self):	# Cuando se falle una letra, se suma una parte del cuerpo
		self.nfallos += 1

	def imprimir(self):		# Imprime la horca y las partes del cuerpo del ahorcado
		print(" .--.")
		print(" |  |")
		print(" {}  |".format('o' if self.nfallos >= 1 else ' '))
		print("{}{}{} |".format('/' if self.nfallos >= 2 else ' ', '|' if self.nfallos >=3 else ' ', '\\' if self.nfallos >= 4 else ' '))
		print(" {}  |".format('|' if self.nfallos >= 5 else ' '))
		print("{} {} |".format('/' if self.nfallos >= 6 else ' ','\\' if self.nfallos >= 7 else ' '))
		print("    |")
		print("    |")
		print(" _ _|_ _", end='\n\n')
		if self.nfallos >= 7:
			return 1

class panel:	# Muestra la palabra en curso, la lista de fallos y la lista de letras dichas

	def __init__(self, palabra_secreta):
		self.palabra_secreta = palabra_secreta
		self.letras_correctas = list(palabra_secreta)
		self.letras_falladas = []
		self.letras_dichas = []
		self.palabra_encurso = list('_'*len(palabra_secreta))
	
	def clasificar_letra(self, mi_horca):	#Todo esto de meter cosas en listas se puede hacer con enumerate()

		if letra_jugador not in self.letras_dichas:
			self.letras_dichas.append(letra_jugador)	# Todas las letras del jugador se guardan para anotar un fallo si repite letra
		else:
			mi_horca.add_cuerpo()
			print ("¡Letra repetida! ")
			return 0
		
		if letra_jugador in self.letras_correctas:				# LETRA CORRECTA: Se actualiza la palabra secreta para mostrarla despues
			for i in range(0, len(self.palabra_secreta), 1): 
				if letra_jugador == self.palabra_secreta[i]:
					self.palabra_encurso.insert(i,letra_jugador)
					del self.palabra_encurso[i+1]
		else:
			mi_horca.add_cuerpo()								# LETRA INCORRECTA: +1 fallo
			if letra_jugador not in self.letras_falladas:
				self.letras_falladas.append(letra_jugador)		# y se mete en la lista letras falladas para mostrarlas despues
		return 0	
		#Antigua forma de actualizar el panel
		"""for i in range(0, len(self.palabra_secreta), 1): # Aqui metemos la letra acertada en el panel si es correcta
									if letra_jugador in self.letras_correctas and letra_jugador == self.palabra_secreta[i]:
										self.palabra_encurso.insert(i,letra_jugador)
										del self.palabra_encurso[i+1]"""

	def ver_panel(self):	# Funcion que imprime el panel con la palabra que esta siendo adivinada y la lista de fallos
		
		#if letra_jugador in letras_correctas:

		print("Adivina: ", end = '')
		for i in range(0, len(self.palabra_encurso), 1):
			print("{} ".format(self.palabra_encurso[i]), end='')
		print('\n')
		print("Fallos: ", end='')
		for j in range(0, len(self.letras_falladas), 1):
			print("{}, ".format(self.letras_falladas[j]), end='')
		print('\n')	

# PROGRAMA PRINCIPAL

																#Instanciamos los objetos
mi_horca = horca() 
mi_panel = panel(input("Nueva palabra secreta: "))
final = 0 														#Variable para verificar condiciones de victoria o derrota


while True:
	#os.system('cls')
	if final == 1:
		print("GAME OVER")
		break
	final = mi_horca.imprimir()
	mi_panel.ver_panel()
	letra_jugador = input("Introduce una letra: ")
	mi_panel.clasificar_letra(mi_horca)
	if '_' not in mi_panel.palabra_encurso:
		print("PALABRA ADIVINADA: {}\nVICTORIA!".format(mi_panel.palabra_secreta))
		break
