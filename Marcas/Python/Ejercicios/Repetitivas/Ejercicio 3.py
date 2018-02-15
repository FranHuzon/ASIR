numero1 = int(input('Indica el valor del primer número: '))
numero2 = int(input('Indica el valor del segundo número (Mayor que {0}): '.format(numero1)))
suma = 0
sumandos = []

for n in range(numero1,numero2+1):
	suma += n
	sumandos.append(n)

print ('La suma de los números entre {0} y {1} es: {2}'.format(numero1,numero2,suma))
print (*sumandos, sep=' + ', end=' = ' '{0}'.format(suma))
print ()