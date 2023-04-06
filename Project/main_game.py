from os import system
from random import choice


def limpiar_consola():
    # Windows
    # return system('cls')
    # Others
    return system('clear')


def elegir_palabra():
    """Genera una palabra secreta para ser adivinada y su pista"""
    lista_palabras = {"animales": {"tiburon": "acuatico",
                                   "elefante": "terrestre",
                                   "dromedario": "desierto",
                                   "aguila": "volador"},
                      "inventos": {"cuchara": "cocina",
                                   "bicicleta": "vehiculo",
                                   "ordenador": "tecnologia",
                                   "archivador": "oficina"},
                      "deportes": {"baloncesto": "deporte",
                                   "vestuario": "lugar",
                                   "silbato": "instrumento",
                                   "campeonato": "evento"},
                      "geografía": {"guadalquivir": "rio",
                                    "vesubio": "monte",
                                    "kazajistan": "pais",
                                    "londres": "capital"}
                      }
    categoria_random = choice(list(lista_palabras.items()))
    palabra_random = choice(list(categoria_random[1].items()))

    # Se devuelve categoria, palabra y pista, en ese orden
    return categoria_random[0], palabra_random[0], palabra_random[1]


def es_valido_nombre(entrada):
    """Comprueba si la entrada es un nombre con formato valido"""
    if entrada.isalpha():
        return True
    else:
        print(f"La entrada '{entrada}' no es válida")
        return False


def es_valida_letra(entrada):
    """Comprueba si la entrada es una letra con formato valido"""
    if entrada.isalpha() and len(entrada) == 1:
        return True
    else:
        print(f"La entrada '{entrada}' no es válida. Por favor, introduce una letra ")
        return False


def esta_en_palabra(letra, palabra):
    """Comprueba si la letra está en la palabra"""
    if letra in palabra:
        return True
    else:
        return False


def mostrar_guiones(palabra, letras_reveladas):
    """Muestra guiones según las letras de la palabra y las letras reveladas"""
    guiones = ""
    for letra in palabra:
        if letra in letras_reveladas:
            guiones += letra.upper()
        else:
            guiones += "█ "
    print(guiones + "\n")


def mostrar_incorrectas(letras):
    """Imprime una coleccion de letras incorrectas"""
    cadena = ""
    if len(letras) > 0:
        cadena += "Las letras "
        for letra in letras:
            cadena += f"'{letra.upper()}' "
        else:
            print(f"{cadena}no están en la palabra")
            print("")
    else:
        print(f"Todas las letras siguen disponibles")
        print("")


def es_completada(palabra, letras_reveladas):
    """Indica si la palabra secreta ya ha sido totalmente revelada"""
    return set(palabra) == letras_reveladas


def dibujar_muñeco(vidas):
    """dibuja el muñeco del ahorcado según las vidas que queden"""
    if vidas == 6:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |             'Se respira paz'\n"
              f"   | \n"
              f"   | \n")

    elif vidas == 5:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (͡°͜ʖ͡°)  '¡Ayudame bro!'\n"
              f"   | \n"
              f"   | \n")

    elif vidas == 4:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (͡°͜ʖ͡°)  '¡Mi abuela juega mejor!'\n"
              f"   |       |\n"
              f"   | \n"
              f"   | \n")

    elif vidas == 3:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (͡°͜ʖ͡°)  '¡WTF!'\n"
              f"   |      \\|\n"
              f"   | \n"
              f"   | \n")

    elif vidas == 2:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (͡°͜ʖ͡°)  'Estoy jodido xD'\n"
              f"   |      \\|/\n"
              f"   | \n"
              f"   | \n")

    elif vidas == 1:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (͡°͜ʖ͡°)  'GG FF 15'\n"
              f"   |      \\|/\n"
              f"   |       |\n"
              f"   |      /\n"
              f"   | \n"
              f"   | \n")

    else:
        print(f"\n    _______\n"
              f"   |/      |\n"
              f"   |      (✖╭╮✖)  '...'\n"
              f"   |      \\|/\n"
              f"   |       |\n"
              f"   |      / \\\n"
              f"   |  C A G A S T E\n"
              f"   | \n")


def dibujar_victoria():
    """Imprime que el jugador ha ganado"""
    print(f"\n━━━━-╮\n"
          f"╰┃  ┣▇━▇\n"
          f"  ┃  ┃  ╰━▅╮\n"
          f"  ╰┳╯  ╰━━┳╯F A L I S I T O\n"
          f"    ╰╮  ┳━━╯ F A L I S I T O\n"
          f"   ▕▔▋  ╰╮╭━╮F A L I S I T O\n"
          f"╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n"
          f"▏   ▔▔▔▔▔▔  O  O┃\n"
          f"╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n"
          f" ▏╳▕▇▇▕  ▏╳▕▇▇▕\n"
          f" ╲▂╱╲▂╱ ╲▂╱╲▂\n")


def iniciar_juego():
    """Bloque de codigo donde se realizan todas las llamadas"""
    print("\nJUEGO DEL AHORCADO 2.0 (version Kalamity)")
    print("¡Hola! Te presento a Pablo Cabeza\n")
    print("  (͡°͜ʖ͡°)\n"
          "  \\|/\n"
          "   |\n"
          "  / \\\n")
    print("El mamagüebo está siendo perseguido por sus troleadas en la Grieta del Invocador\n"
          "¡Ayuda a Pablo a escapar de la justicia de RITO, en esta emocionante aventura!")
    input(">> pulsa cualquier tecla para continuar <<")
    limpiar_consola()

    print("\nREGISTRAR JUGADOR")
    vidas = 6
    intentos = 0
    penalizacion = False
    print("Antes de comenzar, Pablo necesita conocerte para confiar en ti")
    jugador = input("Dime tu nombre: ").upper()
    # Bucle de comprobación del input, hasta que lo escriba bien
    while not es_valido_nombre(jugador):
        jugador = input("Dime tu nombre: ").upper()
    limpiar_consola()

    print("\nCOMIENZA LA PARTIDA")
    print(f"Bien, {jugador}. Para liberar a Pablo de su condena, deberás adivinar la palabra secreta que contiene el "
          f"código de la llave\n"
          f"¡Me tendrás que decir letras al azar! (╯°o°）╯")
    input(">> pulsa cualquier tecla para continuar <<")
    letras_reveladas = set()
    letras_incorrectas = set()
    limpiar_consola()

    # Se genera categoria, palabra y pista, en ese orden
    generador_azar = elegir_palabra()
    categoria = generador_azar[0].upper()
    palabra_secreta = generador_azar[1]
    pista = generador_azar[2].upper()
    pista_activada = False

    while vidas > 0:
        if not es_completada(palabra_secreta, letras_reveladas):
            limpiar_consola()

            # Si la pista esta activada y ha saltado la penalizacion, se informa
            print(f"\nSIGUE DESCIFRANDO")
            if pista_activada:
                if penalizacion:
                    print(f"¡Te han pillado usando scripts! ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿) y ahora a Pablo "
                          f"le quedan {vidas} vidas")
                    penalizacion = False
                else:
                    print(f"Los monos de RITO no se enteran del hackeo... a Pablo (ᵔᴥᵔ) "
                          f"le siguen quedando {vidas} vidas")
                pista_activada = False
            else:
                print(f"¡Adivina! A Pablo le quedan {vidas} vidas")
                print(f"Puedes utilizar scripts para ayudar a Pablo, escribe (?)")
            mostrar_incorrectas(letras_incorrectas)
            print(f"... en el llavero pone {categoria} ¯\\_(ツ)_/¯")
            dibujar_muñeco(vidas)
            mostrar_guiones(palabra_secreta, letras_reveladas)

            # Pasamos a los inputs del usuario
            entrada = (input(f"Dime una letra, {jugador} (escribe algo): ")).lower()
            # Comando especial, para activar la pista
            if entrada == "?":
                # ¿Confirmacion?
                confirmacion = (input(f"¡Advertencia! Si usas la pista, Pablo puede perder vida (y/n) ")).lower()
                if confirmacion in ("y", "yes", "si", "s", "aceptar", "ok", "accept"):
                    # Si la pista esta activada, se muestra una vez
                    pista_activada = True
                    print(f"[Hackeo temporal] ╰( ⁰ ਊ ⁰ )━☆ﾟ.*･｡ﾟ ¡Corre insensato! La pista es {pista}")
                    input(">> pulsa cualquier tecla para continuar <<")
                    # Puede o no, saltar una penalizacion
                    penalizacion = choice([True, False])
                    if penalizacion:
                        vidas -= 1

            else:
                # Bucle de comprobación del input, hasta que lo escriba bien
                while not es_valida_letra(entrada):
                    entrada = input(f"\nDime una letra {jugador}: ").lower()

                else:
                    if esta_en_palabra(entrada, palabra_secreta):
                        # En la siguiente interaccion se mostrarán los guiones
                        letras_reveladas.add(entrada)
                    else:
                        # Evitar que si repite una fallada se le vuelva a quitar vida
                        if entrada not in letras_incorrectas:
                            letras_incorrectas.add(entrada)
                            vidas -= 1
            intentos += 1

        else:
            limpiar_consola()
            dibujar_victoria()
            print("\nFIN DE LA PARTIDA")
            print(f"¡Enhorabuena {jugador}, has salvado a Pablo Cabeza!"
                  f"\nLa palabra secreta coincide con '{palabra_secreta.upper()}'"
                  f"\n  >> Conseguido en {intentos} ejecuciones <<")
            break
    else:
        limpiar_consola()
        if penalizacion:
            print(f"\n¡Te han pillado usando scripts! ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿) y ahora a Pablo "
                  f"le quedan {vidas} vidas")
        dibujar_muñeco(vidas)
        print("\nFIN DE LA PARTIDA")
        print(f"¡Oh no! {jugador}, han funado a Pablo Cabeza ૮(˶╥︿╥)ა"
              f"\nLa palabra era '{palabra_secreta.upper()}'")


iniciar_juego()
