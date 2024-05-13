import matplotlib.pyplot as plt
import random
import sys

# Obtener el número de valores de los argumentos de la línea de comandos
tiradas = int(sys.argv[1])
corridas = int(sys.argv[2])
numero = int(sys.argv[3])
estrategia = str(sys.argv[4])
capital = str(sys.argv[5])
bancarrota = 0
frecuencias_relativas = []
for i in range(tiradas):
    frecuencias_relativas.append(0)
resultados = {'flujo_cajas': [], 'ganancias_corrida': [], 'frecuencias_relativas': []}

if (numero >= 0) and (numero <= 36):
    if len(sys.argv) == 6:
        print("Uso: python programa.py -n <num_valores>")
        if capital == 'f':
            monto = float(input("Ingrese el monto total a jugar: "))
        else:
            monto = float('inf')
        apuesta = float(input("Ingrese el monto de la apuesta inicial: "))
        monto_inicial = monto   
        apuesta_inicial = apuesta    

        for _ in range(corridas):
            valores = [random.randint(0, 36) for _ in range(tiradas)]
            print("Valores generados:", valores)       
            fibonacci = [0, apuesta_inicial]
            ganancias = 0 #???
            ganancias_corrida = []
            #salio = 0
            #numeros_corrida = []
            flujo_caja = []
            contador = 0
            for n in valores:
                if estrategia == 'm':  #martingala
                    if n != numero:
                        if capital == 'f':
                            monto -= apuesta
                            apuesta = apuesta * 2
                            #print("Monto actual: ", monto)
                            if monto <= 0:
                                bancarrota += 1
                                #print("Bancarrota: ", bancarrota)
                                break
                        else:
                            ganancias = ganancias - apuesta
                            apuesta = apuesta * 2
                            #print('Ganancias: ', ganancias)
                    else:
                        if capital == 'f':
                            monto += apuesta * 36
                            apuesta = apuesta_inicial
                            #print("Monto actual: ", monto)
                            frecuencias_relativas[contador] = frecuencias_relativas[contador] + 1 
                        else:
                            ganancias = ganancias + apuesta * 36
                            apuesta = apuesta_inicial
                            #print('Ganancias: ', ganancias)
                elif estrategia == 'd': #d'alembert
                    if n != numero:
                        if capital == 'f':
                            monto -= apuesta
                            apuesta = apuesta + 1
                            #print("Monto actual: ", monto)
                            if monto <= 0:
                                bancarrota += 1
                                #print("Bancarrota")
                                break
                        else:
                            ganancias = ganancias - apuesta
                            apuesta = apuesta + 1
                            #print('Ganancias: ', ganancias)
                    else:
                        if capital == 'f':
                            monto += apuesta * 36
                            apuesta = apuesta - 1
                            #print("Monto actual: ", monto)
                            frecuencias_relativas[contador] = frecuencias_relativas[contador] + 1 
                        else:
                            ganancias = ganancias + apuesta * 36
                            apuesta = apuesta - 1
                            #print('Ganancias: ', ganancias)
                elif estrategia == 'f': # Fibonacci
                    if n != numero:
                        if capital == 'f':
                            monto -= apuesta
                            apuesta = fibonacci[-1] + fibonacci[-2] 
                            fibonacci.append(apuesta)  
                            #print("fibonacci: ", fibonacci)
                            #print("Monto actual: ", monto)
                            if monto <= 0:
                                bancarrota += 1
                                #print("Bancarrota")
                                break
                        else: 
                            ganancias = ganancias - apuesta
                            apuesta = fibonacci[-1] + fibonacci[-2] 
                            fibonacci.append(apuesta)
                            #print('apuesta: ', apuesta)
                            #print('Ganancias: ', ganancias)
                            #print(fibonacci)
                    else:
                        if capital == 'f':
                            monto += apuesta * 36
                            if len(fibonacci) > 3:
                                apuesta = fibonacci[-3] 
                            fibonacci.append(apuesta)
                            #print("Monto actual: ", monto)
                            #print("fibonacci: ", fibonacci)
                            frecuencias_relativas[contador] = frecuencias_relativas[contador] + 1
                        else:
                            ganancias = ganancias + apuesta * 36
                            if len(fibonacci) > 3:
                                apuesta = fibonacci[-3]
                            fibonacci.append(apuesta)
                            #print('apuesta: ', apuesta)
                            #print('Ganancias: ', ganancias)
                            #print(fibonacci)
                elif estrategia == 'p': #paroli o martingala inversa
                    if n == numero:
                        if capital == 'f':
                            monto += apuesta * 36
                            apuesta = apuesta * 2
                            #print("Monto actual: ", monto)
                            frecuencias_relativas[contador] = frecuencias_relativas[contador] + 1
                        else:
                            ganancias = ganancias + apuesta * 36
                            apuesta = apuesta * 2
                            #print('Ganancias: ', ganancias)
                    else:
                        if capital == 'f':
                            monto -= apuesta 
                            apuesta = apuesta_inicial
                            #print("Monto actual: ", monto)
                            if monto <= 0:
                                bancarrota += 1
                                #print("Bancarrota")
                                break
                        else: 
                            ganancias = ganancias - apuesta
                            apuesta = apuesta_inicial
                            #print('Ganancias: ', ganancias)
                flujo_caja.append(monto)
                ganancias_corrida.append(ganancias)
                contador += 1
            apuesta = apuesta_inicial
            monto = monto_inicial
            resultados['flujo_cajas'].append(flujo_caja)
            resultados['ganancias_corrida'].append(ganancias_corrida)

        for i in range(tiradas):
            #print("i es:", i)
            #print("Frecuencias relativas en i:", frecuencias_relativas[i])
            frecuencias_relativas[i] = frecuencias_relativas[i] / (i+1)
        resultados['frecuencias_relativas'].append(frecuencias_relativas)
        #print("Frecuencias relativas: ", frecuencias_relativas)
        
        # Graficos
        plt.figure(figsize=(18, 10))

        #Gráfico de bastones
        plt.subplot(1,1,1)
        plt.bar(range(tiradas), frecuencias_relativas, color='red')
        plt.xlabel('n - Número de Tiradas')
        plt.ylabel('Fr - Frecuencia Relativa')
        plt.title('Frsa - Frecuencia Relativa de obtener la apuesta favorable según n')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

        # Primer subgráfico para el flujo de caja
        plt.subplot(2, 1, 1)
        for flujo_caja in resultados['flujo_cajas']:
            plt.plot(flujo_caja)
        plt.xlabel('n - Número de Tiradas')
        plt.ylabel('CC - Cantidad Capital')
        plt.title('Nube de Curvas - Flujo de Caja')
        plt.axhline(y=monto, color='black', linestyle='--', label='Flujo de caja inicial')
        plt.legend()

        # Segundo subgráfico para la fluctuación de ganancias
        plt.subplot(2, 1, 2)
        for ganancias in resultados['ganancias_corrida']:
            plt.plot(ganancias)
        plt.xlabel('n - Número de Tiradas')
        plt.ylabel('g - Ganancias')
        plt.title('Nube de Curvas - Fluctuación de ganancia')
        plt.subplots_adjust(hspace=0.5)
        plt.tight_layout()
        plt.show()

    else:
        print('Mal ingresados los datos')
        sys.exit(1)
            
                    
                    
                    
                    