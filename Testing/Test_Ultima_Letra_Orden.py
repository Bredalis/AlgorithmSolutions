
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ultima_Letra_Orden import ultima_letra_orden

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("man i need a taxi up to ubud", ["a", "need", "ubud", "i", "taxi", "man", "to", "up"]),
		("what time are we climbing up the volcano", ["time", "are", "we", "the", "climbing", "volcano", "up", "what"]),
		("take me to semynak", ["take", "me", "semynak", "to"]),
		("massage yes massage yes massage", ["massage", "massage", "massage", "yes", "yes"]),
		("take bintang and a dance please", ["a", "and", "take", "dance", "please", "bintang"])
	]
)

def test_ultima_letra_orden(input_x, expected):
	"""Prueba la función ultima_letra_orden"""
	assert ultima_letra_orden(input_x) == expected