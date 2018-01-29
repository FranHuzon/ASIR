#-------------------- CREACION CADENAS --------------------#
palabra = input('Indica una palabra: ')
frase = input('Indica una frase: ')
frase_sin_espacios = ''
#-------------------- FIN CREACION CADENAS --------------------#

#-------------------- CREACION VARIABLES --------------------#
palabra_palindroma = False
frase_palindroma = False
#-------------------- FIN CREACION VARIABLES --------------------#

#-------------------- QUITAR ESPACIOS --------------------#
for caracter in frase:
	if caracter != ' ':
		frase_sin_espacios += caracter
#-------------------- FIN QUITAR ESPACIOS --------------------#

#-------------------- COMPROBAR PALABRA --------------------#
if palabra == palabra[::-1]:
	palabra_palindroma = True
#-------------------- FIN COMPROBAR PALABRA --------------------#

#-------------------- COMPROBAR FRASE --------------------#
if frase_sin_espacios == frase_sin_espacios[::-1]:
	frase_palindroma = True
#-------------------- FIN COMPROBAR FRASE --------------------#

if palabra_palindroma:
	print ('La palabra indicada es palíndroma.')

if frase_palindroma:
print ('La frase indicada es palíndroma.')