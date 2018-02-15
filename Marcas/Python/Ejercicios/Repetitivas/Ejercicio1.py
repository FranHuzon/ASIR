numero = int(input('Indica un número: '))
divisores = []
for n in range(1,numero):
	if numero % n == 0:
		divisores.append(n)

print ('Los divisores de {0} son {1} y {2}'.format(numero,divisores,numero))
