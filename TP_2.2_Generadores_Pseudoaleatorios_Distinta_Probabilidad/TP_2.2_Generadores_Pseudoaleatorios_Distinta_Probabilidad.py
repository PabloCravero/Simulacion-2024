import random
import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#Distribución Uniforme
def uniform(a, b, n):
  ListUni = []
  for i in range(n):
    nr = random.random()
    vu = round(a + nr * (b - a), 4)
    ListUni.append(vu)
  return ListUni

#Números generados con método del rechazo
def rejection_uniform(a, b, n):
  ListRej = []
  while len(ListRej) < n:
    nr = random.random()
    vu = a + nr * (b - a)
    y = random.random()
    if y <= 1/(b - a):
      ListRej.append(vu)
  return ListRej

#Números generados con método de la transformada inversa
def t_inversa_uniform(a, b, n): #CORREGIR
  nr = np.random.uniform(0,1,n) # Generar n números aleatorios
  vu = a + nr * (b - a) # Aplicar la transformada inversa
  return vu

#Distribución Exponencial
def exponential(l, n): # l es el parámetro de la distribución lambda
  ListExp = []
  for i in range(n):
    nr = random.random()
    ve = -1/l * math.log(nr)
    ListExp.append(ve)
  return ListExp

#Números generados con método de la transformada inversa
def t_inversa_exponential(l,n):
  nr = np.random.uniform(0,1,n) # Generar n números aleatorios
  ve = -np.log(1-nr)/l # Aplicar la transformada inversa
  return ve

#Números generados con método del rechazo
def rejection_exponential(l,n):
  ListRej = []
  while len(ListRej) < n:
    nr = random.random()
    ve = -1/l * math.log(nr)
    if nr <= math.exp(-ve/(1/l)):
      ListRej.append(ve)  
  return ListRej

#Distribución Gamma
def gamma(a, b, n): # a es el parámetro de la distribución alpha, b es el parámetro de la distribución beta
  ListGam = []
  for _ in range(n):
    nr = random.random()
    ve = -1/b * math.log(nr)
    productoria = 1.0
    for _ in range(a):
      nr = random.random()
      productoria *= nr
    vg = ve * productoria
    ListGam.append(vg)
  return ListGam

#Números generados con método del rechazo
def rejection_gamma(a, b, n):
  ListRej = []
  while len(ListRej) < n:
    nr = random.random()
    ve = -1/b * math.log(nr)
    productoria = 1.0
    for _ in range(a):
      nr = random.random()
      productoria *= nr
    vg = ve * productoria
    if nr <= math.exp(-vg/(1/b)):
      ListRej.append(vg)
  return ListRej

#Distribución Normal
def normal(mu, sigma, n):
  ListNor = []
  for _ in range(n):
    sum = 0
    for _ in range (1, 13):
      nr = random.random()
      sum += nr
    vn = sigma * (sum - 6) + mu
    ListNor.append(vn)
  return ListNor

#Números generados con método de la transformada inversa
def t_inversa_normal(mu, sigma, n): #VER!!!
  nr = np.random.uniform(0,1,n) # Generar n números aleatorios
  vn = sigma * np.sqrt(2) * np.sin(2 * np.pi * nr) + mu # Aplicar la transformada inversa
  return vn

#Números generados con método del rechazo
def rejection_normal(mu, sigma, n):
  ListRej = []
  while len(ListRej) < n:
    nr = random.random()
    sum = 0
    for _ in range (1, 13):
      nr = random.random()
      sum += nr
    vn = sigma * (sum - 6) + mu
    if nr <= np.exp(-((vn - mu)**2)/(2*sigma**2))/(sigma * np.sqrt(2 * np.pi)): #VER!!! 
      ListRej.append(vn)
  return ListRej


#Distribución Pascal (Binomial Negativa)
def pascal(r, p, n):  # r es el número de éxitos, p es la probabilidad de éxito en cada ensayo
    ListPas = []
    for _ in range(n):
        count = 0  # Número de fracasos
        successes = 0  # Número de éxitos
        while successes < r:
            if random.random() < p:
                successes += 1
            else:
                count += 1
        ListPas.append(count)
    return ListPas

#Números generados con método del rechazo
def rejection_pascal(r, p, n):
    ListRej = []
    while len(ListRej) < n:
        count = 0  # Número de fracasos
        successes = 0  # Número de éxitos
        while successes < r:
            if random.random() < p:
                successes += 1
            else:
                count += 1
        if random.random() < (math.factorial(r) * p**r * (1-p)**count) / (math.factorial(r) * p**r * (1-p)**count):
            ListRej.append(count)
    return ListRej

#Distribución Binomial
def binomial(trials, p, samples):  # trials es el número de ensayos, p es la probabilidad de éxito en cada ensayo, samples es el número de muestras a generar
    ListBin = []
    for _ in range(samples):
        count = 0  # Número de éxitos
        for _ in range(trials):
            if random.random() < p:
                count += 1
        ListBin.append(count)
    return ListBin

#Números generados con método del rechazo
def rejection_binomial(trials, p, samples):
    ListRej = []
    while len(ListRej) < samples:
        count = 0  # Número de éxitos
        for _ in range(trials):
            if random.random() < p:
                count += 1
        if random.random() < (math.factorial(trials) / (math.factorial(count) * math.factorial(trials - count))) * p**count * (1-p)**(trials - count):
            ListRej.append(count)
    return ListRej

#Distribución Hipergeométrica
def hypergeometric(N, m, n, samples):  # N es el número total de elementos, m es el número de elementos de la clase, n es el número de elementos en la muestra, samples es el número de muestras a generar
    ListHyp = []
    for _ in range(samples):
        count = 0  # Número de elementos de la clase en la muestra
        N_temp = N  # Copia de N para esta muestra
        m_temp = m  # Copia de m para esta muestra
        for _ in range(n):
            if random.random() < m_temp / N_temp:
                count += 1
                m_temp -= 1
            N_temp -= 1
        ListHyp.append(count)
    return ListHyp

#Números generados con método del rechazo
def rejection_hypergeometric(N, m, n, samples):
    ListRej = []
    max_iterations = 100000  # Número máximo de iteraciones permitidas
    iterations = 0  # Contador de iteraciones
    while len(ListRej) < samples and iterations < max_iterations:
        count = 0  # Número de elementos de la clase en la muestra
        for _ in range(n):
            if N != 0 and m != 0 and random.random() < m/N:
                count += 1
                m -= 1
            N -= 1
        numerator = math.factorial(m) if m >= 0 else 0
        denominator = (math.factorial(n) * math.factorial(count)) if n >= 0 and count >= 0 else 0
        if N != 0 and numerator != 0 and denominator != 0 and N - m >= 0 and n - count >= 0 and random.random() < numerator * math.factorial(N - m) * math.factorial(n - count) / denominator:
            ListRej.append(count)
        iterations += 1  # Incrementar el contador de iteraciones
    if iterations >= max_iterations:
        print("Se ha alcanzado el límite máximo de iteraciones sin generar todas las muestras.")
    return ListRej


#Distribución de Poisson
def poisson(l, samples):  # l es el parámetro de la distribución lambda, samples es el número de muestras a generar
    ListPoi = []
    for _ in range(samples):
        count = 0  # Número de ocurrencias
        while random.random() >= math.exp(-l):
            count += 1
        ListPoi.append(count)
    return ListPoi

#Números generados con método del rechazo
def rejection_poisson(l, samples):
    ListRej = []
    while len(ListRej) < samples:
        count = 0  # Número de ocurrencias
        while random.random() >= math.exp(-l):
            count += 1
        log_prob = count * math.log(l) - l - math.log(math.factorial(count))            
        if random.random() < math.exp(log_prob):
            ListRej.append(count)
    return ListRej

#Distribución Empírica Discreta
def discrete_empirical(p, samples):  # p es la lista de probabilidades de cada valor, samples es el número de muestras a generar
    ListDis = []
    for _ in range(samples):
        nr = random.random()
        sum = 0
        for i in range(len(p)):
            sum += p[i]
            if nr < sum:
                ListDis.append(i)
                break
    return ListDis

#Números generados con método del rechazo
def rejection_discrete_empirical(p, samples):
    ListRej = []
    while len(ListRej) < samples:
        nr = random.random()
        sum = 0
        for i in range(len(p)):
            sum += p[i]
            if nr < sum:
                ListRej.append(i)
                break
    return ListRej

#Tests
# Prueba Chi Cuadrado
def chi_squared_test(observed, expected, bins):
    observed_freq, _ = np.histogram(observed, bins=bins)
    expected_freq, _ = np.histogram(expected, bins=bins)
    chi2_stat, p_val = stats.chisquare(observed_freq, expected_freq)
    return chi2_stat, p_val

# Prueba Kolmogorov-Smirnov
def ks_test(sample, cdf):
    ks_stat, p_val = stats.kstest(sample, cdf)
    return ks_stat, p_val

# Ejemplos de uso
n = 1000 # Cantidad de muestras
a, b = 2, 5 # Intervalo de la distribución uniforme 
l = 1 # Parámetro de la distribución exponencial
mu, sigma = 0, 1 # Parámetros de la distribución normal
trials, p_binom = 10, 0.5 # Parámetros de la distribución binomial
r, p_pascal = 5, 0.5 # Parámetros de la distribución pascal
N, m, k = 100, 50, 10 # Parametros de la distribucion Hipergeometrica
l_poisson = 3   # Parámetro de la distribución de Poisson
p_empirical = [0.1, 0.2, 0.3, 0.4] # Probabilidades de la distribución empírica discreta

# Generar muestras
uniform_samples = uniform(a, b, n)
exponential_samples = exponential(l, n)
gamma_samples = gamma(2, 2, n)
normal_samples = normal(mu, sigma, n)
binomial_samples = binomial(trials, p_binom, n)
pascal_samples = pascal(r, p_pascal, n)
hypergeometric_samples = hypergeometric(N, m, k, n)
poisson_samples = poisson(l_poisson, n)
discrete_empirical_samples = discrete_empirical(p_empirical, n)

# Generar muestras con método de la transformada inversa
t_inversa_uniform_samples = t_inversa_uniform(a, b, n)
t_inversa_exponential_samples = t_inversa_exponential(l, n)
t_inversa_normal_samples = t_inversa_normal(mu, sigma, n)

# Generar muestras con método del rechazo
rejection_uniform_samples = rejection_uniform(a, b, n)
rejection_exponential_samples = rejection_exponential(l, n)
rejection_gamma_samples = rejection_gamma(2, 2, n)
rejection_normal_samples = rejection_normal(mu, sigma, n) 
rejection_binomial_samples = rejection_binomial(trials, p_binom, n)
rejection_pascal_samples = rejection_pascal(r, p_pascal, n)
rejection_hypergeometric_samples = rejection_hypergeometric(N, m, k, n)
rejection_poisson_samples = rejection_poisson(l_poisson, n)
rejection_discrete_empirical_samples = rejection_discrete_empirical(p_empirical, n)

#Tests

#Uniforme

# Pruebas Kolmogorov-Smirnov
ks_stat, p_val = ks_test(uniform_samples, 'uniform')
print("Kolmogorov-Smirnov - Uniforme: KS stat =", ks_stat, "p-val =", p_val)

#Exponencial

# Pruebas Kolmogorov-Smirnov
ks_stat, p_val = ks_test(exponential_samples, 'expon')
print("Kolmogorov-Smirnov - Exponencial: KS stat =", ks_stat, "p-val =", p_val)

#Normal

# Pruebas Kolmogorov-Smirnov
ks_stat, p_val = ks_test(normal_samples, 'norm')
print("Kolmogorov-Smirnov - Normal: KS stat =", ks_stat, "p-val =", p_val)

#Binomial
# Pruebas Chi Cuadrado
expected_binomial = np.random.binomial(trials, p_binom, n)
chi2_stat, p_val = chi_squared_test(binomial_samples, expected_binomial, bins=10)
print("Chi Cuadrado - Binomial: Chi2 =", chi2_stat, "p-val =", p_val)

#Poisson
# Pruebas Chi Cuadrado
expected_poisson = np.random.poisson(l_poisson, n)
chi2_stat, p_val = chi_squared_test(poisson_samples, expected_poisson, bins=10)
print("Chi Cuadrado - Poisson: Chi2 =", chi2_stat, "p-val =", p_val)

#Empírica Discreta
# Pruebas Chi Cuadrado
expected_discrete_empirical = np.random.choice(len(p_empirical), n, p=p_empirical)
chi2_stat, p_val = chi_squared_test(discrete_empirical_samples, expected_discrete_empirical, bins=10)
print("Chi Cuadrado - Empírica Discreta: Chi2 =", chi2_stat, "p-val =", p_val)

#Graficos
# Graficos Distribución Uniforme
plt.figure(figsize=(18, 5))

# Histograma de uniform_samples
plt.subplot(1, 3, 1)
plt.hist(uniform_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Uniforme')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_uniform_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_uniform_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Uniforme con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de t_inversa_uniform_samples
plt.subplot(1, 3, 3)
plt.hist(t_inversa_uniform_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Uniforme transformada inversa')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Exponencial
plt.figure(figsize=(18, 5))

# Histograma de exponential_samples
plt.subplot(1, 3, 1)
plt.hist(exponential_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Exponencial')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_exponential_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_exponential_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Exponencial con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de t_inversa_exponential_samples
plt.subplot(1, 3, 3)
plt.hist(t_inversa_exponential_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Exponencial transformada inversa')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Gamma
plt.figure(figsize=(18, 5))

# Histograma de gamma_samples
plt.subplot(1, 3, 1)
plt.hist(gamma_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Gamma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_gamma_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_gamma_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Gamma con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Normal
plt.figure(figsize=(18, 5))

# Histograma de normal_samples
plt.subplot(1, 3, 1)
plt.hist(normal_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Normal')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_normal_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_normal_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Normal con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de t_inversa_normal_samples
plt.subplot(1, 3, 3)
plt.hist(t_inversa_normal_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Normal transformada inversa')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Pascal
plt.figure(figsize=(18, 5))

# Histograma de pascal_samples
plt.subplot(1, 3, 1)
plt.hist(pascal_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Pascal')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_pascal_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_pascal_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Pascal con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Binomial
plt.figure(figsize=(18, 5))

# Histograma de binomial_samples
plt.subplot(1, 3, 1)
plt.hist(binomial_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Binomial')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_binomial_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_binomial_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Binomial con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Hipergeométrica
plt.figure(figsize=(18, 5))

# Histograma de hypergeometric_samples
plt.subplot(1, 3, 1)
plt.hist(hypergeometric_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Hipergeométrica')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_hypergeometric_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_hypergeometric_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Hipergeométrica con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Poisson
plt.figure(figsize=(18, 5))

# Histograma de poisson_samples
plt.subplot(1, 3, 1)
plt.hist(poisson_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Poisson')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_poisson_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_poisson_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Poisson con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Graficos Distribución Empírica Discreta
plt.figure(figsize=(18, 5))

# Histograma de discrete_empirical_samples
plt.subplot(1, 3, 1)
plt.hist(discrete_empirical_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Empírica Discreta')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Histograma de rejection_discrete_empirical_samples
plt.subplot(1, 3, 2)
plt.hist(rejection_discrete_empirical_samples, bins=10, edgecolor='black')
plt.title('Histograma Distribución Empírica Discreta con método del rechazo')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()






