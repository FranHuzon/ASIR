#-------------------- IMPORTAR RAIZ CUADRADA --------------------#
from math import sqrt
#-------------------- FIN IMPORTAR RAIZ CUADRADA --------------------#
#-------------------- INTRODUCIR DATOS --------------------#
a = float(input('Indica el valor de "a": '))
b = float(input('Indica el valor de "b": '))
c = float(input('Indica el valor de "c": '))
#-------------------- FIN INTRODUCIR DATOS --------------------#
#-------------------- SOLUCIONES --------------------#
if a == 0:
	solucion = (-c / b)
	print ('La solución de la ecuación es: {}'.format(solucion))
elif b ** 2 - 4 * a * c < 0:
	print ('Raices complejas.')
#-------------------- FIN SOLUCIONES --------------------#