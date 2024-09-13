"""Ejercicio 2: Construya un algoritmo que, haciendo uso de un TAD adecuado, permita simular durante cinco horas, el comportamiento de inscripciones de viviendas en el IPV, teniendo en cuenta que el tiempo de atención del empleado es de 15 minutos, en promedio. Además, la frecuencia de llegada de los solicitantes es de 10 minutos.

a) Fundamente la elección del TAD usado para resolver la problemática planteada.
b) Una vez finalizada la simulación, indique cuál fue el tiempo máximo de cola de espera de aquellos solicitantes que no fueron atendidos."""

import random
from clase_cola_encadenada import cola
from clase_cliente import cliente

if __name__ == '__main__':
    tiempo=300 #300 minutos = 5 horas
    reloj=0
    tiempo_atencion=15
    frecuencia=10
    
    cola_clientes=cola()
    
    while reloj!=tiempo:
        random_cliente=random.random()
        if 0<random_cliente<(1/frecuencia):#Llego un cliente
            tiempo_requerido=random.randint(13, 15)#Tiempo que necesitara ser atendido 
            un_cliente=cliente(tiempo_requerido, reloj)
            
            cola_clientes.insertar(un_cliente)
            
        if tiempo_atencion==15 and cola_clientes.vacia()==False:#Si atencion disponible y cola no vacia
            cliente_atendido=cola_clientes.suprimir()
            cliente_atendido.set_espera(reloj)#Calculo la espera del cliente
            tiempo_restante=cliente_atendido.dar_requerido()
            tiempo_atencion-=tiempo_restante#Ajusto la atencion a lo requerido por el cliente
            
        if tiempo_atencion<15:#Si la atencion esta ocupada se incrementa uno por minuto
            tiempo_atencion+=1
                
        
        reloj+=1
        
    max_espera=0
    while cola_clientes.vacia()!=True:#Los clientes que quedaron en la cola luego de la simulacion
        no_atendido=cola_clientes.suprimir()
        espera=no_atendido.set_espera(reloj)
        
        if espera>max_espera:
            max_espera=espera
            
    print(f"\nEl maximo de espera de clientes no atendios fue de {max_espera} minutos")
    
    
"""Se utiliza un TDA cola porque responde a la politica FIFO first in firt out"""