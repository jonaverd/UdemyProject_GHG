# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros),
# y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_numeros):
    """devuelve la cantidad de numeros pares que existen en la lista"""
    lista_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            pass
    return len(lista_pares)

lista_numeros = [0, 5, 63, 48, 25, 66, 10]
print(cantidad_pares(lista_numeros))
