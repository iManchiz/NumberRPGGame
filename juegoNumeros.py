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

def imprimir_progreso():
    global progreso, barra_ancho
    barra = "[" + "█" * progreso + " " * (barra_ancho - progreso) + "]"
    print(f"\033[1mIntentos: {barra} {totalTrys}/3\033[0m") 

def barra_progreso(intentos):
    global progreso, barra_ancho

intentos = 999
barra_progreso(intentos)

progressionList = ["??? - 10 puntos", "??? - 20 puntos", "??? - 50 puntos", "??? - 75 puntos", "??? - 100 puntos"]

pointsFirstProgressionLevel = 1
pointsSecondProgressionLevel = 2
pointsThirdProgressionLevel = 3
pointsFourthProgressionLevel = 4
pointsFifthProgressionLevel = 5

def progression():

    if player.points == pointsFifthProgressionLevel:
        progressionList[4] = "Maestro"
        print("--------------------------- xxxxx ---------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL QUINTO NIVEL DE PROGRESIÓN\033[0m")
        print("--------------------------- xxxxx ---------------------------")
        print("Mejoras del códice:\n\nLímite superior de números: de 10 a 50 ⬆️\nLímite de intentos aumentado: de 4 a 5 ⬆️​")
    if player.points == pointsFourthProgressionLevel:
        progressionList[3] = "Experto"
        print("---------------------------- xxxx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL CUARTO NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xxxx ----------------------------")
        print("Mejoras del códice:\n\nLímite superior de números: de 10 a 40 ⬆️\nLímite de intentos aumentado: de 4 a 5 ⬆️​")
    if player.points == pointsThirdProgressionLevel:
        progressionList[2] = "Avanzado"
        print("---------------------------- xxx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL TERCER NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xxx ----------------------------")
        print("Mejoras del códice:\n\nLímite superior de números: de 10 a 30 ⬆️\nLímite de intentos aumentado: de 3 a 4 ⬆️​")
    if player.points == pointsSecondProgressionLevel:
        progressionList[1] = "Experimentado"
        print("---------------------------- xx ----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL SEGUNDO NIVEL DE PROGRESIÓN\033[0m")
        print("---------------------------- xx ----------------------------")
        print("Mejoras del códice:\n\nLímite superior de números: de 10 a 20 ⬆️\nLímite de intentos aumentado: de 3 a 4 ⬆️​")
    if player.points == pointsFirstProgressionLevel:
        progressionList[0] = "Principiante"
        print("----------------------------- x -----------------------------")
        print("\033[35m\033[1m¡FELICIDADES!, HAS DESBLOQUEADO EL PRIMER NIVEL DE PROGRESIÓN\033[0m")
        print("----------------------------- x -----------------------------\n")
        print("Mejoras del códice:\n\nLímite superior de números: de 10 a 15 ⬆️​")
        
while True:
    print("\n1. Adivinar un número\n2. Estadísticas\n3. Progresión\n4. Modo Blitz")
    secretNumber = random.randint(1,10)
    trys = 0
    totalTrys = 0
    
    while True:
        try:
            menuOption = int(input("\nEscoge una opción: "))
            if menuOption not in [1, 2, 3, 4]:
                raise ValueError("Opción inválida")
            break
        except ValueError:
            system("cls")
            print("\033[1m\033[31mElige una opción correcta\033[0m\n")
            print("\n1. Adivinar un número\n2. Estadísticas\n3. Progresión")
    system("cls")

    while True:
        if menuOption == 1:

            if progressionList[4] == "Maestro":                                        # Nivel maestro
                secretNumber = random.randint(1,50)
                print(secretNumber)
                print("maestro")

                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
                        break
                    except ValueError:
                        print("Por favor, introduce un número válido.")
                system("cls")
                if myNumber == secretNumber:
                    player.points += 1
                    if player.points == 55:
                        progression()
                        totalTrys = 0
                        progreso = 0
                        pass
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,50)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 5:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 5:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break

            elif progressionList[3] == "Experto":                                        # Nivel experto
                secretNumber = random.randint(1,40)
                print(secretNumber)
                print("experto")

                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
                        break
                    except ValueError:
                        print("Por favor, introduce un número válido.")
                system("cls")
                if myNumber == secretNumber:
                    player.points += 1
                    if player.points == pointsFifthProgressionLevel:
                        progression()
                        totalTrys = 0
                        pass
                        progreso = 0
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,40)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 4:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 4:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break

            elif progressionList[2] == "Avanzado":                                        # Nivel avanzado
                secretNumber = random.randint(1,30)
                print(secretNumber)
                print("avanzado")

                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
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
                        pass
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,30)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break
            
            elif progressionList[1] == "Experimentado": 
                secretNumber = random.randint(1,20)                                       # Nivel experimentado
                print(secretNumber)
                print("experimentado")
                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
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
                        pass
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,20)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break
            
            elif progressionList[0] == "Principiante":                                         # Nivel principiante
                secretNumber = random.randint(1,15)
                print(secretNumber)
                print("principiante")
                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
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
                        pass
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,15)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso+=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break

            elif progressionList[0] != "Principiante":                                         # Nivel inicial
                print(secretNumber)
                print("inicial")
                while True:
                    try:
                        myNumber = int(input("\nIntroduce tu número: "))
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
                        pass
                    else:
                        print("-------- x --------")
                        print("\033[32m\033[1mNúmero descubierto\033[0m")
                        print("-------- x --------")
                        secretNumber = random.randint(1,10)
                        print(secretNumber)
                        print("\n\033[33m\033[1mNuevo número oculto generado\033[0m\n")
                        # Reinicio de los intentos si haciertas
                        totalTrys = 0
                        # Reinicio de la barra de progresión
                        progreso = 0
                        continue
                if myNumber < secretNumber:
                    totalTrys += 1
                    progreso += 1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más grande\033[0m")
                if myNumber > secretNumber:
                    totalTrys += 1
                    progreso +=1
                    imprimir_progreso()
                    if totalTrys == 3:
                        player.totalMistakes += 1
                        print("\n--------- x --------")
                        print("\033[31m\033[1mNúmero no encontrado\033[0m")
                        print("--------- x --------")
                        progreso = 0
                        break
                    else:
                        print("\033[33m\033[1m\nEl número oculto es más pequeño\033[0m")
                if myNumber == 00:
                    progreso = 0
                    system("cls")
                    break

        if menuOption == 2:
            system("cls")
            print("--------------------- x ---------------------\n")
            print (f"\033[1mTu puntuación total es de: \033[32m{player.points} puntos\033[0m")
            print (f"\033[1mEl total de fallos es de: \033[31m{player.totalMistakes} fallos\033[0m")
            print("\n--------------------- x ---------------------")
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
                print("\n---------------- x ----------------")
                break

        if menuOption == 4:                                                                      # Modo de juego Blitz
            system("cls")
            print("\nModo Blitz: Tienes 30 segundos para adivinar la mayor cantidad de números posibles, estos números se sitúan del 1-10 y tienes 3 intentos. Cada número descubierto son 3 puntos y cada número no descubierto resta 2 puntos. Tu objetivo es lograr conseguir la mayor cantidad de puntos y desbloquear mayores niveles de dificultad y recompensas\n")
            menuOption = input("Presiona ENTER para comenzar la partida")
            system("cls")
            secretNumber = random.randint(1,10)
            totalTrys = 0
            print(secretNumber)

            # Inicio del temporizador
            duracion_bucle = 30
            inicio_bucle = time.time()

            while time.time() - inicio_bucle < duracion_bucle:
                myNumber = int(input("Escribe número: "))
                
                if myNumber == secretNumber:
                    player.blitzPoints += 1
                    totalTrys = 0
                    secretNumber = random.randint(1,10)
                    print(secretNumber)
                    print("¡Felicidades! ¡Has acertado!")
                    continue

                if myNumber < secretNumber:
                    system("cls")
                    print("\033[33m\033[1m\nEl número oculto es más grande\n\033[0m")
                else:
                    system("cls")
                    print("\033[33m\033[1m\nEl número oculto es más pequeño\n\033[0m")

                totalTrys += 1

                if totalTrys == 3:
                    print("--------- x --------")
                    print("\033[31m\033[1mNúmero no encontrado\033[0m")
                    print("--------- x --------\n")
                    totalTrys = 0 
                    secretNumber = random.randint(1, 10)
                    print(secretNumber)
                    player.blitzTotalMistakes += 1

                if myNumber == 00:
                    progreso = 0
                    totalTrys = 0
                    system("cls")
                    break

            # Fin del temporizador
            time.sleep(1)

            system("cls")
            print(f"\033[1mHas adivinado un total de: \033[32m\033[4m{player.blitzPoints} números\033[0m\033[1m, con un total de: \033[32m\033[4m{player.blitzPoints * 3} puntos\n\033[0m")
            print(f"\033[1mHas fallado un total de: \033[31m\033[4m{player.blitzTotalMistakes} números\033[0m\033[1m, con un total de: \033[31m\033[4m{player.blitzTotalMistakes * 2} puntos\n\033[0m")
            print(f"\033[1mTu resultado final es de: \033[35m\033[4m{(player.blitzPoints * 3) - player.blitzTotalMistakes * 2} puntos\033[0m")
            system("cls")
            break
                
