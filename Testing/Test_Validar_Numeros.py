
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Validar_Numeros import validar_numeros

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(123, True),
		(248, True), 
		(8, False),
		(321, True),
		(9453, False)
	]
)

def test_validar_numeros(input_x, expected):
	"""Prueba la función validar_numeros"""
	assert validar_numeros(input_x) == expected