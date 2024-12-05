
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Corto_Largo_Corto import corto_largo_corto

# Casos a testear
@pytest.mark.parametrize(
	"input_x, input_y, expected",
	[
		("45", "1", "1451"),
		("13", "200", "1320013"),
		("Soon", "Me", "MeSoonMe"),
		("U", "False", "UFalseU")
	]
)

def test_corto_largo_corto(input_x, input_y, expected):
	"""Prueba la función corto_largo_corto"""
	resultado = corto_largo_corto(input_x, input_y)
	assert resultado == expected