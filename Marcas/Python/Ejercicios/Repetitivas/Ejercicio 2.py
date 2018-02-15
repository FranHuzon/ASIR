cantidadnumeros = int(input('¿Cuantos números se van a introducir?: '))
numero = int(input('Indica un número: '))
for n in range(cantidadnumeros):
	numero2 = int(input('Indica un número mayor que {0}: '.format(numero)))
	if numero2 < numero:
		print ('{0} no es mayor que {1}'.format(numero2,numero))