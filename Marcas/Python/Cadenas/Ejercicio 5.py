#-------------------- CREAR VARIABLES --------------------#
aciertos = 0
coincidencias = 0
intentos = 1
#-------------------- FIN CREAR VARIABLES --------------------#

#-------------------- GENERAR NUMERO ALEATORIO --------------------#
import random
from random import randint

digito_1 = str(randint(1,9))
digito_2 = str(randint(1,9))
digito_3 = str(randint(1,9))
digito_4 = str(randint(1,9))
numero_adivinar = ''
numero_adivinar_definitivo = ''

if numero_adivinar == '':
	numero_adivinar += digito_1
	numero_adivinar += digito_2
	numero_adivinar += digito_3
	numero_adivinar += digito_4

for elem in numero_adivinar:
	if elem not in numero_adivinar_definitivo:
		numero_adivinar_definitivo += elem

while len(numero_adivinar_definitivo) < 4:
	digito_1 = str(randint(1,9))
	digito_2 = str(randint(1,9))
	digito_3 = str(randint(1,9))
	digito_4 = str(randint(1,9))
	numero_adivinar = ''
	numero_adivinar_definitivo = ''
	
	if numero_adivinar == '':
		numero_adivinar += digito_1
		numero_adivinar += digito_2
		numero_adivinar += digito_3
		numero_adivinar += digito_4

	for elem in numero_adivinar:
		if elem not in numero_adivinar_definitivo:
			numero_adivinar_definitivo += elem
#-------------------- FIN GENERAR NUMERO ALEATORIO --------------------#

#-------------------- BIENVENIDA / COMIENZO JUEGO --------------------#
print ('Bienvenido/a a Mastermind !!!')
print ('Tienes que adivinar un código de 4 digitos en el menor número de intentos posbiles.')
print ('Buena suerte ^^ !!!')
print ()

codigo_usuario = input('¿Qué código propones?: ')
while len(codigo_usuario) != 4:
	codigo_usuario =  input('ERROR: Vuelve a introducir el código: ')
#-------------------- FIN BIENVENIDA / COMIENZO JUEGO --------------------#

#-------------------- BUCLE COINCIDENCIAS / ACIERTOS / INTENTOS --------------------#
#-------------------- COMPROBAR COINCIDENCIAS / ACIERTOS --------------------#
while codigo_usuario != numero_adivinar_definitivo:
	for elem_1,elem_2 in zip(numero_adivinar_definitivo,codigo_usuario):
		if elem_1 == elem_2:
			aciertos += 1
		elif elem_2 in numero_adivinar_definitivo:
			coincidencias += 1
#-------------------- FIN COMPROBAR COINCIDENCIAS / ACIERTOS --------------------#
#-------------------- CANTIDAD COINCIDENCIAS / ACIERTOS --------------------#
	if aciertos == 1 and coincidencias == 1:
		print ('El codigo propuesto ( {0} ) tiene {1} acierto y {2} coincidencia.'.format(codigo_usuario,aciertos,coincidencias))
	elif coincidencias == 1:
		print ('El codigo propuesto ( {0} ) tiene {1} aciertos y {2} coincidencia.'.format(codigo_usuario,aciertos,coincidencias))
	elif aciertos == 1:
		print ('El codigo propuesto ( {0} ) tiene {1} acierto y {2} coincidencias.'.format(codigo_usuario,aciertos,coincidencias))
	else:
		print ('El codigo propuesto ( {0} ) tiene {1} aciertos y {2} coincidencias.'.format(codigo_usuario,aciertos,coincidencias))
	intentos += 1
#-------------------- FIN CANTIDAD COINCIDENCIAS / ACIERTOS --------------------#	
	coincidencias = 0
	aciertos = 0
	print ()
	codigo_usuario = input('Propón otro código: ')
	while len(codigo_usuario) != 4:
		codigo_usuario =  input('ERROR: Vuelve a introducir el código: ')
#-------------------- FIN BUCLE COINCIDENCIAS / ACIERTOS / INTENTOS --------------------#

#-------------------- CANTIDAD INTENTOS --------------------#
if intentos == 1:
	print ('Felicidades!!! Has acertado el código en {0} intento.'.format(intentos))
else:
	print ('Felicidades!!! Has acertado el código en {0} intentos.'.format(intentos))
#-------------------- FIN CANTIDAD INTENTOS --------------------#