numero_minimo_intervalo = int(input('Indica el comienzo del intervalo: '))
numero_maximo_intervalo = int(input('Indica el final del intervalo: '))

cantidad_numeros_dentro_intervalo = 0
maximo_fuera_intervalo = []
cantidad_numeros_fuera_intervalo = []
igual_numeros_extremos = False

#-------------------- CORRECION INTERVALO --------------------#
intercambio = numero_maximo_intervalo

if numero_minimo_intervalo > numero_maximo_intervalo:
	numero_maximo_intervalo = numero_minimo_intervalo
	numero_minimo_intervalo = intercambio
elif numero_minimo_intervalo < 0 or numero_maximo_intervalo < 0:
	print ('ERROR.')
#-------------------- FIN CORRECCION INTERVALO --------------------#

#-------------------- BUCLE INTRODUCCION NUMEROS --------------------#
numero = int(input('Indica un número: '))
while numero != 0:
#-------------------- CANTIDAD NUMEROS DENTRO INTERVALO --------------------#
	if numero < numero_maximo_intervalo and numero > numero_minimo_intervalo:
		cantidad_numeros_dentro_intervalo += 1
#-------------------- FIN CANTIDAD NUMEROS DENTRO INTERVALO --------------------#

#-------------------- NUMERO MAXIMO FUERA INTERVALO --------------------#
	elif numero > numero_maximo_intervalo or numero < numero_minimo_intervalo:
		maximo_fuera_intervalo.append(numero)
#-------------------- FIN NUMERO MAXIMO FUERA INTERVALO --------------------#

#-------------------- CANTIDAD NUMEROS FUERA INTERVALO --------------------#
	elif numero > numero_maximo_intervalo or numero < numero_minimo_intervalo:
		cantidad_numeros_fuera_intervalo.append(numero)
#-------------------- FIN CANTIDAD NUMEROS FUERA INTERVALO --------------------#

#-------------------- NUMEROS IGUAL A EXTREMOS --------------------#
	elif numero == numero_minimo_intervalo or numero == numero_maximo_intervalo:
		igual_numeros_extremos = True
	numero = int(input('Indica un número: '))
#-------------------- FIN NUMEROS IGUAL A EXTREMOS --------------------#
#-------------------- FIN BUCLE INTRODUCCION NUMEROS --------------------#


print ('Se han introducido {0} números que pertenecen al intervalo.'.format(cantidad_numeros_dentro_intervalo))
print ('El número maximo introducido fuera del intervalo es {0}.'.format(max(maximo_fuera_intervalo)))
print ('La media de los números que no pertenecen al intervalo es {0}'.format(sum(maximo_fuera_intervalo) / len(maximo_fuera_intervalo)))
if igual_numeros_extremos:
	print ('Se ha introducido un número igual a un límite del intervalo')