
# Encontrar la sublista con la mayor suma de elementos enteros
def mayor_suma_elementos(lista = None):
    try:
        if not isinstance(lista, list):
            return "Debes ingresar una lista"

        sublistas = []
        suma_de_elementos = []

        for sublista in lista:
            if not isinstance(sublista, list):
                return "La lista solo debe contener sublistas"
            
            if not all(isinstance(x, int) for x in sublista):
                return "Los elementos de las sublistas deben ser números enteros"

            sublistas.append(sublista)
            suma_de_elementos.append(sum(sublista))

        max_suma = max(suma_de_elementos)
        sublista_con_mayor_suma = sublistas[suma_de_elementos.index(max_suma)]
        return f"Sublista con la mayor suma de sus elementos: {sublista_con_mayor_suma}, con una suma de {max_suma}"

    except Exception as e:
        return f"Error inesperado: {e}"