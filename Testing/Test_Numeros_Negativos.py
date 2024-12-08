
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Numeros_Negativos import numeros_negativos

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(42, -42), 
		(-9, -9), 
		(0, 0)
	]
)

def test_numeros_negativos(input_x, expected):
	"""Prueba la función numeros_negativos"""
	assert numeros_negativos(input_x) == expected