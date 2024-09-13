import random
from clase_cola_secuencial import cola
from clase_trabajo import trabajo

if __name__ == '__main__':
    cola_impresion=cola()
    tiempo=60
    reloj=0
    frecuencia=5
    tiempo_atencion_impresora=5
    trabajos_impresos=0
    espera_trabajos=0  
    
    while tiempo!=reloj:
        numero_random_ingreso=random.random()#Numero aleaotrio para saber si ingreso un trabajo
        if 0<numero_random_ingreso<(1/frecuencia):
            tiempo_requerido=random.randint(1, 10) #Tiempo de impresion del trabajo
            cola_impresion.insertar(trabajo(tiempo_requerido, reloj))          
        
        if tiempo_atencion_impresora==5 and cola_impresion.vacia()==False:#Sera == 5 si la impresora no esta ocupada
            trabajo_en_impresion=cola_impresion.suprimir()#Atiendo un trabajo
            tiempo_restante=trabajo_en_impresion.dar_requerido()
            espera_trabajos+=trabajo_en_impresion.set_espera(reloj)#Acumulo el tiempo que lleva esperando el trabajo

            if tiempo_restante>5:#El tiempo que requiere el trabajo es mayor al que puede atender la impresora
                trabajo_en_impresion.imprimir(tiempo_atencion_impresora)#Le resto el tiempo requerido lo que la impresora puede atender
                tiempo_atencion_impresora=0#la impresora estara ocupada 5 minutos
                trabajo_en_impresion.actualizar_ingreso(reloj)
                cola_impresion.insertar(trabajo_en_impresion)#El trabajo vuelve a la cola
                
            elif (tiempo-reloj)>=tiempo_restante<=5:# Si tiempo restante <= al tiempo de atencion de impresora y es <= tiempo restante de simulacion
                tiempo_atencion_impresora=tiempo_atencion_impresora-trabajo_en_impresion.dar_requerido()#La impresora estara ocupada solo el tiempo necesario
                trabajos_impresos+=1
  
        reloj+=1  
        
        if tiempo_atencion_impresora<5:#Si impresora esta ocupada
            tiempo_atencion_impresora+=1
  
    #Cuento los que quedaron sin terminar
    sin_imprimir=0
    while cola_impresion.vacia()==False:
        cola_impresion.suprimir()
        sin_imprimir+=1

    print(f"Pomedio de espera de trabajos impresos: {espera_trabajos/trabajos_impresos:.2f} min")
    print(f"Trabajos sin imprimir: {sin_imprimir}")