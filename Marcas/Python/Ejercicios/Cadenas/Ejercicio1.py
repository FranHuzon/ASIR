#-------------------- CREACION CADENAS --------------------#
cadena = input('Indica el valor de la primera cadena: ')
cadena_2 = input ('Indica el valor de la segunda cadena: ')
#-------------------- FIN CREACION CADENAS --------------------# 

#-------------------- COMPROBAR COINCIDENCIA --------------------#
if cadena_2 in cadena or cadena_2 in cadena.upper():
	print ('La segunda cadena es una subcadena de la primera.')
else:
	print ('La segunda cadena no es una subcadena de la primera.')
#-------------------- FIN COMPROBAR COINCIDENCIA --------------------#
