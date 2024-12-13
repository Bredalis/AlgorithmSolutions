
# Esta función separa los caracteres de una cadena en dos grupos:
# los caracteres en posiciones pares y los de posiciones impares,
# y devuelve ambos grupos como una cadena de texto separada por un espacio.

def ordenar_cadena(cadena):
	pares = ""
	impares = ""

	for i in range(len(cadena)):
		if i % 2 == 0:
			pares += cadena[i]

		else:
			impares += cadena[i]

	return f"{pares} {impares}"