
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Banquete import banquete

# Casos a testear
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		("great blue heron", "garlic naan", True),
		("chickadee", "chocolate cake", True),
		("brown bear", "bear claw", False)
	]
)

def test_banquete(input_x, input_y, expected):
	"""Prueba la función banquete"""
	resultado = banquete(input_x, input_y)
	assert resultado == expected