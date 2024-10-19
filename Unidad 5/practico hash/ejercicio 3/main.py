from random import randint
from clase_hash import tabla_hash

if __name__ == '__main__':
    tabla=tabla_hash(1009)
    for i in range(1000):
        tabla.insertar(randint(20000000, 50000000))
        
    tabla.recorrer()