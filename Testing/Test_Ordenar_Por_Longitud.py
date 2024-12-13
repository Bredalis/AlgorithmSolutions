
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Por_Longitud import ordenar_por_longitud

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
	    (["beg", "life", "i", "to"], ["i", "to", "beg", "life"]),
	    (["", "moderately", "brains", "pizza"], ["", "pizza", "brains", "moderately"]),
	    (["longer", "longest", "short"], ["short", "longer", "longest"]),
	    (["dog", "food", "a", "of"], ["a", "of", "dog", "food"]),
	    (["", "dictionary", "eloquent", "bees"], ["", "bees", "eloquent", "dictionary"])
	]
)

def test_ordenar_por_longitud(input_x, expected):
	"""Prueba la función ordenar_por_longitud"""
	assert ordenar_por_longitud(input_x) == expected