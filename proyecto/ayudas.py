def opcionesList(a):
    opciones = []
    if a == 1:
        opciones = ["BREAKING BAD","SQUID GAME","GAME OF THRONES","PRISON BREAK","LUCIFER","DARK","YOU","WHAT IF",
                    "THE WALKING DEAD","WANDAVISION","RICK AND MORTY","LOKI","ONE PIECE","RIVERDALE","BLACK MIRROR",
                    "THE SIMPSONS","STRANGER THINGS","GREYS ANATOMY"] #Lista con series
    elif a == 2:
        opciones = ["AVENGERS INFINITY WAR","JUSTICE LEAGUE","SPACE JAM","BRIGHTBURN","VENOM","SPIDER MAN","HARRY POTTER",
                    "SUPERMAN","AQUAMAN","TITANIC","THE DARK KNIGHT","WONDER WOMAN","TRANSFORMERS","THE HOBBIT","RESIDENT EVIL",
                    "BLACK WIDOW","STAR WARS"] #Lista con películas
    elif a == 3:
        opciones = ["PROGRAMACIÓN","CÁLCULO DE UNA VARIABLE","MATEMÁTICAS DISCRETAS","CÁLCULO VECTORIAL","ÁLGEBRA LINEAL",
                    "ECUACIONES DIFERENCIALES","ÓPTICAS Y ONDAS","LABORATORIO DE COMUNICACIÓN","ESTADÍSTICA Y PROBABILIDADES",
                    "DESARROLLO BASADO EN PLATAFORMAS","BASE DE DATOS","PROYECTO INTERDISCIPLINARIO","MÉTODOS NUMÉRICOS",
                    "ALGORITMOS Y ESTRUTURAS DE DATOS","ARQUITECTURA DE COMPUTADORAS","CLOUD COMPUTING","EMPRESA Y CONSUMIDOR",
                    "COMPILADORES","ANÁLISIS Y DISEÑO DE ALGORITMOS","INGENIERÍA DE SOFTWARE","MACHINE LEARNING",
                    "SISTEMAS OPERATIVOS","FINANZAS EMPRESARIALES","COMPUTACIÓN PARALELA Y DISTRIBUIDA","COMPUTACIÓN GRÁFICA",
                    "INTERACCIÓN HUMANO COMPUTADOR","REDES Y COMUNICACIONES","INVESTIGACIÓN EN COMPUTACIÓN","ARTE Y TECNOLOGIA",
                    "INTERNET DE LAS COSAS","ÉTICA Y TECNOLOGÍA","EVALUACIÓN FINANCIERA DE PROYECTOS","ESTRATEGIA Y ORGANIZACIONES"] #Lista de cursos CS
    return opciones
def hangdraw(intento):
    if intento == 0:
        print(" ________________")  #Todo esto sirve para dibujar la horca mientras que los intentos fallidos se incrementan
        print("|____            |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 1:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 2:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|    |           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 3:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 4:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 5:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   /            |")
        print("|                |")
        print("|________________|")
    elif intento == 6:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   / \          |")
        print("|                |")
        print("|________________|")