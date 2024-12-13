
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Por_Ejemplo import ordenar_por_ejemplo

# Casos a testear
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		([1, 2, 3, 4, 5], [2, 3, 4, 1, 5], [2, 3, 4, 1, 5]), 
		([1, 2, 3, 3, 3, 4, 5], [2, 3, 4, 1, 5], [2, 3, 3, 3, 4, 1, 5]), 
		([1, 2, 3, 3, 3, 5], [2, 3, 4, 1, 5], [2, 3, 3, 3, 1, 5]),
		(["a", "a", "b", "f", "d", "a"], ["c", "a", "d", "b", "e", "f"], ["a", "a", "a", "d", "b", "f"])
	]
)

def test_ordenar_por_ejemplo(input_x, input_y, expected):
	"""Prueba la función ordenar_por_ejemplo"""
	resultado = ordenar_por_ejemplo(input_x, input_y)
	assert resultado == expected