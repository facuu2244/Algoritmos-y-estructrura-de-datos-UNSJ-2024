from random import randint
from clase_hash import tabla_hash

if __name__ == '__main__':
    #tabla=tabla_hash(1000) #tamaño de la tabla numero no primo
    tabla=tabla_hash(1009) #tamaño de la tabla numero primo
    
    # for i in range(1000):
    #     dni=randint(20000000, 50000000)
    #     tabla.insertar(dni)
    tabla.insertar("roma")
    tabla.insertar("amor")
    tabla.insertar("maro""")
    
    tabla.buscar("maro")


"""Ejecutando el programa algunas veces, obtuve como promedio de coliciones o consultas a la hora de buscar una posicion linreo:

si el tamaño de la tabla es un numero no primo (1000): 16662 consultas
si el tamaño de la tabla es un numero primo(): 15391 consultas""" 