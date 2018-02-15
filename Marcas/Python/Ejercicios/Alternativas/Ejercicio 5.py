dato = int(input('Indica una longitud expresada en centímetros: '))
centimetros = (dato % 100000) % 100
metros = (dato % 100000) // 100
kilometros = dato // 100000

if kilometros == 0 and metros == 0:
	print ('{0} centímetros son {1} cm.'.format(dato,centimetros))
elif metros == 0  and centimetros == 0:
	print ('{0} centímetros son {1} km.'.format(dato,kilometros))
elif kilometros == 0 and centimetros == 0:
	print ('{0} centímetros son {1} m.'.format(dato,metros))
elif kilometros == 0:
	print ('{0} centímetros son {1} m y {2} cm.'.format(dato,metros,centimetros))
elif metros == 0:
	print ('{0} centímetros son {1} km y {2} cm.'.format(dato,kilometros,centimetros))
elif centimetros == 0:
	print ('{0} centimetros son {1} km, {2} m.'.format(dato,kilometros,metros))
else:
	print ('{0} centimetros son {1} km, {2} m y {3} centímetros.'.format (dato,kilometros,metros,centimetros))
