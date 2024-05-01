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
        valores = [random.randint(0, 5) for _ in range(tiradas)]
        print("Valores generados:", valores)
        if capital == 'f':
            monto = float(input("Ingrese el monto total a jugar: "))
        else:
            monto = float('inf')
        apuesta = float(input("Ingrese el monto de la apuesta inicial: "))
        apuesta_inicial = apuesta
        monto_inicial = monto
        bancarrota = 0
        ganancias = 0
        for n in valores:
            if estrategia == 'm':  #martingala
                if n != numero:
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
                    monto += apuesta
                    apuesta = apuesta_inicial
                    print("Monto actual: ", monto)
            elif estrategia == 'd': #d'alembert
                if n != numero:
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
                    monto += apuesta
                    apuesta = apuesta - 1
                    print("Monto actual: ", monto)
            elif estrategia == 'f': #fibonacci completar
                if n != numero:
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
                    monto += apuesta
                    apuesta = apuesta - 1
                    print("Monto actual: ", monto)
            elif estrategia == 'p': #paroli o martingala inversa
                if n == numero:
                    monto += apuesta
                    apuesta = apuesta * 2
                    print("Monto actual: ", monto)
                else:
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
        
                    
                    
                    
                    