a = float(input('Indica el valor del coeficiente A: '))
b = float(input('Indica el valor del coeficiente B: '))
solucion = -b / a

if a * solucion + b == 0:
	print ('La solución de la ecuación es:', solucion)