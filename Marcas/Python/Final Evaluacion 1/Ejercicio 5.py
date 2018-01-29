#-------------------- INTRODUCIR DATOS --------------------#
cantidad_total = float(input('Cantidad total: '))
cantidad_entregada = float(input('Cantidad entregada: '))
cantidad_devolver = print ('Cantidad a devolver: {}'.format(round(cantidad_entregada - cantidad_total,2)))
cantidad_devolver_2 = round(cantidad_entregada - cantidad_total,2)
#-------------------- FIN INTRODUCIR DATOS --------------------#
#-------------------- CREAR VARIABLES --------------------#
billete_200 = 0
billete_100 = 0
billete_50 = 0
billete_20 = 0
billete_10 = 0
billete_5 = 0
moneda_2 = 0
moneda_1 = 0
moneda_50 = 0
moneda_20 = 0
moneda_10 = 0
moneda_5 = 0
moneda_2_c = 0
moneda_1_c = 0
#-------------------- FIN CREAR VARIABLES --------------------#
#-------------------- CALCULAR CAMBIO --------------------#
while cantidad_devolver_2 != 0:
	if cantidad_devolver_2 >= 200:
		billete_200 += int(cantidad_devolver_2 // 200)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_200 * 200),2)
	if cantidad_devolver_2 >= 100:
		billete_100 += int(cantidad_devolver_2 // 100)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_100 * 100),2)
	if cantidad_devolver_2 >= 50:
		billete_50 += int(cantidad_devolver_2 // 50)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_50 * 50),2)
	if cantidad_devolver_2 >= 20:
		billete_20 += int(cantidad_devolver_2 // 20)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_20 * 20),2)
	if cantidad_devolver_2 >= 10:
		billete_10 += int(cantidad_devolver_2 // 10)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_10 * 10),2)
	if cantidad_devolver_2 >= 5:
		billete_5 += int(cantidad_devolver_2 // 5)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (billete_5 * 5),2)
	if cantidad_devolver_2 >= 2:
		moneda_2 += int(cantidad_devolver_2 // 2)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_2 * 2),2)
	if cantidad_devolver_2 >= 1:
		moneda_1 += int(cantidad_devolver_2 // 1)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_1 * 1),2)
	if cantidad_devolver_2 >= 0.5:
		moneda_50 += int(cantidad_devolver_2 // 0.5)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_50 * 0.5),2)
	if cantidad_devolver_2 >= 0.2:
		moneda_20 += int(cantidad_devolver_2 // 0.2)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_20 * 0.2),2)
	if cantidad_devolver_2 >= 0.1:
		moneda_10 += int(cantidad_devolver_2 // 0.1)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_10 * 0.1),2)
	if cantidad_devolver_2 >= 0.05:
		moneda_5 += int(cantidad_devolver_2 // 0.05)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_5 * 0.05),2)
	if cantidad_devolver_2 >= 0.02:
		moneda_2_c += int(cantidad_devolver_2 // 0.02)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_2_c * 0.02),2)
	if cantidad_devolver_2 >= 0.01:
		moneda_1_c += int(cantidad_devolver_2 // 0.01)
		cantidad_devolver_2 = round(cantidad_devolver_2 - (moneda_1_c * 0.01),2)
#-------------------- FIN CALCULAR CAMBIO --------------------#
#-------------------- CAMBIO --------------------#
if billete_200 == 1:
	print ('{} billete de 200€.'.format(billete_200))
elif billete_200 > 1:
	print ('{} billetes de 200€.'.format(billete_200))
if billete_100 == 1:
	print ('{} billete de 100€.'.format(billete_100))
elif billete_100 > 1:
	print ('{} billetes de 100€.'.format(billete_100))
if billete_50 == 1:	
	print ('{} billete de 50€.'.format(billete_50))
elif billete_50 > 1:
	print ('{} billetes de 50€.'.format(billete_50))
if billete_20 == 1:
	print ('{} billete de 20€.'.format(billete_20))
elif billete_20 > 1:
	print ('{} billetes de 20€.'.format(billete_20))
if billete_10 == 1:
	print ('{} billete de 10€.'.format(billete_10))
elif billete_10 > 1:
	print ('{} billetes de 10€.'.format(billete_10))
if billete_5 == 1:
	print ('{} billete de 5€.'.format(billete_5))
elif billete_5 > 1:
	print ('{} billetes de 5€.'.format(billete_5))
if moneda_2 == 1:
	print ('{} moneda de 2€.'.format(moneda_2))
elif moneda_2 > 1:
	print ('{} monedas de 2€.'.format(moneda_2))
if moneda_1 == 1:
	print ('{} moneda de 1€.'.format(moneda_1))
elif moneda_1 > 1:
	print ('{} monedas de 1€.'.format(moneda_1))
if moneda_50 == 1:
	print ('{} moneda de 50 cent.'.format(moneda_50))
elif moneda_50 > 1:
	print ('{} monedas de 50 cent.'.format(moneda_50))
if moneda_20 == 1:
	print ('{} moneda de 20 cent.'.format(moneda_20))
elif moneda_20 > 1:
	print ('{} monedas de 20 cent.'.format(moneda_20))
if moneda_10 == 1:
	print ('{} moneda de 10 cent.'.format(moneda_10))
elif moneda_10 > 1:
	print ('{} monedas de 10 cent.'.format(moneda_10))
if moneda_5 == 1:
	print ('{} moneda de 5 cent.'.format(moneda_5))
elif moneda_5 > 1:
	print ('{} monedas de 5 cent.'.format(moneda_5))
if moneda_2_c == 1:
	print ('{} moneda de 2 cent.'.format(moneda_2_c))
elif moneda_2_c > 1:
	print ('{} monedas de 2 cent.'.format(moneda_2_c))
if moneda_1_c == 1:
	print ('{} moneda de 1 cent.'.format(moneda_1_c))
elif moneda_1_c > 1:
	print ('{} monedas de 1 cent.'.format(moneda_1_c))
#-------------------- FIN CAMBIO --------------------#