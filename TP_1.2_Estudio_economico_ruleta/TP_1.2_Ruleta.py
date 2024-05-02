import matplotlib.pyplot as plt
import random
import sys

# Obtener el número de valores de los argumentos de la línea de comandos
tiradas = int(sys.argv[1])
corridas = int(sys.argv[2])
numero = int(sys.argv[3])
estrategia = str(sys.argv[4])
capital = str(sys.argv[5])

if (numero >= 0) and (numero <= 36):
    if len(sys.argv) != 3 or tiradas != "-n":
        print("Uso: python programa.py -n <num_valores>")
        # sys.exit(1)
    else:
        print('Mal ingresados los datos')

    for _ in range(corridas):
        valores = [random.randint(0, 1) for _ in range(tiradas)]
        print("Valores generados:", valores)
        if capital == 'f':
            monto = float(input("Ingrese el monto total a jugar: "))
        else:
            monto = float('inf')
        apuesta = float(input("Ingrese el monto de la apuesta inicial: "))
        apuesta_inicial = apuesta
        monto_inicial = monto
        bancarrota = 0
        fibonacci = [0, apuesta_inicial]
        ganancias = 0 #???
        for n in valores:
            if estrategia == 'm':  #martingala
                if n != numero:
                    if capital == 'f':
                        monto -= apuesta
                        apuesta = apuesta * 2
                        print("Monto actual: ", monto)
                        if monto <= 0:
                            bancarrota += 1
                            print("Bancarrota")
                            monto = monto_inicial
                            apuesta = apuesta_inicial
                            print('monto bancarrota: ', monto)
                            print('monto inicial: ', monto_inicial)
                    else:
                        ganancias = ganancias - apuesta
                        apuesta = apuesta * 2
                        print('Ganancias: ', ganancias)
                else:
                    if capital == 'f':
                        monto += apuesta
                        apuesta = apuesta_inicial
                        print("Monto actual: ", monto)
                    else:
                        ganancias = ganancias + apuesta
                        apuesta = apuesta_inicial
                        print('Ganancias: ', ganancias)
            elif estrategia == 'd': #d'alembert
                if n != numero:
                    if capital == 'f':
                        monto -= apuesta
                        apuesta = apuesta + 1
                        print("Monto actual: ", monto)
                        if monto <= 0:
                            bancarrota += 1
                            print("Bancarrota")
                            monto = monto_inicial
                            apuesta = apuesta_inicial
                            print('monto bancarrota: ', monto)
                            print('monto inicial: ', monto_inicial)
                    else:
                        ganancias = ganancias - apuesta
                        apuesta = apuesta + 1
                        print('Ganancias: ', ganancias)
                else:
                    if capital == 'f':
                        monto += apuesta
                        apuesta = apuesta - 1
                        print("Monto actual: ", monto)
                    else:
                        ganancias = ganancias + apuesta
                        apuesta = apuesta - 1
                        print('Ganancias: ', ganancias)
            elif estrategia == 'f': # Fibonacci
                if n != numero:
                    if capital == 'f':
                        monto -= apuesta
                        apuesta = fibonacci[-1] + fibonacci[-2] 
                        fibonacci.append(apuesta)  
                        print("fibonacci: ", fibonacci)
                        print("Monto actual: ", monto)
                        if monto <= 0:
                            bancarrota += 1
                            print("Bancarrota")
                            monto = monto_inicial
                            apuesta = apuesta_inicial
                            fibonacci = [0, apuesta_inicial]
                            print('monto bancarrota: ', monto)
                            print('monto inicial: ', monto_inicial)
                    else: 
                        ganancias = ganancias - apuesta
                        apuesta = fibonacci[-1] + fibonacci[-2] 
                        fibonacci.append(apuesta)
                        print('apuesta: ', apuesta)
                        print('Ganancias: ', ganancias)
                        print(fibonacci)
                else:
                    if capital == 'f':
                        monto += apuesta
                        if len(fibonacci) > 3:
                            apuesta = fibonacci[-3] 
                        fibonacci.append(apuesta)
                        print("Monto actual: ", monto)
                        print("fibonacci: ", fibonacci)
                    else:
                        ganancias = ganancias + apuesta
                        if len(fibonacci) > 3:
                            apuesta = fibonacci[-3]
                        fibonacci.append(apuesta)
                        print('apuesta: ', apuesta)
                        print('Ganancias: ', ganancias)
                        print(fibonacci)
            elif estrategia == 'p': #paroli o martingala inversa
                if n == numero:
                    if capital == 'f':
                        monto += apuesta
                        apuesta = apuesta * 2
                        print("Monto actual: ", monto)
                    else:
                        ganancias = ganancias + apuesta
                        apuesta = apuesta * 2
                        print('Ganancias: ', ganancias)
                else:
                    if capital == 'f':
                        monto -= apuesta
                        apuesta = apuesta_inicial
                        print("Monto actual: ", monto)
                        if monto <= 0:
                            bancarrota += 1
                            print("Bancarrota")
                            monto = monto_inicial
                            apuesta = apuesta_inicial
                            print('monto bancarrota: ', monto)
                            print('monto inicial: ', monto_inicial)
                    else: 
                        ganancias = ganancias - apuesta
                        apuesta = apuesta_inicial
                        print('Ganancias: ', ganancias)
            
                    
                    
                    
                    