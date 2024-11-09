
# Encontrar la sublista con la mayor
# suma en sus elementos de números enteros

def mayor_suma_elementos(lista):

	try:
		suma_de_elementos = []
		sublistas = []

		if not type(lista) == list:
			return "Debes ingresar una lista"

		for i in lista:
			if not type(i) == list:
				return "La lista solo debe tener sublistas"

			for j in i:
				if not type(j) == int:
					return "Los elementos de las sublistas solo deben ser números enteros"

			sublistas.append(i)
			suma_de_elementos.append(sum(i))

		sublista_con_mayor_suma = list(filter(lambda x: sum(x) == max(suma_de_elementos), sublistas))[0]
		return f"Sublista con la mayor suma de sus elementos {sublista_con_mayor_suma} con un resultado de {max(suma_de_elementos)}"

	except Exception as e:
		print(f"Error inesperado: {e}")

print(mayor_suma_elementos([[1, 2], [1], [6, 7, 10]]))