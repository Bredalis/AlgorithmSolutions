
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_String import ordenar_string

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("abcdef", "abcdef"),
		("pqksuvy", "kpqsuvy"),
		("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz")
	]
)

def test_ordenar_string(input_x, expected):
	"""Prueba la función ordenar_string"""
	assert ordenar_string(input_x) == expected