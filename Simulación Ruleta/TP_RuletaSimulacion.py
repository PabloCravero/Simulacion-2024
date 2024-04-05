import matplotlib.pyplot as plt
import random
import sys
import numpy as np

# Obtener el número de valores de los argumentos de la línea de comandos
tiradas = int(sys.argv[1])
corridas = int(sys.argv[2])
numerito = int(sys.argv[3])

frecuencia_relativa_esperada = round(1/37, 4)
promedio_esperado = sum(range(37)) / 37
desvio_esperado = round(np.std(range(37)), 4)
varianza_esperada = round(np.var(range(37)), 4)

# Verificar si se proporciona el número de valores como argumento
if (numerito >= 0) and (numerito <= 36):
    if len(sys.argv) != 3 or tiradas != "-n":
        print("Uso: python programa.py -n <num_valores>")
        # sys.exit(1)
    else:
        print('Mal puestos los datos')

    resultados = {'frecuencias_relativas': [], 'varianzas': [], 'desvios': [], 'promedios': []}
    for _ in range(corridas):
        salio = 0
        numeros_corrida = []
        frecuencias_relativas = []
        varianzas = []
        desvios = []
        promedios = []
        valores = [random.randint(0, 37) for _ in range(tiradas)]
        print("Valores generados:", valores)

        for numero in valores:
            if numero == numerito:
                salio += 1
            frecuencia_relativa = salio / len(numeros_corrida) if len(numeros_corrida) > 0 else 0
            frecuencias_relativas.append(frecuencia_relativa)
            numeros_corrida.append(numero)
            varianza = np.var(numeros_corrida)
            varianzas.append(varianza)
            desvio = np.std(numeros_corrida)
            desvios.append(desvio)
            promedio = np.mean(numeros_corrida)
            promedios.append(promedio)

        resultados['frecuencias_relativas'].append(frecuencias_relativas)
        resultados['varianzas'].append(varianzas)
        resultados['desvios'].append(desvios)
        resultados['promedios'].append(promedios)
    #Graficos
    plt.figure(figsize=(18, 10))

    plt.subplot(2, 4, 1)
    for frecuencia_relativa in resultados['frecuencias_relativas']:
        plt.plot(frecuencia_relativa)
    plt.xlabel('Índice')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Nube de Curvas - Frecuencias Relativas')
    plt.axhline(y=frecuencia_relativa_esperada, color='black', linestyle='--', label='Frecuencia Relativa Esperada')

    plt.subplot(2, 4, 3)
    for varianza in resultados['varianzas']:
        plt.plot(varianza)
    plt.xlabel('Índice')
    plt.ylabel('Varianza')
    plt.title('Nube de Curvas - Varianzas')
    plt.axhline(y=varianza_esperada, color='black', linestyle='--', label='Varianza Esperada')

    plt.subplot(2, 4, 5)
    for desvio in resultados['desvios']:
        plt.plot(desvio)
    plt.xlabel('Índice')
    plt.ylabel('Desvío')
    plt.title('Nube de Curvas - Desvíos')
    plt.axhline(y=desvio_esperado, color='black', linestyle='--', label='Desvio Esperado')

    plt.subplot(2, 4, 7)
    for promedio in resultados['promedios']:
        plt.plot(promedio)
    plt.xlabel('Índice')
    plt.ylabel('Promedio')
    plt.title('Nube de Curvas - Promedios')
    plt.axhline(y=promedio_esperado, color='black', linestyle='--', label='Promedio Esperado')

    #Histogramas
    plt.subplot(2, 4, 2)
    plt.hist(resultados['frecuencias_relativas'], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Frecuencia Relativa')
    plt.ylabel('Frecuencia')
    plt.title('Histograma - Frecuencias Relativas')

    plt.subplot(2, 4, 4)
    plt.hist(resultados['varianzas'], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Varianza')
    plt.ylabel('Frecuencia')
    plt.title('Histograma - Varianzas')

    plt.subplot(2, 4, 6)
    plt.hist(resultados['desvios'], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Desvío')
    plt.ylabel('Frecuencia')
    plt.title('Histograma - Desvío')

    plt.subplot(2, 4, 8)
    plt.hist(resultados['promedios'], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Promedio')
    plt.ylabel('Frecuencia')
    plt.title('Histograma - Promedios')

    plt.subplots_adjust(hspace=100, wspace=100)
    plt.tight_layout()
    plt.show()

else:
    print("Se debe elegir un número entre 0-36")