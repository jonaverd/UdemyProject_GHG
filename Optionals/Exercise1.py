def devolver_distintos(num1, num2, num3):
    """devuelve el mayor, menor o el intermedio"""

    lista = [num1, num2, num3]
    suma = sum(lista)

    if suma > 15:
        return max(lista)

    elif suma < 10:
        return min(lista)

    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(5, 3, 1))


