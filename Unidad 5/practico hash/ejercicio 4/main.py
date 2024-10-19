from random import randint
from clase_hash import tabla_hash

if __name__ == '__main__':
    tabla=tabla_hash(tamano_tabla=211, tamano_bucket=5)#tamaño de tabla primo sin contar overflow
    for i in range(1000):
        tabla.insertar(randint(20000000, 50000000))
    
    #Lote de prueba fijo 
    # tabla.insertar(12345678)
    # tabla.insertar(87654321)
    # tabla.insertar(11223344)
    # tabla.insertar(11223344)
    # tabla.insertar(11223344)
    # tabla.insertar(11223344)
    # tabla.insertar(11223344)
 
    # tabla.insertar(11223344)# Colisión
    # tabla.insertar(11223344)# Colisión
    # tabla.insertar(11223344)# Colisión
    # tabla.insertar(11223344)# Colisión
    
    # tabla.insertar(44332211)
    # tabla.insertar(12344321)
    # tabla.insertar(12344322)
    # tabla.insertar(12344323)
    # tabla.insertar(12344324)
    # tabla.insertar(12344325) 
    
    # tabla.insertar(12344326) # Colisión
    # tabla.insertar(12344327) # Colisión
    # tabla.insertar(12344328) # Colisión
    
    # tabla.insertar(22334455)
    # tabla.insertar(55667788)
    # tabla.insertar(66778899)
    # tabla.insertar(77889900)
    # tabla.insertar(44556677)
    
    # tabla.buscar(44556677)
    
    #tabla.recorrer()