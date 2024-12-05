
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Cortar_Fecha import cortar_fecha

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		("Monday February 2, 8pm", "Monday February 2"),
		("Tuesday May 29, 8pm", "Tuesday May 29"), 
		("Wed September 1, 3am", "Wed September 1"),
		("Friday May 2, 9am", "Friday May 2"),
		("Tuesday January 29, 10pm", "Tuesday January 29")
	]
)

def test_cortar_fecha(input_x, expected):
	"""Prueba la función cortar_fecha"""
	assert cortar_fecha(input_x) == expected