año = int(input('¿En que año estamos?: '))
año1 = int(input('Indica el año deseado: '))
#Se restan los años indicados dependiendo de cual es mayor para saber la diferencia de años.
futuro = año1 - año
pasado = año - año1


if año < año1:
	print ('Para llegar al año', año1, 'faltan', futuro, 'años.')
elif año > año1:
	print ('Desde el año', año1, 'han pasado', pasado, 'años.')
elif futuro == 1:
	print ('Para llegar al año', año1, 'falta', futuro, 'año.')
elif pasado == 1:
	print ('Desde el año', año1, 'ha pasado', pasado, 'año.')
elif:
	print ('Son el mismo año.')