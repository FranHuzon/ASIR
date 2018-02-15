#-------------------- CREACION LISTA --------------------#
palabras = input('Escribe la palabra que quieras añadir a la primera lista (Para terminar pulsa ENTER sin escribir nada): ')
lista_palabras = []

while palabras != '':
	lista_palabras.append(palabras)
	palabras = input('Escribe la palabra que quieras añadir a la primera lista (Para terminar pulsa ENTER sin escribir nada): ')

print ()
print ('Primera lista: {0}'.format(lista_palabras))
print ()
#-------------------- FIN CREACION LISTA --------------------#

#-------------------- CREACION LISTA 2 --------------------#
palabras_2 = input('Escribe la palabra que quieras añadir a la segunda lista (Para terminar pulsa ENTER sin escribir nada): ')
lista_palabras_2 = []

while palabras_2 != '':
	lista_palabras_2.append(palabras_2)
	palabras_2 = input('Escribe la palabra que quieras añadir a la segunda lista (Para terminar pulsa ENTER sin escribir nada): ')

print ()
print ('Segunda lista: {0}'.format(lista_palabras_2))
print ()
#-------------------- FIN CREACION LISTA 2 --------------------#

#-------------------- ELIMINAR PALABRAS REPETIDAS -------------------#
lista_palabras_3 = []
lista_palabras_4 = []

for elem in lista_palabras:
	if not elem in lista_palabras_3:
		lista_palabras_3.append(elem)
		lista_palabras = lista_palabras_3[:]

for elem in lista_palabras_2:
	if not elem in lista_palabras_4:
		lista_palabras_4.append(elem)
		lista_palabras_2 = lista_palabras_4[:]
#-------------------- FIN ELIMINAR PALABRAS REPETIDAS --------------------#

#-------------------- PALABRAS EN LAS 2 LISTAS --------------------#
palabras_en_ambas_listas = []

for elem in lista_palabras:
	if elem in lista_palabras_2:
		palabras_en_ambas_listas.append(elem)
#-------------------- FIN PALABRAS EN LAS 2 LISTAS --------------------#

#-------------------- PALABRAS SOLO EN LISTA 1 --------------------#
palabras_solo_en_la_primera_lista = []

for elem_1 in lista_palabras:
	if elem_1 not in lista_palabras_2:
		palabras_solo_en_la_primera_lista.append(elem_1)
#-------------------- FIN PALABRAS SOLO EN LISTA 1 --------------------#

#-------------------- PALABRAS SOLO EN LISTA 2 --------------------#
palabras_solo_en_la_segunda_lista = []

for elem_2 in lista_palabras_2:
	if elem_2 not in lista_palabras:
		palabras_solo_en_la_segunda_lista.append(elem_2)
#-------------------- FIN PALABRAS SOLO EN LISTA 2 --------------------#

#-------------------- TODAS LAS PALABRAS --------------------#
todas_las_palabras = []

for elem_1,elem_2 in zip(lista_palabras,lista_palabras_2):
	if elem_1 not in todas_las_palabras:
		todas_las_palabras.append(elem_1)
	if elem_2 not in todas_las_palabras:
		todas_las_palabras.append(elem_2)
#-------------------- FIN TODAS LAS PALABRAS --------------------#

print ('Palabras que aparecen en ambas listas: {0}'.format(palabras_en_ambas_listas))
print ('Palabras que solo aparecen en la primera lista: {0}'.format(palabras_solo_en_la_primera_lista))
print ('Palabras que solo aparecen en la segunda lista: {0}'.format(palabras_solo_en_la_segunda_lista))
print ('Todas las palabras: {0}'.format(todas_las_palabras))