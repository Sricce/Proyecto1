from timer import *
"""
    A continuación, se nombran las siguientes funciónes utilizadas en el proyecto.
    * hangdraw(intento)
    * opcionesList(a)
    * endingdraw(b)
"""
def hangdraw(intento):
    """
    Esta función recibe un parámetro entero 'intento' del 1 al 6 y dibuja la horca dependiendo el valor de
    'intento'
    """

    # 'intento' puede ser cualquier valor del 1 al 6 y va aumentando según el usuario fallé al insertar
    # una letra en el 'guees'.
    if intento == 0:
        print('Vidas : 6 | ❤ ❤ ❤ ❤ ❤ ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 1:
        print('Vidas : 5 | ❤ ❤ ❤ ❤ ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 2:
        print('Vidas : 4 | ❤ ❤ ❤ ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|    |           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 3:
        print('Vidas : 3 | ❤ ❤ ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 4:
        print('Vidas : 2 | ❤ ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 5:
        print('Vidas : 1 | ❤')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   /            |")
        print("|                |")
        print("|________________|")
    elif intento == 6:
        print('Vidas : 0 | ☠')
        print()
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   / \          |")
        print("|                |")
        print("|________________|")

def opcionesList(a):
    """
    Esta función sirve para elegir las palabras que vamos a adivinar en el transcurso del juego, basado en la
    categoría que seleccionamos en un inicio.
    """
    # Definimos 'opciones' como una lista vacía.
    # Posteriormente se sobreescribirá dependiendo el valor de 'a'.
    # Esta lista se sobreescribirá con una lista de cadenas en mayúscula para que sea más fácil enlazar con las
    # letras que el usuario va a adivinar.
    opciones = []
    if a == 1:
        opciones = ["BREAKING BAD", "SQUID GAME", "GAME OF THRONES", "PRISON BREAK", "LUCIFER", "DARK", "YOU",
                    "WHAT IF",
                    "THE WALKING DEAD", "WANDAVISION", "RICK AND MORTY", "LOKI", "ONE PIECE", "RIVERDALE",
                    "BLACK MIRROR",
                    "THE SIMPSONS", "STRANGER THINGS", "GREYS ANATOMY"]  # Lista con series
    elif a == 2:
        opciones = ["AVENGERS INFINITY WAR", "JUSTICE LEAGUE", "SPACE JAM", "BRIGHTBURN", "VENOM", "SPIDER MAN",
                    "HARRY POTTER",
                    "SUPERMAN", "AQUAMAN", "TITANIC", "THE DARK KNIGHT", "WONDER WOMAN", "TRANSFORMERS", "THE HOBBIT",
                    "RESIDENT EVIL",
                    "BLACK WIDOW", "STAR WARS"]  # Lista con películas
    elif a == 3:
        opciones = ["PROGRAMACIÓN", "CÁLCULO DE UNA VARIABLE", "MATEMÁTICAS DISCRETAS", "CÁLCULO VECTORIAL",
                    "ÁLGEBRA LINEAL",
                    "ECUACIONES DIFERENCIALES", "ÓPTICAS Y ONDAS", "LABORATORIO DE COMUNICACIÓN",
                    "ESTADÍSTICA Y PROBABILIDADES",
                    "DESARROLLO BASADO EN PLATAFORMAS", "BASE DE DATOS", "PROYECTO INTERDISCIPLINARIO",
                    "MÉTODOS NUMÉRICOS",
                    "ALGORITMOS Y ESTRUTURAS DE DATOS", "ARQUITECTURA DE COMPUTADORAS", "CLOUD COMPUTING",
                    "EMPRESA Y CONSUMIDOR",
                    "COMPILADORES", "ANÁLISIS Y DISEÑO DE ALGORITMOS", "INGENIERÍA DE SOFTWARE", "MACHINE LEARNING",
                    "SISTEMAS OPERATIVOS", "FINANZAS EMPRESARIALES", "COMPUTACIÓN PARALELA Y DISTRIBUIDA",
                    "COMPUTACIÓN GRÁFICA",
                    "INTERACCIÓN HUMANO COMPUTADOR", "REDES Y COMUNICACIONES", "INVESTIGACIÓN EN COMPUTACIÓN",
                    "ARTE Y TECNOLOGIA",
                    "INTERNET DE LAS COSAS", "ÉTICA Y TECNOLOGÍA", "EVALUACIÓN FINANCIERA DE PROYECTOS",
                    "ESTRATEGIA Y ORGANIZACIONES"] #Lista de cursos CS
    # Finalmente, retornamos la lista opciones para seguir con el procedimiento del código
    return opciones

def endingdraw(b):
    """
    Esta función sirve para mostrar un dibujo relacionado a nuestro resultado en el juego del ahorcado.
    La primera opción es cuando ganamos y la segunda opción es cuando perdemos.
    """
    if b == 1:
        print(f"""
            ░░░░░░░░░░░▄▄
            ░░░░░░░░░░█░░█
            ░░░░░░░░░░█░░█
            ░░░░░░░░░█░░░█
            ░░░░░░░░█░░░░█
            ██████▄▄█░░░░░██████▄
            ▓▓▓▓▓█░░░░░░░░░░░░░░█
            ▓▓▓▓▓█░░░░░░░░░░░░░░█
            ▓▓▓▓▓█░░░░░░░░░░░░░░█
            ▓▓▓▓▓█░░░░░░░░░░░░░░█
            ▓▓▓▓▓█░░░░░░░░░░░░░░█
            ▓▓▓▓▓█████░░░░░░░░░█
            █████▀░░░░▀▀██████▀ 
                        """) # Cuando ganamos
    elif b == 2:
        print(f"""
            ´´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
            ´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
            ´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
            ´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
            ´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
            ´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
            ´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
            ´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
            ´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
            ´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
            ¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
            ¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
            ´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
            ´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
            ´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
            ´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
            ´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
            ´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
            ´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
            ´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
            ´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
            ´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
            ´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
                        """) # Cuando perdemos

def historiamad1(one,two,three,four,five,six,seven):
    print("**** Mad Story ***")
    print("Salvando la navidad")
    m = ["Era de noche, nevaba y hacia demasiado frio. En eso",
        "apareció un destello rojo en el cielo y escuché el",
        "sonido de una explosión en el bosque.",
        "Corrí hacia el lugar y vi a Santa Claus en el suelo, casi",
        "inconsciente. Solo atiné a decirle '{}' y a".format(one),
        "darle '{}' cachetadas hasta que reaccionó. Me contó".format(two),
        "que estaba distraído en '{}' cuando chocó con".format(seven),
        "un arbol muy alto.",
        "Su trineo estaba intacto pero sus renos estaban",
        "inconscientes. Entonces, decidí prestarle '{}' '{}'".format(five,three),
        "para poder llevar los regalos en su trineo. El aceptó",
        "gustoso, así que mientras le daba un '{}' para".format(six),
        "que coma y se recupere, fui a repartir los regalos que",
        "quedaban. Al terminar, me agradeció regalandome un",
        "'{}'. En verdad que fue una noche de locos.".format(four)]
    for i in m:
        print(i)
    input("Presione enter para continuar... ")

