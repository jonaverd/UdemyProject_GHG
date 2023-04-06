# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común),
# utilizando el método isdisjoint().
# Almacena dicho resultado en la variable conjuntos_aislados:
# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

# https://docs.python.org/es/3/library/stdtypes.html?highlight=isdisjoint#frozenset.isdisjoint
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
