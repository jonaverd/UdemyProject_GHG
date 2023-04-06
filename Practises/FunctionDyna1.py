# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True
# si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo.
# Crea una lista llamada lista_numeros con valores positivos y negativos.
# No invoques la función, solo es necesario definirla.

def todos_positivos(lista_numeros):
    """Devuelve true si son todos positivos"""
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    else:
        return True

lista_numeros = [-9, 50, 0, -63, 42, -3]
print(todos_positivos(lista_numeros))