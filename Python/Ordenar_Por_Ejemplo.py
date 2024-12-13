
# Esta función organiza una lista según el orden 
# de los elementos de un arreglo de ejemplo. Los elementos 
# de la lista de entrada se ordenan para coincidir con el 
# orden de los elementos del arreglo de ejemplo.

def ordenar_por_ejemplo(lista, lista_ejemplo):
	return [i for i in lista_ejemplo for j in lista if i == j]