#-------------------- CREACION LISTA --------------------#
lista_palabras = []
#-------------------- FIN CRECION LISTA --------------------#
#-------------------- AÑADIR PALABRAS --------------------#
palabras = input('Indica la palabra que quieres añadir: ')
while palabras != '*':
	lista_palabras.append(palabras)
	palabras = input('Indica la palabra que quieres añadir: ')
#-------------------- FIN AÑADIR PALABRAS --------------------#
#-------------------- ORDENAR ALFABETICAMENTE --------------------#
lista_palabras.sort()
print ('Lista ordenada alfabeticamente: {}'.format(lista_palabras))
#-------------------- FIN ORDENAR ALFABETICAMENTE --------------------#
#-------------------- MAS DE 5 CARACTERES --------------------#
mas_de_5_caracteres = []
for elem in lista_palabras:
	if elem not in mas_de_5_caracteres and len(elem) > 5:
		mas_de_5_caracteres.append(elem)
if len(mas_de_5_caracteres) >= 1:
	print ('Las palabras con más de 5 caracteres son: {}'.format(mas_de_5_caracteres))
#-------------------- FIN MAS DE 5 CARACTERES --------------------#
#-------------------- EMPIEZAN POR VOCAL --------------------#
empieza_por_vocal = []
for elem in lista_palabras:
	if elem[0] == 'a' or elem[0] == 'e' or elem[0] == 'i' or elem[0] == 'o' or elem[0] == 'u':
		empieza_por_vocal.append(elem)
if len(empieza_por_vocal) >= 1:
	print ('Se han introducido {} cadenas que empiezan por vocal.'.format(len(empieza_por_vocal)))
#-------------------- FIN EMPIEZAN POR VOCAL --------------------#
#-------------------- CADENA CON ESPACIO --------------------#
cadena_con_espacio = False 
for elem in lista_palabras:
	if elem.count(' '):
		cadena_con_espacio = True
	
if cadena_con_espacio:
	print ('Se ha introducido una cadena con espacio.')
#-------------------- FIN CADENA CON ESPACIO --------------------#
#-------------------- SIMILITUD CADENA --------------------#
cadena_similitud = input('Indica una cadena: ')
similitudes = []
for elem in lista_palabras:
	if elem.startswith(cadena_similitud):
		similitudes.append(elem)
if len(similitudes) >= 1:
	print ('Las cadenas que empiezan por la cadena {0} son: {1}'.format(cadena_similitud,similitudes))
#-------------------- FIN SIMILITUD CADENA --------------------#
