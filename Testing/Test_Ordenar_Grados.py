
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Grados import ordenar_grados

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(["V1"], ["V1"]),
		(["V7", "V12", "V1"], ["V1", "V7", "V12"]),
		([], []),
		(["V13", "V14", "VB", "V0"], ["VB", "V0", "V13", "V14"]),
		(["V0+", "V0", "V16", "V2", "VB", "V6"], ["VB", "V0", "V0+", "V2", "V6", "V16"])
	]
)

def test_ordenar_grados(input_x, expected):
	"""Prueba la función ordenar_grados"""
	assert ordenar_grados(input_x) == expected