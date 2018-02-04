def convertir_a_segundos(horas,minutos,segundos):
	segundos_totales = (horas * 3600) + (minutos * 60) + segundos
	return segundos_totales

def calcular_coste(segundos,coste):
	factura = segundos * coste
	return factura

def convertir_a_euros(centimos):
	euros = centimos / 100
	return euros
