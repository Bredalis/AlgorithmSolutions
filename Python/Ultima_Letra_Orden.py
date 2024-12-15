
def ultima_letra_orden(cadena):
	return sorted(cadena.split(), key = lambda x: x[-1])