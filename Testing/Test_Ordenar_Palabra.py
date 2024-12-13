
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Palabra import ordenar_palabra

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
	    ("Hello, World!", " !,HWdellloor"),
	    ("bobby", "bbboy"),
	    ("", "Invalid String!"),
	    ("\"][@!#$*(^&%", "!\"#$%&(*@[]^"),
	    (None, "Invalid String!")
	]
)

def test_ordenar_palabra(input_x, expected):
	"""Prueba la función ordenar_palabra"""
	assert ordenar_palabra(input_x) == expected