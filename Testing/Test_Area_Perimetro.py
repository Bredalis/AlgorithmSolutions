
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Area_Perimetro import area_perimetro

# Casos a testear
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		(4, 4, 16),
		(2, 2, 4), 
		(6, 10, 32)
	]
)

def test_area_perimetro(input_x, input_y, expected):
	"""Prueba la función area_perimetro"""
	resultado = area_perimetro(input_x, input_y)
	assert resultado == expected