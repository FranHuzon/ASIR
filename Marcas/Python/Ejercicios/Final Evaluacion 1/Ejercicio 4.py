#-------------------- CREACION LISTA --------------------#
almacen = []
precio_con_iva = []
#-------------------- FIN CREACION LISTA --------------------#
#-------------------- AÑADIR ARTICULOS --------------------#
codigo_articulo = int(input('Código del artículo: '))
while codigo_articulo != 0:
	nombre_articulo = input('Nombre del artículo: ')
	cantidad_articulo = int(input('Cantidad del artículo: '))
	precio_articulo = float(input('Precio del artículo: '))
#-------------------- AÑADIR PRECIO CON IVA --------------------#	
	d1 = {'codigo':codigo_articulo, 'nombre':nombre_articulo, 'cantidad':cantidad_articulo, 'precio':precio_articulo + (precio_articulo * 0.21)}
	d2 = {'codigo':codigo_articulo, 'nombre':nombre_articulo, 'cantidad':cantidad_articulo, 'precio':precio_articulo + (precio_articulo * 0.21)}
#-------------------- FIN AÑADIR PRECIO CON IVA --------------------#
	almacen.append(d1)
	precio_con_iva.append(d2)
	codigo_articulo = int(input('Código del artículo: '))
#-------------------- FIN AÑADIR ARTICULOS --------------------#
#-------------------- PRECIO CON IVA --------------------#
for elem in precio_con_iva:
	elem.pop('cantidad')
print ('Lista de articulos con IVA añadido: {}'.format(precio_con_iva))
#-------------------- FIN PRECIO CON IVA --------------------#
#-------------------- CANTIDAD MENOR DE 10 --------------------#
menor_de_10 = []
for elem in almacen:
	if elem['cantidad'] < 10:
		d2 = {'codigo':elem['codigo'], 'nombre':elem['nombre']}
		menor_de_10.append(d2)
print ('Los articulos con cantidades menores a 10 son: {}'.format(menor_de_10))
#-------------------- FIN CANTIDAD MENOR DE 10 --------------------#
#-------------------- BUSQUEDA ARTICULO --------------------#
busqueda = int(input('¿Que codigo desea buscar?: '))
for elem in almacen:
	if busqueda == elem['codigo']:
		print ('El codigo {0} corresponde al artículo {1}'.format(elem['codigo'],elem['nombre']))
#-------------------- FIN BUSQUEDA ARTICULO --------------------#