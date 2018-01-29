#-------------------- CREACION CADENAS --------------------#
cadena = input('Indica una cadena: ')
cadena_2 = ''
#-------------------- FIN CREACION CADENAS --------------------#

#-------------------- COMPROBAR REPETICIONES --------------------#
for elem in cadena:
	if elem not in cadena_2:
		cadena_2 += elem

if cadena_2 == cadena:
	print ('En la cadena no existen caracteres repetidos.')
else:
	print ('En la cadena existen caracteres repetidos.')
#-------------------- FIN COMPROBAR REPETICIONES --------------------#