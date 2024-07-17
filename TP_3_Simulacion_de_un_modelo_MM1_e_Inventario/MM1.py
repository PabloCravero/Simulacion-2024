import random
import math
import matplotlib.pyplot as plt
import numpy as np
def inicializar(): #Funcion que inicializa las variables
    tiempo_simulacion = 0.0
    estado_servidor = 0
    num_en_cola = 0
    tiempo_ultimo_evento = 0.0
    total_retrasos = 0.0
    num_clientes_atendidos = 0
    area_num_en_cola = 0.0
    area_estado_servidor = 0.0

    return tiempo_simulacion, estado_servidor, num_en_cola, tiempo_ultimo_evento, total_retrasos, num_clientes_atendidos, area_num_en_cola, area_estado_servidor

def tiempo(tiempo_simulacion, tiempo_proximo_evento, tipo_siguiente_evento, num_eventos): #Funcion que determina el siguiente evento
    min_tiempo_proximo_evento = float('inf')
    tipo_siguiente_evento = 0

    for i in range(1, num_eventos + 1):
        if tiempo_proximo_evento[i] < min_tiempo_proximo_evento:
            min_tiempo_proximo_evento = tiempo_proximo_evento[i]
            tipo_siguiente_evento = i

    if tipo_siguiente_evento == 0:
        print("\nLista de eventos vacía en tiempo", tiempo_simulacion)
        exit(1)

    tiempo_simulacion = min_tiempo_proximo_evento

    return tiempo_simulacion, tipo_siguiente_evento

def llegada(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, media_llegadas, media_servicio): #Funcion que maneja la llegada de un cliente   
    tiempo_proximo_evento[1] = tiempo_simulacion + exponencial(media_llegadas) 

    if estado_servidor == 1:
        num_en_cola += 1

        if num_en_cola > Q_LIMITE:
            print("\nDesbordamiento de la cola en tiempo", tiempo_simulacion)
            exit(2)

        tiempo_llegada[num_en_cola] = tiempo_simulacion
    else:
        demora = 0.0
        total_retrasos += demora

        num_clientes_atendidos += 1
        estado_servidor = 1
        tiempo_proximo_evento[2] = tiempo_simulacion + exponencial(media_servicio)

    return tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos

def salida(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, media_servicio): #Funcion que maneja la salida de un cliente 
    if num_en_cola == 0:
        estado_servidor = 0
        tiempo_proximo_evento[2] = float('inf')
    else:
        num_en_cola -= 1

        demora = tiempo_simulacion - tiempo_llegada[1]
        total_retrasos += demora

        num_clientes_atendidos += 1
        tiempo_proximo_evento[2] = tiempo_simulacion + exponencial(media_servicio)

        for i in range(1, num_en_cola + 1): #Desplaza los clientes en cola
            tiempo_llegada[i] = tiempo_llegada[i + 1]

    return tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos

def informe(tiempo_simulacion, num_clientes_atendidos, total_retrasos, area_num_en_cola, area_estado_servidor, media_llegadas, media_servicio):
    promedio_clientes_sistema = (area_estado_servidor / (tiempo_simulacion))*media_servicio
    promedio_clientes_cola = area_num_en_cola / (tiempo_simulacion)
    tiempo_promedio_sistema = (total_retrasos / num_clientes_atendidos)
    tiempo_promedio_cola = ((area_num_en_cola*promedio_clientes_sistema) / num_clientes_atendidos)
    utilizacion_servidor = area_estado_servidor / tiempo_simulacion
    print(tiempo_simulacion)
    print("\nResultados de la simulación:")
    print("Promedio de clientes en el sistema:", promedio_clientes_sistema)
    print("Promedio de clientes en cola:", promedio_clientes_cola)
    print("Tiempo promedio en el sistema:", tiempo_promedio_sistema)
    print("Tiempo promedio en cola:", tiempo_promedio_cola)
    print("Utilización del servidor:", utilizacion_servidor)
    print("Tiempo de finalización de la simulación:", tiempo_simulacion, "minutos")

def exponencial(media): 
    return -media * math.log(random.random()) 

def simular(media_llegadas, media_servicio, num_retrasos_requeridos):
    tiempo_proximo_evento = [0.0, 0.0, 0.0]
    tipo_siguiente_evento = 0
    tiempo_llegada = [0.0] * ( Q_LIMITE+ 1)

    tiempo_simulacion, estado_servidor, num_en_cola, tiempo_ultimo_evento, total_retrasos, num_clientes_atendidos, area_num_en_cola, area_estado_servidor = inicializar()

    tiempo_proximo_evento[1] = tiempo_simulacion + exponencial(media_llegadas)
    tiempo_proximo_evento[2] = float('inf')
    tiempos = []
    clientes_en_cola = []
    utilizacion_servidor1 = [] = []
    while num_clientes_atendidos < num_retrasos_requeridos:
        tiempo_simulacion, tipo_siguiente_evento = tiempo(tiempo_simulacion, tiempo_proximo_evento, tipo_siguiente_evento, 2)
        area_num_en_cola += num_en_cola * (tiempo_simulacion - tiempo_ultimo_evento)
        area_estado_servidor += estado_servidor * (tiempo_simulacion - tiempo_ultimo_evento)
        tiempo_ultimo_evento = tiempo_simulacion

        if tipo_siguiente_evento == 1:
            tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos = llegada(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, media_llegadas, media_servicio)
        elif tipo_siguiente_evento == 2:
            tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos = salida(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, media_servicio)
        tiempos.append(tiempo_simulacion)
        clientes_en_cola.append(num_en_cola)
        utilizacion_servidor1.append(area_estado_servidor/tiempo_simulacion)
    informe(tiempo_simulacion, num_clientes_atendidos, total_retrasos, area_num_en_cola, area_estado_servidor, media_llegadas, media_servicio)
    
    tiempos=np.array(tiempos)/60
    plt.bar(tiempos, clientes_en_cola)
    plt.xlabel('Hora')
    plt.ylabel('Clientes en cola')
    plt.title('Número de clientes en cola a lo largo del tiempo')
    plt.show()

    
    tiempo_promedio_utilizacion = area_estado_servidor / tiempo_simulacion
    labels = ['Utilizado', 'No utilizado']
    sizes = [tiempo_promedio_utilizacion, 1 - tiempo_promedio_utilizacion]
    explode = (0.1, 0)  
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  
    plt.title("Tiempo Promedio de Utilización del Servidor")
    plt.show()
    

Q_LIMITE = 10000
media_llegadas = 3
media_servicio = 4 #este siempre mayor que media_llegadas   
num_retrasos_requeridos = 1000

simular(media_llegadas, media_servicio, num_retrasos_requeridos)
