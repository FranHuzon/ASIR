num1 = float(input('Indica el valor del primer número: '))
num2 = float(input('Indica el valor del segundo número: '))
num3 = float(input('Indica el valor del tercer número: '))

if num1 == num2 and num2 == num3 and num1 == num3:
	print ('Los tres números indicados son iguales.')
elif num1 == num2 or num2 == num3 or num1 == num3:
	print ('Dos de los tres números indicados son iguales.')
else:
	print ('Los tres números indicados son distintos.')