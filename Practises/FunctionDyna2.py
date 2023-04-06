# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros)
# siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista_numeros):
    """Suma los numeros menores de una lista"""
    resultado_suma = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            resultado_suma += numero

    return resultado_suma

lista_numeros = [50, 2000, -6, 25]
print(suma_menores(lista_numeros))