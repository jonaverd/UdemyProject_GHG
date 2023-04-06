# Crea una función llamada cantidad_atributos que cuente la cantidad de
# parémetros que se entregan, y devuelva esa cantidad como resultado.


def cantidad_atributos(**kwargs):
    """devuelve la cantidad de argumentos"""
    return len(kwargs)

print(cantidad_atributos(x="hola", y=5, z=(6,8)))