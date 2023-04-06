# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros),
# y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos)
# y eliminando el valor más alto. El orden de los elementos puede modificarse.
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la
# anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

import statistics

lista_numeros = [1, 2, 15, 7, 2]


def eliminar_duplicados(lista):
    """elimina numero repetidos, dejando solo uno de cada"""

    filtrada = []

    for numero in lista:
        if numero not in filtrada:
            filtrada.append(numero)
        else:
            pass

    return filtrada


def eliminar_maximo(lista):
    """elimina el numero mas grande"""
    lista.remove(max(lista))
    return lista


def reducir_lista(lista):
    """aplica una serie de filtros"""
    return eliminar_maximo(eliminar_duplicados(lista))


def promedio(lista):
    """devuelve el valor medio"""
    return statistics.mean(lista)


print(round(promedio(reducir_lista(lista_numeros)), 2))
