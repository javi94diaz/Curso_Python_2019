# letras grandes de prueba para imprimir GAMEOVER (para incluirlo ene la ahorcado)

g=["****","*   ", "* **", "*  *", "****"]
a=["****","*  *", "*  *", "****", "*  *"]
m=["*   *","** **", "* * *", "*   *", "*   *"]
e=["****","*   ", "*** ", "*   ", "****"]

o=["****","*  *", "*  *", "*  *", "****"]
v=["*   *","*   *", "*   *", " * * ", "  *  "]
r=["****","*  *", "*** ", "*  *", "*   *"]

gameover = [g,a,m,e,o,v,e,r]

for i in range(0,len(gameover)):
	for j in range(0,len(gameover[i])):
		print(len(gameover[i]))
		#print(gameover[j][i], end = ' ')
	print(i,j)