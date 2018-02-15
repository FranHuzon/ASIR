#-------------------- CREACIÓN LISTA --------------------#
palabras = input('Escribe la palabra que quieras añadir a la lista (Para terminar pulsa ENTER sin escribir nada): ')
lista_palabras = []

while palabras != '':
	lista_palabras.append(palabras)
	palabras = input('Escribe la palabra que quieras añadir a la lista (Para terminar pulsa ENTER sin escribir nada): ')
#-------------------- FIN CREACIÓN LISTA --------------------#

print ()

#-------------------- MENU --------------------#
print ('1. Contar.')
print ('2. Modificar.')
print ('3. Eliminar.')
print ('4. Salir.')

opcion = int(input('Elige una opción: '))

while opcion != 4:
#-------------------- DESARROLLO MENU --------------------#
#-------------------- DESARROLLO MENU: BUSCAR --------------------#
	if opcion == 1:
		palabra_buscar = input('¿Que palabra quiere buscar?: ')
		print ('La palabra {0} aparece {1} veces en la lista.'.format(palabra_buscar,lista_palabras.count(palabra_buscar)))
#-------------------- FIN DESARROLLO MENU: BUSCAR --------------------#
#-------------------- DESARROLLO MENU: MODIFICAR --------------------#
	elif opcion == 2:
		indice = 0
		palabra_sustituir = input('¿Que palabra quiere sustituir?: ')
		palabra_sustituta = input('¿Que palabra va a sustituir a la palabra {0}?: '.format(palabra_sustituir))
		for elem in lista_palabras:
			if elem == palabra_sustituir:
				lista_palabras[indice] = palabra_sustituta
			indice += 1
		print ('Lista actual {0}'.format(lista_palabras))
#-------------------- FIN DESARROLLO MENU: MODIFICAR --------------------#
#-------------------- DESARROLLO MENU: ELIMINAR --------------------#
	elif opcion == 3:
		palabra_eliminar = input('¿Que palabra quiere eliminar de la lista?: ')
		for elem in lista_palabras:
			if elem == palabra_eliminar:
				lista_palabras.remove(palabra_eliminar)
		print ('Lista actual {0}'.format(lista_palabras))
#-------------------- FIN DESARROLLO MENU: ELIMINAR --------------------#
	else:
		print ('Adios!!!!')
#-------------------- FIN DESARROLLO MENU --------------------#
	print ('1. Contar.')
	print ('2. Modificar.')
	print ('3. Eliminar.')
	print ('4. Salir.')
	opcion = int(input('Elige una opción: '))
#-------------------- FIN MENU --------------------#