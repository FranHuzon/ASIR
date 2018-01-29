#-------------------- CREACION CADENAS --------------------#
poblacion_temp_max_temp_min = '''
Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
'''
#-------------------- FIN CREACION CADENAS --------------------#

#-------------------- CREACION LISTAS --------------------#
lista_poblacion_temp_max_temp_min = poblacion_temp_max_temp_min.splitlines()
lista_poblacion_temp_max_temp_min.pop(0)
lista_2_poblacion_temp_max_temp_min = []

for elem in lista_poblacion_temp_max_temp_min:
	lista_2_poblacion_temp_max_temp_min.append(elem.split(","))

#-------------------- CONVERTIR DIGITOS A ENTEROS --------------------#
for elem in lista_2_poblacion_temp_max_temp_min:
	if elem[1].isdigit():
		elem[1] = int(elem[1])
	if elem[2].isdigit():
		elem[2] = int(elem[2])
#-------------------- FIN CONVERTIR DIGITOS A ENTEROS --------------------#

#-------------------- TEMPERATURA MEDIA --------------------#
for elem in lista_2_poblacion_temp_max_temp_min:
	print ('La temperatura media de {0} es {1} ºC.'.format(elem[0],(elem[1] + elem[2]) / 2))
#-------------------- FIN TEMPERATURA MEDIA --------------------#

#-------------------- CONSULTA TEMPERATURA-CIUDAD --------------------#
consulta_temperatura = input('¿De que ciudad quieres saber su temperatura?: ')
#-------------------- ERROR CONSULTA --------------------#
error = 0

for elem in lista_2_poblacion_temp_max_temp_min:
	if elem[0] != consulta_temperatura:
		error += 1

if error == 4:
	print ('ERROR')
#-------------------- FIN ERROR CONSULTA --------------------#
for elem in lista_2_poblacion_temp_max_temp_min:
	if elem[0] == consulta_temperatura:
		print ('Las temperaturas máxima y mínima de {0} son {1} y {2}'.format(elem[0],elem[1],elem[2]))
#-------------------- FIN CONSULTA TEMPERATURA-CIUDAD --------------------#