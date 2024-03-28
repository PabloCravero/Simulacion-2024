# Importamos las librerias!
import matplotlib as plt
import random
import sys
import statistics

# Obtener el número de valores de los argumentos de la línea de comandos
tiradas = int(sys.argv[1])
corridas = int(sys.argv[2])
numerito = int(sys.argv[3])

# Verificar si se proporciona el número de valores como argumento
if (numerito >= 0) and (numerito <= 36):
    if len(sys.argv) != 3 or tiradas != "-n":
        print("Uso: python programa.py -n <num_valores>")
        # sys.exit(1)
    else:
        print('Mal puestos los datos')

    # Generar los valores aleatorios entre 0 y 1 y almacenarlos en una lista
    resultados = []
    total = []
    for _ in range(corridas):
        valores = [random.randint(0, 37) for _ in range(tiradas)]
        ocurrencias = valores.count(numerito)
        resultados.append(ocurrencias)
        total.append(sum(valores))
        print("Valores generados:", valores)

    # Mostrar la cantidad de ocurrencias
    cantidad_total = 0
    frecuencias_absolutas =[]
    frecuencias_relativas =[]
    for i, ocurrencias in enumerate(resultados, 1):
        print('ESTO ES I: ', i)
        cantidad_total = cantidad_total + ocurrencias
        frecuencias_absolutas.append(ocurrencias)
        frecuencias_relativas.append(ocurrencias/tiradas)
        print(f"Corrida {i}: {ocurrencias} ocurrencias del número {numerito}")
        print(f"Frecuencias absolutas: {frecuencias_absolutas}")
        print(f"Frecuencias: {frecuencias_relativas}")
        print(f"Promedio por corrida: {total[i-1]/tiradas}")

    print('Frecuencia relativa esperada:', round(1/37, 4))
    print('Promedio esperado:', sum(range(37)) / 37)
    print('Desvío esperado:', round(statistics.stdev(range(37)), 4))
    print('Varianza esperada:', round(statistics.variance(range(37)), 4))
    print('Total de ocurrencias:', cantidad_total)
    print('Nombre Archivo:', sys.argv[0],'Cantidad Tiradas:', sys.argv[1],'Cantidad Corridas:', sys.argv[2], 'Numero a elegir', sys.argv[3])
else:
    print("Se debe elegir un número entre 0-36")




