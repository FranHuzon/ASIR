from Funciones import convertir_a_segundos, calcular_coste, convertir_a_euros

tarifa = int(input('Coste por segundo (Centimos): '))

llamadas = int(input('Indica el número de llamadas realizadas: '))

llamadas_duracion = []

total_segundos = 0

indice = 1

for elem in range(llamadas):
	lista = []
	print ('Indica la duración de la llamada {}.'.format(indice))
	duracion_horas = int(input('Horas: '))
	duracion_minutos = int(input('Minutos: '))
	duracion_segundos = int(input('Segundos: '))
	lista.append(indice)
	lista.append(convertir_a_segundos(duracion_horas,duracion_minutos,duracion_segundos))
	llamadas_duracion.append(lista)
	lista = []
	indice += 1

for elem in llamadas_duracion:
	total_segundos += elem[1]

for elem in llamadas_duracion:
	print ('El coste de la llamada {0} es {1} €.'.format(elem[0],convertir_a_euros(int(calcular_coste(elem[1], tarifa)))))

print ('El coste total de las llamadas es {} €.'.format(convertir_a_euros(calcular_coste(total_segundos,tarifa))))