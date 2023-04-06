# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados
# en forma de palabras clave (keywords).
# La función debe preveer recibir cualquier cantidad de argumentos de este tipo.


def lista_atributos(**kwargs):
    """devuelve los argumentos en una lista"""
    lista = []

    for valor in kwargs.values():
        lista.append(valor)

    return lista

print(lista_atributos(c1=100, c2=200, c3=300))