
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Ordenar_Renos import ordenar_renos

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
	    (["Kenjiro Mori", "Susumu Tokugawa", "Akira Sanada"], ["Kenjiro Mori", "Akira Sanada", "Susumu Tokugawa"]),
	    ([], []),
	    (["Daisuke Mori", "Saburo Shima", "Juzo Yabu", "Sukeharu Yamamoto"], ["Daisuke Mori", "Saburo Shima", "Juzo Yabu", "Sukeharu Yamamoto"]),
	    (["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Daisuke Mori"], ["Daisuke Mori", "Saburo Shima", "Juzo Yabu", "Sukeharu Yamamoto"])
	]
)

def test_ordenar_renos(input_x, expected):
	"""Prueba la función ordenar_renos"""
	assert ordenar_renos(input_x) == expected