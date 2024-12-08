
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Sequencia_Inversa import sequencia_inversa

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(5, [5, 4, 3, 2, 1])
	]
)

def test_sequencia_inversa(input_x, expected):
	"""Prueba la función sequencia_inversa"""
	assert sequencia_inversa(input_x) == expected