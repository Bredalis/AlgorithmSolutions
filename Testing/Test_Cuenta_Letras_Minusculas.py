
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Cuenta_Letras_Minusculas import cantidad_letras_minusculas

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("abc", 3),
		("abcABC123", 3),
		("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~", 3),
		("", 0),
		("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~", 0),
		("abcdefghijklmnopqrstuvwxyz", 26)
	]
)

def test_cantidad_letras_minusculas(input_x, expected):
	"""Prueba la función cantidad_letras_minusculas"""
	assert cantidad_letras_minusculas(input_x) == expected