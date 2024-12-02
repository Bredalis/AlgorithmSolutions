
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Numeros_Divisibles_Por_Numero_Dado import divisible_por

# Casos a testear
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		([1, 2, 3, 4, 5, 6], 2, [2, 4, 6]),
		([1, 2, 3, 4, 5, 6], 3, [3, 6]),
		([0, 1, 2, 3, 4, 5, 6], 4, [0, 4]),
		([0], 4, [0]),
		([1, 3, 5], 2, []),
		([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	]
)

def test_divisible_por(input_x, input_y, expected):
	"""Prueba la función divisible_por"""
	resultado = divisible_por(input_x, input_y)
	assert resultado == expected