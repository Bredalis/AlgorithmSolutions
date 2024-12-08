
def que_dia(num):
	dias = {1: "Domingo", 2: "Lunes", 3: "Martes", 4: "Miércoles", 5: "Jueves", 6: "Viernes", 7: "Sábado"}
	return "Incorrecto, por favor ingrese un número entre 1 y 7" if num == 0 or num > 7 else dias[num]