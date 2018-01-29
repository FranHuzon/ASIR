#-------------------- INTRODUCIR DATOS --------------------#
fecha = input('Fecha: ')
#-------------------- FIN INTRODUCIR DATOS --------------------#
#-------------------- CREAR VARIABLES --------------------#
lista_fecha = fecha.split("/")
dia = int(lista_fecha[0])
mes = int(lista_fecha[1])
año = int(lista_fecha[2])
lista_dias = [31,28,31,30,31,30,31,31,30,31,30,31]
bisiesto = False
dia_juliano = 0
#-------------------- FIN CREAR VARIABLES --------------------#
#-------------------- AÑO BISIESTO --------------------#
if año % 4 == 0:
	if año % 100 == 0:
		if año % 400 == 0:
			bisiesto = True
if bisiesto == False and dia == 29 and mes == 2 or dia > 31 or mes > 12:
	print ('Fecha incorrecta.')
#-------------------- FIN AÑO BISIESTO --------------------#
#-------------------- DIA JULIANO --------------------#
else:
	lista_dias[1] = 29
	for elem in lista_dias[:mes-1]:
		dia_juliano += elem
	print ('Dia Juliano: {}'.format(dia_juliano + dia))
#-------------------- FIN DIA JULIANO --------------------#
