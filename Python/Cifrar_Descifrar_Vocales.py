
def cifrar(string):
	for i, j in enumerate("aeiou", start = 1):
		string = string.replace(j, str(i))

	return  string

def descifrar(string):
    for i, j in enumerate("aeiou", start = 1):
    	string = string.replace(str(i), j)

    return  string