def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def contar_primos(limite):
    """Rango de primos hasta limite"""

    lista = []

    for numero in range(2, limite):
        if es_primo(numero):
            lista.append(numero)
        else:
            pass

    return lista


print(contar_primos(50))
