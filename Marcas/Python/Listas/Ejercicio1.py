#-------------------- CREACIÓN LISTA --------------------#
numeros = int(input('Indica el valor que tendrá el número: '))
lista_numeros = []

while numeros != 0:
	lista_numeros.append(numeros)
	numeros = int(input('Indica el valor que tendra el número: '))
#-------------------- FIN CREACIÓN LISTA --------------------#

print ('Se han añadido {0} números a la lista.'.format(len(lista_numeros)))
print ('El número más grande que se ha añadido en la lista es {0}.'.format(max(lista_numeros)))

lista_numeros.sort()

print ('Lista ordenada de menor a mayor: {0}'.format(lista_numeros))
print ('La media de los números añadidos a las lista es {0}'.format(round(sum(lista_numeros) / len(lista_numeros),2)))
