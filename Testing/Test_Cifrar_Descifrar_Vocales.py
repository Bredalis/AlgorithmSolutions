
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Cifrar_Descifrar_Vocales import cifrar, descifrar

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("hello", "h2ll4"),
		("How are you today?", "H4w 1r2 y45 t4d1y?"),
		("This is an encoding test.", "Th3s 3s 1n 2nc4d3ng t2st.")
	]
)

def test_cifrar(input_x, expected):
	"""Prueba la función cifrar"""
	assert cifrar(input_x) == expected

def test_descifrar():
	"""Prueba la función descifrar"""
	assert descifrar("h2ll4") == "hello"