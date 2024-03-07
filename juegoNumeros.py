import random
import time
from os import system

points = 0
totalPoints = 0

class character:
    def __init__(self, points, totalPoints, mistakes, totalMistakes, blitzPoints, blitzTotalPoints, blitzMistakes, blitzTotalMistakes):
        self.points = points
        self.totalPoints = totalPoints
        self.mistakes = mistakes
        self.totalMistakes = totalMistakes
        self.blitzPoints = blitzPoints
        self.blitzTotalPoints = blitzTotalPoints
        self.blitzMistakes = blitzMistakes
        self.blitzTotalMistakes = blitzTotalMistakes

        totalPoints = totalPoints + points
        blitzTotalPoints = blitzTotalPoints + blitzPoints


class items:    
    def __init__(self, ):
        pass



# Estadísticas iniciales personaje
player = character(0, 0, 0, 0, 0, 0, 0, 0)
# Barra de progresión
progreso = 0
barra_ancho = 3
barra_intentos = 3

def imprimir_progreso():
    global progreso, barra_ancho, barra_intentos
    barra = "[" + "█" * progreso + " " * (barra_ancho - progreso) + "]"
    print(f"\033[1mIntentos: {barra} {totalTrys}/{barra_intentos}\033[0m") 

def barra_progreso(intentos):
    global progreso, barra_ancho
    pass

intentos = 999
barra_progreso(intentos)

progressionList = ["??? - 10 puntos", "??? - 20 puntos", "??? - 50 puntos", "??? - 75 puntos", "??? - 100 puntos"]

# Puntos necesarios para aumentar el nivel de progresión
pointsFirstProgressionLevel = 10
pointsSecondProgressionLevel = 20
pointsThirdProgressionLevel = 50
pointsFourthProgressionLevel = 75
pointsFifthProgressionLevel = 100

def progression():
    global barra_ancho
    global barra_intentos
    if player.points == 105:
        print("-----------------x x x x x x-----------------")
        print("\033[35m\033[1m\033[7mHAS COMPLETADO EL ÚLTIMO NIVEL DE DIFICULTAD\033[0m")
        print("-----------------x x x x x x-----------------\n")
    if player.points == pointsFifthProgressionLevel:
        progressionList[4] = "Maestro"
        print("--------------------------- xxxxx ---------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL QUINTO NIVEL DE PROGRESIÓN\033[0m")
        print("--------------------------- xxxxx ---------------------------\n")
        print("\033[1m\033[4mMejoras del códice\033[0m\033[1m:\n\nLímite superior de números: de 10 a 50 ⬆️\033[0m\n​")
    if player.points == pointsFourthProgressionLevel:
        progressionList[3] = "Experto"
        print("---------------------------- xxxx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL CUARTO NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xxxx ----------------------------\n")
        print("\033[1m\033[4mMejoras del códice\033[0m\033[1m:\n\nLímite superior de números: de 10 a 40 ⬆️\nLímite de intentos aumentado: de 6 a 7 ⬆️\033[0m\n​")
        barra_ancho = 7
        barra_intentos = 7
    if player.points == pointsThirdProgressionLevel:
        progressionList[2] = "Avanzado"
        print("---------------------------- xxx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL TERCER NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xxx ----------------------------\n")
        print("\033[1m\033[4mMejoras del códice\033[0m\033[1m:\n\nLímite superior de números: de 10 a 30 ⬆️\nLímite de intentos aumentado: de 5 a 6 ⬆️\033[0m\n​")
        barra_ancho = 6
        barra_intentos = 6
    if player.points == pointsSecondProgressionLevel:
        progressionList[1] = "Experimentado"
        print("---------------------------- xx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL SEGUNDO NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xx ----------------------------\n")
        print("\033[1m\033[4mMejoras del códice\033[0m\033[1m:\n\nLímite superior de números: de 10 a 20 ⬆️\nLímite de intentos aumentado: de 4 a 5 ⬆️\033[0m\n​")
        barra_ancho = 5
        barra_intentos = 5
    if player.points == pointsFirstProgressionLevel:
        progressionList[0] = "Principiante"
        print("----------------------------- x -----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL PRIMER NIVEL DE PROGRESIÓN\033[0m")
        print("----------------------------- x -----------------------------\n")
        print("\033[1m\033[4mMejoras del códice\033[0m\033[1m:\n\nLímite superior de números: de 10 a 15 ⬆️\nLímite de intentos aumentado: de 3 a 4 ⬆️\033[0m\n​")
        barra_ancho = 4
        barra_intentos = 4

def progressionRemaining():
    print(pointsFirstProgressionLevel - player.points)

print("\n\n\033[1mBienvenido a \033[4m\033[33mTheNumberGame\033[0m\033[1m, puedes jugar al \033[36mmodo clásico\033[0m\033[1m, o al \033[35mmodo Blitz\033[0m\033[1m, en el clásico deberás ir adivinando números sin restricción de tiempo, aumentando poco a poco la dificultad y desbloqueando los niveles de progresión, mientras que en el modo Blitz tendrás que adivinar los máximos números posibles en 30 segundos para obtener una puntuación final e ir batiendo tu propio record\033[0m\n\n")
while True:
    print("\033[1m\033[36m1. Adivinar un número\033[0m\033[1m\n2. Estadísticas\n3. Progresión\n4. \033[35mModo Blitz\033[35m\033[0m")

    print("\n\033[1mPara volver al menú principal, escribe el número ' 0 ' en cualquier momento\033[0m")

    # Numeros iniciales al subir nivel de progresión
    secretNumber =  random.randint(1,10)
    if progressionList[0] == "Principiante" or progressionList[0] == "\033[32mPrincipiante\033[0m":
        secretNumber = random.randint(1,15)
    if progressionList[1] == "Experimentado" or progressionList[1] == "\033[32mExperimentado\033[0m":
        secretNumber = random.randint(1,20)
    if progressionList[2] == "Avanzado" or progressionList[2] == "\033[32mAvanzado\033[0m":
        secretNumber = random.randint(1,30)
    if progressionList[3] == "Experto" or progressionList[3] == "\033[32mExperto\033[0m":
        secretNumber = random.randint(1,40)
    if progressionList[4] == "Maestro" or progressionList[4] == "\033[32mMaestro\033[0m":
        secretNumber = random.randint(1,50)

    trys = 0
    totalTrys = 0
    
    while True:
        try:
            menuOption = int(input("\nEscoge una opción: "))
            system("cls")
            if menuOption not in [1, 2, 3, 4]:
                raise ValueError("Opción inválida")
            break
        except ValueError:
            system("cls")
            print("\033[1m\033[31mElige una opción correcta\033[0m\n")
            print("\033[1m\033[36m1. Adivinar un número\033[0m\033[1m\n2. Estadísticas\n3. Progresión\n4. \033[35mModo Blitz\033[35m\033[0m")

    while True:
        if menuOption == 1:

            if progressionList[4] == "Maestro" or progressionList[4] == "\033[32mMaestro\033[0m":                                        # Nivel maestro
                if totalTrys == 7:
                    secretNumber = random.randint(1,50)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-50)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == 105:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            pass
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,50)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 7:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 7:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break

            elif progressionList[3] == "Experto" or progressionList[3] == "\033[32mExperto\033[0m":                                        # Nivel experto
                if totalTrys == 7:
                    secretNumber = random.randint(1,40)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-40)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == pointsFifthProgressionLevel:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            secretNumber = random.randint(1,50)
                            break
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,40)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 7:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 7:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break

            elif progressionList[2] == "Avanzado" or progressionList[2] == "\033[32mAvanzado\033[0m":                                        # Nivel avanzado
                if totalTrys == 6:
                    secretNumber = random.randint(1,30)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-30)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == pointsFourthProgressionLevel:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            secretNumber = random.randint(1,40)
                            break
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,30)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 6:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 6:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break
            
            elif progressionList[1] == "Experimentado" or progressionList[1] == "\033[32mExperimentado\033[0m":                                   # Nivel experimentado
                if totalTrys == 5:
                    secretNumber = random.randint(1,20)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-20)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == pointsThirdProgressionLevel:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            secretNumber = random.randint(1,30)
                            break
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,20)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 5:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 5:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break
            
            elif progressionList[0] == "Principiante" or progressionList[0] == "\033[32mPrincipiante\033[0m":                                       # Nivel principiante
                if totalTrys == 4:
                    secretNumber = random.randint(1,15)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-15)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == pointsSecondProgressionLevel:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            secretNumber = random.randint(1,20)
                            break
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,15)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 4:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso+=1
                        if totalTrys == 4:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break

            elif progressionList[0] != "Principiante":                                         # Nivel inicial
                if totalTrys == 3:
                    secretNumber = random.randint(1,10)
                    totalTrys = 0
                else:
                    while True:
                        try:
                            myNumber = int(input("\n\033[36mIntroduce tu número (1-10)\033[0m: "))
                            break
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                    system("cls")
                    if myNumber == secretNumber:
                        player.points += 1
                        if player.points == pointsFirstProgressionLevel:
                            progression()
                            totalTrys = 0
                            progreso = 0
                            secretNumber = random.randint(1,15)
                            break
                        else:
                            print("-------- x --------")
                            print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                            print("-------- x --------")
                            secretNumber = random.randint(1,10)
                            print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                            # Reinicio de los intentos si haciertas
                            totalTrys = 0
                            # Reinicio de la barra de progresión
                            progreso = 0
                            continue
                    if myNumber < secretNumber:
                        totalTrys += 1
                        progreso += 1
                        if totalTrys == 3:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                    if myNumber > secretNumber:
                        totalTrys += 1
                        progreso +=1
                        if totalTrys == 3:
                            player.totalMistakes += 1
                            print("\n--------- x --------")
                            print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                            print("--------- x --------\n")
                            progreso = 0
                            break
                        else:
                            imprimir_progreso()
                            print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                    if myNumber == 00:
                        progreso = 0
                        system("cls")
                        break

        if menuOption == 2:
            system("cls")
            print("-------------------------- x --------------------------\n")
            print (f"\033[1mHas adivinado un total de: \033[32m{player.points} números\033[0m\033[1m en el modo clásico\033[0m")
            print (f"\033[1mHas fallado un total de: \033[31m{player.totalMistakes} números\033[0m\033[1m en el modo clásico")
            print("\n-------------------------- x --------------------------\n\n")
            break
        if menuOption == 3:
            system("cls")
            if progressionList[0] == "Principiante":
                progressionList[0] = "\033[32mPrincipiante\033[0m"
            if progressionList[1] == "Experimentado":
                progressionList[1] = "\033[32mExperimentado\033[0m"
            if progressionList[2] == "Avanzado":
                progressionList[2] = "\033[32mAvanzado\033[0m"
            if progressionList[3] == "Experto":
                progressionList[3] = "\033[32mExperto\033[0m"
            if progressionList[4] == "Maestro":
                progressionList[4] = "\033[32mMaestro\033[0m"
            else:
                print("---------------- x ----------------\n")
                print("\033[1m\033[33mCamino de progresión:\033[0m\n")
                for progress in progressionList:
                    print(f"\033[1m\033[31m{progress}\033[0m")
                print("\n---------------- x ----------------\n\n")
                break

        if menuOption == 4:                                                                      # Modo de juego Blitz
            system("cls")
            print("\n\033[1m\033[35mModo Blitz\033[0m\033[1m: Tienes \033[33m30 segundos\033[0m\033[1m para adivinar la mayor cantidad de números posibles, estos números \033[33mse sitúan del 1-10 y tienes 3 intentos\033[0m\033[1m. Cada número descubierto son 2 puntos y cada número no descubierto resta 1 punto. Tu objetivo es lograr conseguir la mayor cantidad de puntos\033[0m\n")
            menuOption = input("\033[1mPresiona \033[4mENTER\033[0m\033[1m para comenzar la partida\033[0m")
            system("cls")
            print("\033[1mTemporizador iniciado, tienes 30 segundos...\033[0m\n")
            secretNumber = random.randint(1,10)
            totalTrys = 0

            # Inicio del temporizador
            duracion_bucle = 30
            inicio_bucle = time.time()

            myNumber = None

            while time.time() - inicio_bucle < duracion_bucle:
                try:
                    myNumber = int(input("\n\033[36mIntroduce tu número (1-10)\033[0m: "))
                except ValueError:
                    print("\033[1mPor favor, introduce un número válido\033[0m")

                if myNumber is not None:
                    if myNumber == secretNumber:
                        player.blitzPoints += 1
                        totalTrys = 0
                        progreso = 0
                        secretNumber = random.randint(1,10)
                        system("cls")
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto ✅\033[0m")
                        print("-------- x --------")
                        print("\n\033[33m\033[1mNuevo número oculto generado...\033[0m\n")
                        continue

                    if myNumber < secretNumber:
                        system("cls")
                        print("\033[33m\033[1m\nEl número oculto es más grande\n\033[0m")
                    else:
                        system("cls")
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\n\033[0m")
                    
                    progreso += 1
                    totalTrys += 1
                    imprimir_progreso()

                    if totalTrys == 3:
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado ❌\033[0m")
                        print("--------- x --------\n")
                        totalTrys = 0 
                        secretNumber = random.randint(1, 10)
                        player.blitzTotalMistakes += 1
                        progreso = 0

                    if myNumber == 00:
                        progreso = 0
                        totalTrys = 0
                        system("cls")
                        break

            # Fin del temporizador
            time.sleep(2)
            progreso = 0
            system("cls")
            print("\n\033[1mJUEGO FINALIZADO, CARGANDO ESTADÍSTICAS... NO PRESIONES NINGUNA TECLA...\033[0m\n")

            duracion_bucle = 2
            inicio_bucle = time.time()
            time.sleep(4)

            system("cls")
            print(f"\033[1mHas adivinado un total de: \033[32m\033[4m{player.blitzPoints} números\033[0m\033[1m, con un total de: \033[32m\033[4m{player.blitzPoints * 2} puntos\n\033[0m")
            print(f"\033[1mHas fallado un total de: \033[31m\033[4m{player.blitzTotalMistakes} números\033[0m\033[1m, con un total de: \033[31m\033[4m{player.blitzTotalMistakes * 1} puntos\n\033[0m")
            print(f"\033[1mTu resultado final es de: \033[35m\033[4m{(player.blitzPoints * 2) - player.blitzTotalMistakes * 1} puntos\033[0m")
            input("\n\n\033[1mPresiona ENTER para continuar... \033[0m")
            system("cls")
            break
