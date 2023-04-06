def ordenar_letras(palabra):
    """devuelve todas las letras sin repetir"""
    lista = []

    for letra in palabra:

        if letra not in lista:
            lista.append(letra)

        else:
            pass

    lista.sort()

    return lista

print(ordenar_letras("jonathan"))

# Se puede hacer con sets para guardar sin repetir y luego castearlo a una lista para ordenarlo
# set = set()
# for ...
#    set.add()
# lista = list(set)