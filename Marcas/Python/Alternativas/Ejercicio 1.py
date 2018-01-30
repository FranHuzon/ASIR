dividendo = int(input('Indica el valor del dividendo: '))
divisor = int(input('Indica el valor del divisor: '))
#Almacena el resto de la división
resto = dividendo % divisor
#Almacena el cociente de la división
cociente = dividendo // divisor

#Comprueba si el resto de la división es igual a 0 para saber si la división es exacta o no.
if resto == 0:
	print ('La división es exacta. Cociente:', cociente)
elif resto != 0:
	print ('La división no es exacta. Cociente:', cociente, 'Resto:', resto)
elif divisor == 0:
print ('ERROR:El valor del divisor debe ser distinto de 0')
