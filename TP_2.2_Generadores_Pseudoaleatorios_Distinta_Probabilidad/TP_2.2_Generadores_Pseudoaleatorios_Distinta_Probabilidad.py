import random
import math
import numpy as np

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
