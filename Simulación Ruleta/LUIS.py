# Importamos las librerias!
import matplotlib as plt
import random
import sys
import statistics

# Obtener el número de valores de los argumentos de la línea de comandos
tiradas = int(sys.argv[1])
corridas = int(sys.argv[2])
numerito = int(sys.argv[3])

resultados = []
total = []
cantidad_total = 0
frecuencias_absolutas = []
frecuencias_relativas = []
desviaciones_estandar = []
varianzas = []


if (numerito >= 0) and (numerito <= 36):
    if len(sys.argv) != 3 or tiradas != "-n":
        print("Uso: python programa.py -n <num_valores>")
        # sys.exit(1)
    else:
        print('Mal puestos los datos')

# Generar los valores aleatorios entre 0 y 1 y almacenarlos en una lista
    for i in range(1, corridas + 1):
        valores = [random.randint(0, 37) for _ in range(tiradas)]
        ocurrencias = valores.count(numerito)
        resultados.append(ocurrencias)
        total.append(sum(valores))
        print("Valores generados en corrida", i, ":", valores)

        cantidad_total += ocurrencias
        frecuencias_absolutas.append(ocurrencias)
        frecuencias_relativas.append(ocurrencias / tiradas)
        desviacion = statistics.stdev(valores)
        desviaciones_estandar.append(desviacion)
        varianza = statistics.variance(valores)
        varianzas.append(varianza)

        print(f"Corrida {i}: {ocurrencias} ocurrencias del número {numerito}")
        print(f"Frecuencias absolutas: {frecuencias_absolutas}")
        print(f"Frecuencias relativas: {frecuencias_relativas}")
        print(f"Promedio por corrida: {total[i-1] / tiradas}")
        print(f"Desviación estándar: {desviacion}")
        print(f"Varianza: {varianza}")


    print("Cantidad total de ocurrencias:", cantidad_total)