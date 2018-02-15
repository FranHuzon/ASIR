#-------------------- CREACION LISTA --------------------#
lista_alumnos_edad = []
ficha_alumno = []

alumno = input('Indica el nombre del alumno: ')
edad = int(input('Indica su edad: '))

print ()

while alumno != '*':
	ficha_alumno.append(alumno)
	ficha_alumno.append(edad)
	lista_alumnos_edad.append(ficha_alumno)
	ficha_alumno = []
	alumno = input('Indica el nombre del alumno: ')
	if alumno != '*':
		edad = int(input('Indica su edad: '))
	print ()
#-------------------- FIN CREACION LISTA --------------------#

#-------------------- ALUMNOS CON MAS EDAD --------------------#
alumno_mas_mayor = []
edad_maxima = 0

for elem in lista_alumnos_edad:
	if elem[1] > edad_maxima:
		edad_maxima = elem[1]
	if elem[1] == edad_maxima:
		alumno_mas_mayor.append(elem[0])
#-------------------- FIN ALUMNOS CON MAS EDAD --------------------#

#-------------------- MEDIA EDAD CLASE --------------------#
suma_edades = 0

for elem in lista_alumnos_edad:
	suma_edades += elem[1]
#-------------------- FIN MEDIA EDAD CLASE --------------------#

#-------------------- CONSULTA EDAD --------------------#
consulta_edad = input('¿De que alumno quieres saber su edad?: ')

for elem in lista_alumnos_edad:
	if elem[0] == consulta_edad:
		print ('La edad del alumno {0} es {1}'.format(elem[0],elem[1]))
#-------------------- FIN CONSULTA EDAD --------------------#

#-------------------- MAYORES EDAD --------------------#
alumnos_mayores_edad = []
ficha_alumno_mayor_edad = []

for elem in lista_alumnos_edad:
	if elem[1] >= 18:
		ficha_alumno_mayor_edad.append(elem[0])
		ficha_alumno_mayor_edad.append(elem[1])
		alumnos_mayores_edad.append(ficha_alumno_mayor_edad)
		ficha_alumno_mayor_edad = []
#-------------------- FIN MAYORES EDAD --------------------#

if len(alumno_mas_mayor) == 1:
	print ('El alumno más mayor es {0}'.format(alumno_mas_mayor))
else:
	print ('Los alumnos más mayores son {0}'.format(alumno_mas_mayor))

print ('La edad media de la clase es {0}'.format(suma_edades / len(lista_alumnos_edad)))
print ('Los mayores de edad son {0}'.format(alumnos_mayores_edad))
		alumno_mas_mayor.append(elem[0])
#-------------------- FIN ALUMNOS CON MAS EDAD --------------------#

#-------------------- MEDIA EDAD CLASE --------------------#
suma_edades = 0

for elem in lista_alumnos_edad:
	suma_edades += elem[1]
#-------------------- FIN MEDIA EDAD CLASE --------------------#

#-------------------- CONSULTA EDAD --------------------#
consulta_edad = input('¿De que alumno quieres saber su edad?: ')

for elem in lista_alumnos_edad:
	if elem[0] == consulta_edad:
		print ('La edad del alumno {0} es {1}'.format(elem[0],elem[1]))
#-------------------- FIN CONSULTA EDAD --------------------#

#-------------------- MAYORES EDAD --------------------#
alumnos_mayores_edad = []
ficha_alumno_mayor_edad = []

for elem in lista_alumnos_edad:
	if elem[1] >= 18:
		ficha_alumno_mayor_edad.append(elem[0])
		ficha_alumno_mayor_edad.append(elem[1])
		alumnos_mayores_edad.append(ficha_alumno_mayor_edad)
		ficha_alumno_mayor_edad = []
#-------------------- FIN MAYORES EDAD --------------------#

if len(alumno_mas_mayor) == 1:
	print ('El alumno más mayor es {0}'.format(alumno_mas_mayor))
else:
	print ('Los alumnos más mayores son {0}'.format(alumno_mas_mayor))
	
print ('La edad media de la clase es {0}'.format(suma_edades / len(lista_alumnos_edad)))
print ('Los mayores de edad son {0}'.format(alumnos_mayores_edad))