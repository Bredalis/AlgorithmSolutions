
def ordenar_grados(lista):
	grados = []

	if lista == []:
		return []

	for i in lista:
		if i[1:].isdigit():
			grados.append(int(i[1:]))

		if i == "VB":
			grados.insert(0, -1)

		if i == "V0+":
			grados.append(0.1)

	grados.sort()
	return ["V0+" if i == 0.1 else "VB" if i == -1 else f"V{i}" for i in grados]