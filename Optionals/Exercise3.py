def repetidos(*args):
    """devuelve true si el 0 se repite dos veces seguidas"""

    for index, numero in enumerate(args):
        if args[index] == 0 and args[index+1] == 0:
            return True
        else:
            pass

    return False

print(repetidos(5, 6, 1, 0, 0, 9, 3, 5))
print(repetidos(6, 0, 5, 1, 0, 3, 0, 1))

# se puede hacer con una variable contador + 1 en cada interaccion del bucle
# en vez de [index], seria [contador]
# si da error porque el contador se sale del bucle, hacer un if con el len(args)
# y devolver False, para que no siga contando