
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Palabras_Inversas import palabras_inversas

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("hello world!", "world! hello"),
		("345 num", "num 345")
	]
)

def test_palabras_inversas(input_x, expected):
	"""Prueba la función palabras_inversas"""
	assert palabras_inversas(input_x) == expected