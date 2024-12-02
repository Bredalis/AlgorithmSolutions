
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Cuarto_Del_Año import cuarto_del_anio

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(3, 1),
		(8, 3), 
		(11, 4),
		(9, 3)
	]
)

def test_cuarto_del_anio(input_x, expected):
	"""Prueba la función cuarto_del_anio"""
	assert cuarto_del_anio(input_x) == expected