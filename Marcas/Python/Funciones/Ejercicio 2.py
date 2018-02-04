from Funciones import convertir_a_segundos, calcular_coste ,convertir_a_euros

fichero = open("F:\ASIR o ASAR\Marcas\Funciones\Factura.txt", "r")
lista = fichero.readlines()
fichero.close()

tarifa = 0
lista_2 = []
duracion_llamadas = []
duracion_llamadas_segundos = []
total_segundos = 0
indice = 1

for elem in lista:
	lista_2.append(elem.replace('\n', ''))

for elem in lista_2[0]:
	centimos = 0
	if elem.isdigit():
		centimos += int(elem)
	lista_2[0] = centimos
	tarifa = centimos

for elem in lista_2[1::]:
	lista_3 = []
	horas,minutos,segundos = elem.split(':')
	lista_3.append(int(horas))
	lista_3.append(int(minutos))
	lista_3.append(int(segundos))
	duracion_llamadas.append(lista_3)

for elem in duracion_llamadas:
	duracion = 0
	duracion += convertir_a_segundos(elem[0], elem[1], elem[2])
	duracion_llamadas_segundos.append(duracion)
	total_segundos += duracion

for elem in duracion_llamadas_segundos:
	print ('El coste de la llamada {0} es {1} €.'.format(indice, convertir_a_euros(calcular_coste(elem, tarifa))))
	indice += 1
print ('El coste total de las llamadas es {0} €.'.format(convertir_a_euros(calcular_coste(total_segundos, tarifa))))