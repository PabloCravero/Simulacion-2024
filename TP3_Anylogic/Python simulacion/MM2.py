import random
import math
import matplotlib.pyplot as plt
import numpy as np

def inicializar():
    tiempo_simulacion = 0.0
    estado_servidor = 0
    num_en_cola = 0
    tiempo_ultimo_evento = 0.0
    total_retrasos = 0.0
    num_clientes_atendidos = 0
    area_num_en_cola = 0.0
    area_estado_servidor = 0.0

    return tiempo_simulacion, estado_servidor, num_en_cola, tiempo_ultimo_evento, total_retrasos, num_clientes_atendidos, area_num_en_cola, area_estado_servidor

def tiempo(tiempo_simulacion, tiempo_proximo_evento, tipo_siguiente_evento, num_eventos):
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

def llegada(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, mu, lambdaa):
    tiempo_proximo_evento[1] = tiempo_simulacion + exponencial(mu)

    if estado_servidor == 1:
        num_en_cola += 1

        if num_en_cola > limite_cola:
            print("\nDesbordamiento de la cola en tiempo", tiempo_simulacion)
            exit(2)

        tiempo_llegada[num_en_cola] = tiempo_simulacion
    else:
        demora = 0.0
        total_retrasos += demora

        num_clientes_atendidos += 1
        estado_servidor = 1
        tiempo_proximo_evento[2] = tiempo_simulacion + exponencial(lambdaa)

    return tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos

def salida(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, lambdaa):
    if num_en_cola == 0:
        estado_servidor = 0
        tiempo_proximo_evento[2] = float('inf')
    else:
        num_en_cola -= 1

        demora = tiempo_simulacion - tiempo_llegada[1]
        total_retrasos += demora

        num_clientes_atendidos += 1
        tiempo_proximo_evento[2] = tiempo_simulacion + exponencial(lambdaa)

        for i in range(1, num_en_cola + 1):
            tiempo_llegada[i] = tiempo_llegada[i + 1]

    return tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos

def informe(tiempo_simulacion, num_clientes_atendidos, total_retrasos, area_num_en_cola, area_estado_servidor, mu, lambdaa):
    promedio_clientes_sistema = (area_estado_servidor / tiempo_simulacion) * lambdaa
    promedio_clientes_cola = area_num_en_cola / tiempo_simulacion
    tiempo_promedio_sistema = total_retrasos / num_clientes_atendidos
    tiempo_promedio_cola = (area_num_en_cola * promedio_clientes_sistema) / num_clientes_atendidos
    utilizacion_servidor = area_estado_servidor / tiempo_simulacion

    print("\nResultados de la simulación:")
    print("Promedio de clientes en el sistema:", promedio_clientes_sistema)
    print("Promedio de clientes en cola:", promedio_clientes_cola)
    print("Tiempo promedio en el sistema:", tiempo_promedio_sistema)
    print("Tiempo promedio en cola:", tiempo_promedio_cola)
    print("Utilización del servidor:", utilizacion_servidor)
    print("Tiempo de finalización de la simulación:", tiempo_simulacion, "minutos")

def exponencial(media):
    return -media * math.log(random.random())

def simular(mu, lambdaa, num_retrasos_requeridos):
    tiempo_proximo_evento = [0.0, 0.0, 0.0]
    tipo_siguiente_evento = 0
    tiempo_llegada = [0.0] * (limite_cola + 1)

    tiempo_simulacion, estado_servidor, num_en_cola, tiempo_ultimo_evento, total_retrasos, num_clientes_atendidos, area_num_en_cola, area_estado_servidor = inicializar()

    tiempo_proximo_evento[1] = tiempo_simulacion + exponencial(mu)
    tiempo_proximo_evento[2] = float('inf')

    tiempos = []
    clientes_en_cola = []
    utilizacion_servidor1 = []

    while num_clientes_atendidos < num_retrasos_requeridos:
        tiempo_simulacion, tipo_siguiente_evento = tiempo(tiempo_simulacion, tiempo_proximo_evento, tipo_siguiente_evento, 2)
        area_num_en_cola += num_en_cola * (tiempo_simulacion - tiempo_ultimo_evento)
        area_estado_servidor += estado_servidor * (tiempo_simulacion - tiempo_ultimo_evento)
        tiempo_ultimo_evento = tiempo_simulacion

        if tipo_siguiente_evento == 1:
            tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos = llegada(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, mu, lambdaa)
        elif tipo_siguiente_evento == 2:
            tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos = salida(tiempo_simulacion, tiempo_proximo_evento, estado_servidor, num_en_cola, tiempo_llegada, total_retrasos, num_clientes_atendidos, lambdaa)

        tiempos.append(tiempo_simulacion)
        clientes_en_cola.append(num_en_cola)
        utilizacion_servidor1.append(area_estado_servidor / tiempo_simulacion)

    return tiempos, clientes_en_cola, utilizacion_servidor1, tiempo_simulacion, num_clientes_atendidos, total_retrasos, area_num_en_cola, area_estado_servidor

def ejecutar_simulaciones(mu, lambdaa, num_retrasos_requeridos, num_corridas):
    todos_tiempos = []
    todos_clientes_en_cola = []
    todas_utilizaciones = []
    promedios_clientes_sistema = []
    promedios_clientes_cola = []
    tiempos_promedios_sistema = []
    tiempos_promedios_cola = []
    utilizaciones_servidor = []

    max_len = 0

    for i in range(num_corridas):
        tiempos, clientes_en_cola, utilizacion_servidor1, tiempo_simulacion, num_clientes_atendidos, total_retrasos, area_num_en_cola, area_estado_servidor = simular(mu, lambdaa, num_retrasos_requeridos)
        
        promedio_clientes_sistema = (area_estado_servidor / tiempo_simulacion) * lambdaa
        promedio_clientes_cola = area_num_en_cola / tiempo_simulacion
        tiempo_promedio_sistema = total_retrasos / num_clientes_atendidos
        tiempo_promedio_cola = (area_num_en_cola * promedio_clientes_sistema) / num_clientes_atendidos
        utilizacion_servidor = area_estado_servidor / tiempo_simulacion

        promedios_clientes_sistema.append(promedio_clientes_sistema)
        promedios_clientes_cola.append(promedio_clientes_cola)
        tiempos_promedios_sistema.append(tiempo_promedio_sistema)
        tiempos_promedios_cola.append(tiempo_promedio_cola)
        utilizaciones_servidor.append(utilizacion_servidor)

        todos_tiempos.append(tiempos)
        todos_clientes_en_cola.append(clientes_en_cola)
        todas_utilizaciones.append(utilizacion_servidor1)

        if len(tiempos) > max_len:
            max_len = len(tiempos)

    # Rellenar o truncar los arreglos para que tengan la misma longitud
    for i in range(num_corridas):
        if len(todos_tiempos[i]) < max_len:
            padding = max_len - len(todos_tiempos[i])
            todos_tiempos[i] = np.pad(todos_tiempos[i], (0, padding), 'edge')
            todos_clientes_en_cola[i] = np.pad(todos_clientes_en_cola[i], (0, padding), 'edge')
            todas_utilizaciones[i] = np.pad(todas_utilizaciones[i], (0, padding), 'edge')
        elif len(todos_tiempos[i]) > max_len:
            todos_tiempos[i] = todos_tiempos[i][:max_len]
            todos_clientes_en_cola[i] = todos_clientes_en_cola[i][:max_len]
            todas_utilizaciones[i] = todas_utilizaciones[i][:max_len]

    # Cálculo del promedio de las 10 corridas
    tiempos_promedio = np.mean(todos_tiempos, axis=0)
    clientes_en_cola_promedio = np.mean(todos_clientes_en_cola, axis=0)
    utilizacion_promedio = np.mean(todas_utilizaciones, axis=0)
    promedio_clientes_sistema = np.mean(promedios_clientes_sistema)
    promedio_clientes_cola = np.mean(promedios_clientes_cola)
    tiempo_promedio_sistema = np.mean(tiempos_promedios_sistema)
    tiempo_promedio_cola = np.mean(tiempos_promedios_cola)
    utilizacion_servidor_promedio = np.mean(utilizaciones_servidor)

    # Gráfico de clientes en cola promedio
    tiempos_promedio = tiempos_promedio / 60
    plt.bar(tiempos_promedio, clientes_en_cola_promedio)
    plt.xlabel('Hora')
    plt.ylabel('Clientes en cola')
    plt.title('Promedio de clientes en cola a lo largo del tiempo')
    plt.show()

    # Gráfico de utilización promedio del servidor
    labels = ['Utilizado', 'No utilizado']
    sizes = [utilizacion_servidor_promedio, 1 - utilizacion_servidor_promedio]
    explode = (0.1, 0)  
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  
    plt.title("Promedio de utilización del servidor")
    plt.show()

    print("\nResultados promedio de la simulación múltiple:")
    print("Promedio de clientes en el sistema:", promedio_clientes_sistema)
    print("Promedio de clientes en cola:", promedio_clientes_cola)
    print("Tiempo promedio en el sistema:", tiempo_promedio_sistema)
    print("Tiempo promedio en cola:", tiempo_promedio_cola)
    print("Utilización del servidor:", utilizacion_servidor_promedio)

limite_cola = 10000
mu = 4
lambdaa = 2
num_retrasos_requeridos = 1000
num_corridas = 10

ejecutar_simulaciones(mu, lambdaa, num_retrasos_requeridos, num_corridas)
