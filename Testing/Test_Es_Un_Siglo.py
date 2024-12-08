
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Es_Un_Siglo import siglo

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(1705, 18),
		(1900, 19),
		(1601, 17),
		(2000, 20),
		(356, 4),
		(89, 1)
	]
)

def test_siglo(input_x, expected):
	"""Prueba la función siglo"""
	assert siglo(input_x) == expected