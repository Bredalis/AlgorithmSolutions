
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Cadena import ordenar_cadena

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("CodeWars", "CdWr oeas"),
		("YCOLUE'VREER", "YOU'RE CLEVER")
	]
)

def test_ordenar_cadena(input_x, expected):
	"""Prueba la función ordenar_cadena"""
	assert ordenar_cadena(input_x) == expected