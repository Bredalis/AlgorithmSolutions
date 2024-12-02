
def cuarto_del_anio(mes):
	for i in range(1, 13):
		if mes == i and i <= 3:
			return 1

		if mes == i and i <= 6:
			return 2

		if mes == i and i <= 9:
			return 3

		if mes == i and i <= 12:
			return 4