# Importamos lo siguiente:
import os # Librería utilizada para limpiar la consola.
import random # Importamos la librería random para escoger valores aleatorios.
from funciones_1 import * # Importamos la función 'ahorcado' del módulo 'funciones_1.py'.

def inicio():
    """
    Esta función sin parámetros imprime el menú principal de **** UTEC GAMES ****. 
    """
    print("  **** UTEC GAMES ****  ")
    print("")
    print("[1] Juego del ahorcado")
    print("[2] Otros juegos")
    print("[3] Salir")
    print("")
    opcion = input("Ingrese una opción : ")
    
    # El siguiente bucle while repite el input hasta que la variable 'opcion' este dentro de la lista ["1","2","3"].

    while opcion not in ["1","2","3"]: 
        opcion = input("Elija una opción válida : ")

    # La siguiente estructura selectiva es para que deacuerdo al valor de 'opcion' vincule a otra determinada función. 

    if opcion == "1":
        os.system("cls") # Limpia la consola.
        # Se va a la función ahorcado, que previamente ha sido importada de 'funciones.py'.
        ahorcado() 

    elif opcion == "2":
        os.system("cls") # Limpia la consola.
        # Como no hay otro juego, se vuelve al menú de principal (recursividad).
        inicio()

    elif opcion == "3":
        os.system("cls") # Limpia la consola
        # Finaliza el programa.
        print("Cerrando UTEC GAMES...") 

def ahorcado(): 
    """
    Esta función sin parámetros imprime el menú del juego **** El Ahorcado ***.
    """
    print(" **** El Ahorcado *** ")
    print("")
    print("Seleccione una categoria")
    print("")
    print("[1] Series")
    print("[2] Peliculas")
    print("[3] Cursos de CS")
    print("[4] Regresar")
    print("")
    opthang = input("Seleccione una opción : ")

    # Este bucle while repite el input hasta que la variable 'opthang' este dentro de la lista ["1","2","3","4"].
    while opthang not in ["1","2","3","4"]:
        opthang = input("Elija una opción válida : ")

    # Limpia la consola.
    os.system("cls") 
    
    # Luego de elegir una opción válida, se ejecuta la función 'ahorcar(a)'.
    ahorcar(int(opthang))

# a = int(opthang)
def ahorcar(a):
    """
    Esta función recibe un parámetro entero 'a' y se encarga de ejecutar el código para que funcione el juego
    **** El Ahorcado *** dependiendo el valor de a.
    """
    # Definimos 'categoria' como una cadena vacía. 
    # Posteriormente se sobreescribirá por "Series", "Películas" o "Cursos de CS" según corresponada el valor 
    # de 'a'. 
    categoria = ""

    # Definimos 'run' como un valor booleano, que nos va permitir correr el juego o no. 
    run = False

    # -------------------------------------------------------------------------------------------------------------
    # ---------------------VALIDACIÓN DE LAS OPCIONES DEL MENÚ DEL JUEGO **** El Ahorcado ***.---------------------
    # -------------------------------------------------------------------------------------------------------------

    # La siguiente estructura selectiva es para que deacuerdo al valor de 'a' ejecute un determinado código.
    # 'a' puede ser 1,2,3 o 4
    
    if a == 1:

        # Definimos 'opciones'
        # Llamamos a la función opcionesList del apartado "funciones_1.py" para obtener la lista.
        opciones = opcionesList(a)
        
        # Se sobreescribe 'categoria' por lo siguiente.
        categoria = "Series"

        # Se sobreescribe 'run' por 'True' para correr el juego.
        run = True
    
    elif a == 2:

        # Definimos 'opciones'
        # Llamamos a la función opcionesList del apartado "funciones_1.py" para obtener la lista.
        opciones = opcionesList(a)
        
        # Se sobreescribe 'categoria' por lo siguiente.
        categoria = "Películas"
        
        # Se sobreescribe 'run' por 'True' para correr el juego.
        run = True

    elif a == 3:

        # Definimos 'opciones'
        # Llamamos a la función opcionesList del apartado "funciones_1.py" para obtener la lista.
        opciones = opcionesList(a)
        
        # Se sobreescribe 'categoria' por lo siguiente.
        categoria = "Cursos de CS"

        # Se sobreescribe 'run' por 'True' para correr el juego.
        run = True 
    
    elif a == 4:

        # Si a = 4, entonces regresamos al menú principal de **** UTEC GAMES ****.
        # No se sobreescribe 'run' para no correr el juego.
        run = False
        
        # Se regresa al menú principal de **** UTEC GAMES ****.
        inicio()

    # -------------------------------------------------------------------------------------------------------------    
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    

    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------EJECUCIÓN DEL JUEGO **** El Ahorcado ***.-------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    
    # Si 'run' es igual a True se ejecuta lo siguiente.

    if run == True:

        # Definimos 'eleccion' que almacena un string.
        # Se elige una 'opción' (str) de la designada lista 'opciones' al azar.
        # Esa 'opcion' se guarda en la variable 'eleccion'.
        # 'eleccion' es lo que va a tener que adivinar el usuario.
        eleccion = opciones[random.randint(0,len(opciones)-1)] 

        # Definimos 'encontrar' como una cadena vacía.
        # Se va a tener los espacios a adivinar para el juego, ejemplo de esto --> _____ ____
        encontrar = "" 
        
        # Se almacena en 'long' la longitud de la palabra a encontrar
        long = len(eleccion) 

        # Interamos la cadena 'eleccion'
        for i in eleccion:
            if i == " ":
                # Si en la cadena 'eleccion' (palabra a adivinar), el caracter esta constituido por un espacio, 
                # entonces se va a agregar a la cadena 'encontrar' un espacio en blanco.
                encontrar += " " 
            else:
                # Si en la cadena 'eleccion' (palabra a adivinar), el caracter es una letra, entonces se va
                # a agregar a la cadena 'encontrar' un _.               
                encontrar += "_" 

        # Lo siguiente es un bucle while para correr el juego mientras 'intento' no exeda a 6.
        intento = 0
        error = "Errores: " # Acá almacenaran los errores próximos en caso de fallar intentos.
        while intento <= 6:

            # Se imprime el siguiente código que irá cambiando según el intento.
            print(" **** El Ahorcado *** ")
            print("")
            print("Categoría seleccionada:",categoria)
            print("")
            hangdraw(intento) # Esta función dibuja la horca que se va a tener al momento de jugar en consola.
            print("")
            print(encontrar[0:long]) # Imprime los espacios a de la palabra a adivinar, puede ir variando.
            print("")
            print(error) # Esto imprime los errores del usuario ([letra]), puede ir variando.
            print("")

            # Se va almacenar en 'guess' la letra que el usuario ingrese para adivinar la palabra.
            guess = input("Ingrese una letra: ") 
            
            # Si se escribe más de un valor, se vuelve a preguntar 'guess'.
            while len(guess) > 1: 
                guess = input("Ingrese una sola letra: ")
            
            # Definimos 'lista' donde se va a poner cada espacio o letra de la variable 'eleccion' en una lista por separado.
            # Ejemplo: eleccion = hola --> lista = ["h","o","l","a"]
            lista = [] 

            # Todo lo que escribamos en 'guess' va a ser convertido en mayúscula ya que en 'lista', todos los
            # elementos son en mayúscula.
            # Recorremos 'eleccion' para comprobar si la letra insertada por el usuario esta en dicha lista.
            if guess.upper() in eleccion:

                # El siguiente bucle for sirve para recorrer 'eleccion' e ir obteniendo la pocisión 'pos' y elemento respectivo 'chr'.                  
                for pos, chr in enumerate(eleccion):
                    
                    # Esta parte del código sirve para que cada vez que pongamos una letra en el 'guess', esta se llene
                    # en los espacios a adivinar (Ejem: _____ ____)
                    if (chr == guess.upper()):
                        lista.append(pos) 

                # El siguiente bucle for sirve para recorrer 'lista' e ir obteniendo el elemento 'i'.                      
                for i in lista:
                    encontrar = list(encontrar) # Esto convierte los espacios de 'encontrar' en una lista.
                    encontrar[i] = eleccion[i] # Esto iguala los valores de 'encontrar[i]' y 'eleccion[i]'.
                    encontrar = "".join(encontrar) # Transformamos la lista 'encontrar' a un string
                    encontrar = encontrar[0:long]
                    
                    # Al principio la cadena 'encontrar' se pasó a lista para facilitar el proceso, porque sino al trabajar 
                    # con 'str' podría darse el caso de que varios espacios '_' cambien por un carácter igual y no a un carácter
                    # en concreto deacuerdo a la posición.
                    # Ejemplo: guess = A, _____ ____ ---> encontrar = AAAAA AAAA)
            

            # En caso 'guess' no se encuentre en 'eleccion'.
            elif guess.upper() not in eleccion:

                # Esto sirve para poner los errores en la variable error, con cada letra en el guess que fallemos.
                error = error+"["+guess.upper()+"]"+" "
                # Se incrementan los intentos que sirve para los dibujos de la función hangdraw.
                intento += 1 

    # -------------------------------------------------------------------------------------------------------------    
    # -------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------


    # -------------------------------------------------------------------------------------------------------------    
    # ------------------------------PARTE FINAL DEL JUEGO  **** El Ahorcado ***.-----------------------------------
    # -------------------------------------------------------------------------------------------------------------
            
            # Comprobamos si el usuario adivinó o no la palabra e imprima el resultado.
            # 'encontrar' es lo digitado por el usuario
            # 'eleccion' es la palabra que se asigno desde un principio para adivinar
            if encontrar == eleccion:
                os.system("cls")  # Limpia la consola
                # Cuando se alcanza la palabra, nos recibe un mensaje de felicitación
                print("Felicidades, la palabra era",eleccion) 
                endingdraw(1) #Se llama a la función endingdraw para mostrar el dibujo correspondiente a nuestra victoria.
                print(input("Escriba cualquier cosa para salir --> ")) # Esto es para que escribas cualquier cosa para continuar.
                break 
                # Este break es necesario ya que si no lo ponemos nos saldrá error o seguirá con el juego, cuando tratemos de cerrar 
                # el juego en el terminal. 

            elif encontrar != eleccion and intento == 6:
                os.system("cls")  # Limpia la consola
                print("Lo siento, la palabra era",eleccion) # Este mensaje sale si se acaban los intentos.
                endingdraw(2) #Se llama a la función endingdraw para mostrar el dibujo correspondiente a nuestra derrota.
                print(input("Escriba cualquier cosa para salir --> "))
                break 
                # Este break es igual de importante que el anterior.
            
            # Limpiamos la consola
            os.system("cls")
        
        # Limpiamos la consola
        os.system("cls")
        
        # Todo se termina y se vuelve al menú principal de la función ahorcado.
        ahorcado() 

inicio() # Incializa el programa