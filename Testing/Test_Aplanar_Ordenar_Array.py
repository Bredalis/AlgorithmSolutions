
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Aplanar_Ordenar_Array import aplanar_ordenar

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		([], []),
		([[], []], []),
		([[], [1]], [1]),
		([[3, 2, 1], [7, 9, 8], [6, 4, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
		([[1, 3, 5], [100], [2, 4, 6]], [1, 2, 3, 4, 5, 6, 100])
	]
)

def test_aplanar_ordenar(input_x, expected):
	"""Prueba la función aplanar_ordenar"""
	assert aplanar_ordenar(input_x) == expected