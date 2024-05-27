import scipy.stats
import random
import matplotlib.pyplot as plt

#Generadores Pseudoaleatorios
#Generador GCL
def GCL(seed, a, c, m):
    x = seed
    while True:
        x = (a * x + c) % m
        yield x / m


#Método de los cuadrados medios
def SquareMiddle(seed, digits):
    x = seed
    while True:
        x = x ** 2
        x = int(str(x).zfill(2 * digits)[digits // 2: -digits // 2])
        yield x / 10 ** digits

# Ejemplo de uso
# Parámetros típicos para un GCL:
seed = 2609  # Semilla inicial
a = 1664525  # Multiplicador
c = 1013904223  # Incremento
m = 2**32  # Módulo
digits = 4  # Cantidad de dígitos

# Crear una instancia del generador
GCL_gen = GCL(seed, a, c, m)
SquareMiddle_gen = SquareMiddle(seed, digits)

#print("Generador GCL: ", [next(GCL_gen) for _ in range(10)])
#print("Generador Cuadrados Medios: ", [next(SquareMiddle_gen) for _ in range(10)])

#Tests de los generadores

#Test de bondad de ajuste Chi-cuadrado

def chi2_cdf(x, df): # Función de distribución acumulada de la Chi-cuadrado
    return 1 - scipy.stats.chi2.cdf(x, df)

def chi2_test(generator, intervals, n):
    # Generar n números
    numbers = [next(generator) for _ in range(n)]
    # Contar la cantidad de números en cada intervalo
    observed = [sum(1 for x in numbers if a <= x < b) for a, b in intervals]
    # Calcular el estadístico de prueba
    expected = n / len(intervals)
    chi2 = sum((o - expected) ** 2 / expected for o in observed)
    # Calcular los grados de libertad
    df = len(intervals) - 1
    # Calcular el p-valor
    p_value = 1 - chi2_cdf(chi2, df)
    return chi2, df, p_value

test_chi_GLC = chi2_test(GCL_gen, [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1)], 1000)
test_chi_SquareMiddle = chi2_test(SquareMiddle_gen, [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1)], 1000)
print("Test de Chi-cuadrado para GCL: ", test_chi_GLC)
print("Test de Chi-cuadrado para Cuadrados Medios: ", test_chi_SquareMiddle)

#Test de Corridas (Runs)
def test_runs(generator, n):
    # Generar n números
    numbers = [next(generator) for _ in range(n)]
    # Calcular las corridas
    runs = [1 if x < y else 0 for x, y in zip(numbers, numbers[1:])]
    # Contar la cantidad de corridas
    n1 = sum(runs)
    n2 = len(runs) - n1
    # Calcular el estadístico de prueba
    n = len(runs)
    mu = (2 * n1 * n2) / n + 1 # Media
    sigma = (mu - 1) * (mu - 2) / (n - 1) # Desviación estándar
    z = (n1 - mu) / sigma ** 0.5 # Estadístico de prueba
    # Calcular el p-valor
    p_value = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
    return z, p_value

test_runs_GLC = test_runs(GCL_gen, 1000)
test_runs_SquareMiddle = test_runs(SquareMiddle_gen, 1000)
print("Test de Corridas para GCL: ", test_runs_GLC)
print("Test de Corridas para Cuadrados Medios: ", test_runs_SquareMiddle)

#Prueba de Rachas (Test Squeeze)
def test_squeeze(generator, n):
    # Generar n números
    numbers = [next(generator) for _ in range(n)]
    # Calcular las rachas
    runs = [1 if x < y else 0 for x, y in zip(numbers, numbers[1:])]
    # Contar la cantidad de rachas
    r = sum(1 for x, y in zip(runs, runs[1:]) if x != y)
    # Calcular el estadístico de prueba
    n = len(runs)
    mu = (2 * n - 1) / 3 # Media
    sigma = (16 * n - 29) / 90 # Desviación estándar
    z = (r - mu) / sigma # Estadístico de prueba
    # Calcular el p-valor
    p_value = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
    return z, p_value

test_squeeze_GLC = test_squeeze(GCL_gen, 1000)
test_squeeze_SquareMiddle = test_squeeze(SquareMiddle_gen, 1000)
print("Test de Squeeze para GCL: ", test_squeeze_GLC)
print("Test de Squeeze para Cuadrados Medios: ", test_squeeze_SquareMiddle)

#Prueba Media Aritmética (Test Arithmetic Mean)
def test_arithmetic_mean(generator, n):
    # Generar n números
    numbers = [next(generator) for _ in range(n)]
    # Calcular la media aritmética
    mean = sum(numbers) / n
    # Calcular el estadístico de prueba
    n = len(numbers)
    mu = 0.5 # Media
    sigma = (1 / (12 * n)) ** 0.5 # Desviación estándar
    z = (mean - mu) / sigma # Estadístico de prueba
    # Calcular el p-valor
    p_value = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
    return z, p_value

test_arithmetic_mean_GLC = test_arithmetic_mean(GCL_gen, 1000)
test_arithmetic_mean_SquareMiddle = test_arithmetic_mean(SquareMiddle_gen, 1000)  
print("Test de Media Aritmética para GCL: ", test_arithmetic_mean_GLC)
print("Test de Media Aritmética para Cuadrados Medios: ", test_arithmetic_mean_SquareMiddle)  

#Generador de números aleatorios Python
numeros_random = [random.random() for _ in range(1000)]
numeros_GCL = [next(GCL_gen) for _ in range(1000)]
numeros_SquareMiddle = [next(SquareMiddle_gen) for _ in range(1000)]

#Graficos
#Dispersión de los números generados
plt.scatter(range(1000), numeros_random, label="Generador Random Python")
plt.scatter(range(1000), numeros_GCL, label="Generador de Congruencia Lineal")
plt.scatter(range(1000), numeros_SquareMiddle, label="Generador de Cuadrados Medios")
plt.xlabel("Indice") #numero de muestra
plt.ylabel("Valor generado")
plt.title('Comparación entre generador random, GCL y Cuadrados Medios')
plt.legend()
plt.show()