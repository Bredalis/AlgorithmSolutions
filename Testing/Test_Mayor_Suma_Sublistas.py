
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Mayor_Suma_Sublistas import mayor_suma_elementos

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("Hola", "Debes ingresar una lista"),
		([1, 2, 3], "La lista solo debe contener sublistas"), 
		([["d"], [2, 3]], "Los elementos de las sublistas deben ser números enteros"),
		(None, "Debes ingresar una lista"),
		([[2, 3, 4], [4, 5, 7]], "Sublista con la mayor suma de sus elementos: [4, 5, 7], con una suma de 16")
	]
)

def test_mayor_suma_elementos(input_x, expected):
	"""Prueba la función mayor_suma_elementos"""
	assert mayor_suma_elementos(input_x) == expected