
# Librerías para modificar la ruta
from Ruta_Python import *

# Librería para testing
import pytest
from Dias_De_La_Semana import que_dia

# Casos a testear
@pytest.mark.parametrize(
	"input_x, expected",
	[
		(1, "Domingo"),
		(2, "Lunes"),
		(3, "Martes"),
		(8, "Incorrecto, por favor ingrese un número entre 1 y 7"),
		(20, "Incorrecto, por favor ingrese un número entre 1 y 7")
	]
)

def test_que_dia(input_x, expected):
	"""Prueba la función que_dia"""
	assert que_dia(input_x) == expected