from random import randint

cantidad_preguntas = int(input('Número de preguntas: '))
multiplicando = randint (2,10)
multiplicador = randint (2,10)
resultado = multiplicando * multiplicador
respuestas_correctas = 0

#-------------------- CORRECION CANTIDAD PREGUNTAS --------------------#
if cantidad_preguntas < 0:
	print ('El número de preguntas debe ser al menos 1.')
#-------------------- FIN CORRECCION CANTIDAD PREGUNTAS --------------------#

#-------------------- BUCLE RESPUESTAS --------------------#
for n in range (cantidad_preguntas):
	respuesta = int(input('¿Cuanto es {0} * {1}?: '.format(multiplicando,multiplicador)))
#-------------------- COMPROBACION RESPUESTA CORRECTA --------------------#	
	if respuesta == resultado:
		print ('Respuesta correcta.')
		respuestas_correctas += 1
#-------------------- FIN COMPROBACION RESPUESTA CORRECTA --------------------#

#-------------------- COMPROBACION RESPUESTA INCORRECTA --------------------#
	else:
		print ('Respuesta incorrecta.')
	multiplicando = randint (2,10)
	multiplicador = randint (2,10)
	resultado = multiplicando * multiplicador
#-------------------- FIN COMPROBACION RESPUESTA INCORRECTA --------------------#
#-------------------- FIN BUCLE RESPUESTAS --------------------#

#-------------------- CANTIDAD RESPUESTAS CORRECTAS --------------------#
if respuestas_correctas == 1:
	print ('Ha contestado correctamente 1 pregunta.')
else:
	print ('Ha contestado correctamente {0} preguntas.'.format(respuestas_correctas))
#-------------------- FIN CANTIDAD RESPUESTAS CORRECTAS --------------------#

#-------------------- NOTA CORRESPONDIENTE --------------------#
if respuestas_correctas / cantidad_preguntas * 10 >= 9:
	print ('Le corresponde una nota de', respuestas_correctas / cantidad_preguntas * 10)
	print ('Enhorabuena!!!!')
else:
	print ('Le corresponde una nota de', round(respuestas_correctas / cantidad_preguntas * 10,1))
#-------------------- FIN NOTA CORRESPONDIENTE --------------------#