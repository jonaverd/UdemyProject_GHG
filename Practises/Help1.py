# Remueve los caracteres a la izquierda de nuestro texto principal:
# ,
# :
# %
# _
# #
# Utiliza el método lstrip(). Imprime el resultado en pantalla:
#
# ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa.
# Puedes utilizar variables intermedias si las necesitas.

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# https://docs.python.org/es/3/library/stdtypes.html?highlight=lstrip#str.lstrip
print(texto.lstrip(",:%_#"))
