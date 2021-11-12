import random
import os
from ayudas import *
def inicio(): #Esto es la pantalla de inicio
    print("  **** UTEC GAMES ****  ")
    print("")
    print("[1] Juego del ahorcado")
    print("[2] Otros juegos")
    print("[3] Salir")
    print("")
    opcion = input("Ingrese una opción : ")
    while opcion not in ["1","2","3"]: #Esto es para que se elija una opción del 1 al 3 o sino se vuelve a pedir el input
        opcion = input("Elija una opción válida : ")
    if opcion == "1":
        os.system("cls")
        ahorcado() #Se va a la función ahorcado
    elif opcion == "2":
        os.system("cls")
        inicio() #Como no hay otro juego, se vuelve a la pantalla de inicio
    elif opcion == "3":
        os.system("cls")
        print("Cerrando UTEC GAMES...")

def ahorcado(): #Acá se va a una pantalla principal para esta función
    print(" **** El Ahorcado *** ")
    print("")
    print("Seleccione una categoria")
    print("")
    print("[1] Series")
    print("[2] Peliculas")
    print("[3] Cursos de CS")
    print("[4] Regresar")
    print("")
    opthang = input("Selecciones una opción : ")
    while opthang not in ["1","2","3","4"]: #Esto es para que se elija una opcion entre 1 a 4
        opthang = input("Elija una opción válida : ")
    os.system("cls")
    ahorcar(int(opthang)) #Elegido una opción válida, se va a la función ahorcar
def ahorcar(a):
    categoria = ""
    opciones = [] #La opciones van a estar en mayúscula para que sea mas facil enlazar con las letras que vamos a adivinar
    run = False
    if a == 1: #Si la variable opthang de la función anterior fue 1, se coge esta opción. Lo mismo con los otros
        opciones = opcionesList(a) #Con esta función, se llama a las lista de opciones de la categoría correspondiente
        categoria = "Series"
        run = True
    elif a == 2:
        opciones = opcionesList(a)
        categoria = "Películas"
        run = True
    elif a == 3:
        opciones = opcionesList(a)
        categoria = "Cursos de CS"
        run = True #Esto es para que mientras esto sea True, corra el juego
    elif a == 4:
        run = False #Acá el run no va a correr el juego
        inicio() #Si se elige opthang = 4, entonces se vuelve a la pantalla de inicio
    if run == True: #Lo que pasa cuando Run = True
        eleccion = opciones[random.randint(0,len(opciones)-1)] #Acá se elige una opción de la designada lista al azar
        encontrar = "" # Acá se va a tener los espacios a adivinar para el juego, ejemplo de esto --> _____ ____
        long = len(eleccion) #Acá se tiene la longitud de la palabra a eliminar
        for i in eleccion:
            if i == " ":
                encontrar += " " #Si en la variable eleccion (Palabra a adivinar), el espacio esta constituido con un espacio, se va a agregar
            else:                #a la variable encontrar un espacio en blanco
                encontrar += "_" #Si eleccion tiene en un espacio una letra, se va a agregar en encontrar una _
        intento = 0
        error = "Errores: " #Acá se tienen los errores próximos
        while intento != 6: #Mientras que el número de intentos no exceda el límite de 6, se activa este código
            print(" **** El Ahorcado *** ")
            print("")
            print("Categoría seleccionada:",categoria)
            print("")
            hangdraw(intento) #Todo esto imprime el espacio que se va a tener al momento de jugar
            print("")
            print(encontrar[0:long])
            print("")
            print(error) #Esto imprime los errores
            print("")
            guess = input("Ingrese una letra: ") #Acá se va a empezar a adivinar las letras
            while len(guess) > 1: #Si se escribe más de un valor, se vuelve a preguntar guess
                guess = input("Ingrese una sola letra: ")

            lista = [] #Acá se va a poner cada espacio o letra de la variable elección en una lista por separado.
                       # Eleccion = hola, lista = ["h","o","l","a"]
            if guess.upper() in eleccion: #Todo lo que escribamos en guess va a ser convertido en mayúscula ya que en las lista,
                                          #los elementos estan en mayuscula
                for pos, chr in enumerate(eleccion):
                    if (chr == guess.upper()):
                        lista.append(pos) # Esta parte del código sirve para que cada vez que pongamos una letra en el guess, esta se llene
                                          # en los espacios a adivinar (ejem. _____ ____)
                for i in lista:
                    encontrar = list(encontrar) #Esta convierte los espacios de encontrar en una lista
                    encontrar[i] = eleccion[i] # Esto compara las posiciones de encontrar y las iguala a las posiciones de la lista en eleccion
                    encontrar = "".join(encontrar)
                    encontrar = encontrar[0:long]
                    #Todo se pasó a lista porque si se trabajo con string, por ejemplo si varios espacios son _, aunque queramos cambiar
                    #una posición en concreto, todos los que tengan ese mismo valor se cambiaran (ejemplo. guess = A, _____ ____ ---> AAAAA AAAA)
            elif guess.upper() not in eleccion:
                error = error+"["+guess.upper()+"]"+" " # Esto sirve para poner los errores en la variable error, con cada letra en el guess que fallemos
                intento += 1 #Se incrementan los intentos que sirve para los dibujos de la función hangdraw

            if encontrar == eleccion:
                print("Felicidades, la palabra era",eleccion)   #Cuando se alcanza la palabra, nos recibe un mensaje de felicitación
                print(input("Escriba cualquier cosa para salir --> ")) #Esto es para que escribas cualquier cosa para continuar
                break #Este break es necesario ya que si no lo ponemos, cuando tratemos se cerrar el juego, en el terminal saldrá error o seguirá
                      #con el juego
            elif encontrar != eleccion and intento == 6:
                print("Lo siento, la palabra era",eleccion)     #Este mensaje sale si se acaban los intentos
                print(input("Escriba cualquier cosa para salir --> "))
                break #Este break es igual de importante que el anterior
            os.system("cls")
        os.system("cls")
        ahorcado() #Todo se rompe y vuelve a la pantalla principal de la función ahorcado

inicio() #Esto es para que todo se inicie