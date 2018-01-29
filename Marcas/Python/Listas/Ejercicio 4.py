#-------------------- CREACIÓN LISTA --------------------#
lista_alumnos_edad = []

alumno = input('Indica el nombre del alumno: ')
edad = int(input('Indica su edad: '))

print ()

while alumno != '*':
	lista_alumnos_edad.append(alumno)
	lista_alumnos_edad.append(edad)
	alumno = input('Indica el nombre del alumno: ')
	if alumno != '*':
		edad = int(input('Indica su edad: '))
	print ()
#-------------------- FIN CREACIÓN LISTA --------------------#

#-------------------- ALUMNOS CON MAS EDAD --------------------#
alumno_mas_mayor = []

for elem_1,elem_2 in zip(lista_alumnos_edad[0::2],lista_alumnos_edad[1::2]):
	if elem_2 == max(lista_alumnos_edad[1::2]):
		alumno_mas_mayor.append(elem_1)
#-------------------- FIN ALUMNOS CON MAS EDAD --------------------#

#-------------------- CONSULTA EDAD ALUMNO --------------------#
consulta_edad = input('¿De que alumno quieres saber su edad?: ')

for elem_1,elem_2 in zip(lista_alumnos_edad[0::2],lista_alumnos_edad[1::2]):
	if elem_1 == consulta_edad:
		print ('La edad del alumno {0} es {1}'.format(consulta_edad,elem_2))
#-------------------- FIN CONSULTA EDAD ALUMNO --------------------#

#-------------------- ALUMNOS MAYORES DE EDAD --------------------#
alumnos_mayores_edad = []

for elem_1,elem_2 in zip(lista_alumnos_edad[0::2],lista_alumnos_edad[1::2]):
	if elem_2 >= 18:
		alumnos_mayores_edad.append(elem_1)
		alumnos_mayores_edad.append(elem_2)
#-------------------- FIN ALUMNO MAYORES DE EDAD --------------------#

if len(alumno_mas_mayor) == 1:
	print ('El alumno más mayor es {0}'.format(alumno_mas_mayor))
else:
	print ('Los alumnos más mayores son {0}'.format(alumno_mas_mayor))
	
print ('La edad media de la clase es: {0}'.format(sum(lista_alumnos_edad[1::2]) / len(lista_alumnos_edad[1::2])))
print ('Los mayores de edad son {0}'.format(alumnos_mayores_edad))