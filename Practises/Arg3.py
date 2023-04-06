# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre,
# y a continuación, una cantidad indefinida de números.
# La función debe devolver el siguiente mensaje:
# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    """devuelve la suma de los numeros"""
    suma_numeros = 0

    for numero in args:
        suma_numeros += numero

    return f"{nombre}, la suma de tus números es {suma_numeros}"

print(numeros_persona("Jonathan", 5, 3, 2))