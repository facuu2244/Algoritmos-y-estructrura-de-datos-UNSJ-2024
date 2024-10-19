import numpy as np
from clase_bucket import bucket

class tabla_hash:
    __arreglo:np.array
    __tamano:int
    __indice_overflow:int#Indice donde empieza area overflow
    
    
    def __init__(self, tamano_tabla, tamano_bucket):
        self.__tamano=int(tamano_tabla*1.2)#tamaño +20% para overflow
        self.__indice_overflow=tamano_tabla#overflow empieza en ultimo indice de la tabla
        
        self.__arreglo=np.zeros(self.__tamano, dtype=object)#arreglo de buckets
        for i in range(self.__tamano):
            self.__arreglo[i]=bucket(tamano_bucket)
    

    def metodo_extraccion(self, clave):#Extraera los digitos centrales de la clave
        clave_cadena=str(clave)
        longitud=len(clave_cadena)
        #calculo el indice desde y hasta donde cortare la cadena
        inicio=(longitud//2)-2      
        fin=(longitud//2)+1
        #corto la cadena y la convierto en entero
        indice=int(clave_cadena[inicio:fin])
        return indice%self.__indice_overflow
    
    
    def insertar(self, clave):
        indice=self.metodo_extraccion(clave)
        
        if self.__arreglo[indice].insertar(clave)==True:
            print("Insertado en bucket")
                        
        else:
            #voy a recorrer el area de overflow
            aux_indice_overflow=self.__indice_overflow
            while self.__arreglo[aux_indice_overflow].disponible()==False:#bucket overflow no libre 
                aux_indice_overflow+=1
            self.__arreglo[aux_indice_overflow].insertar(clave)
            print("Insertado en overflow")

    
    def buscar(self, clave):
        indice=self.metodo_extraccion(clave)
        
        if self.__arreglo[indice].dar_contador()!=0:
            if self.__arreglo[indice].overflow()==False or self.__arreglo[indice].buscar_en_bucket(clave):
                print(f"Encontrado: {clave} en tabla")
            else:
                indice=self.__indice_overflow
                band=False
                while indice<self.__tamano and band==False:
                    if self.__arreglo[indice].buscar_en_bucket(clave)==True:
                        band=True
                    indice+=1
                if band==True:
                    print(f"Encontrado: {clave} overflow")
                else:
                    print("No encontrado overflow")
        else:
            print("No encontrado, bucket vacio")
              
                                
    def recorrer(self):
        #primero muestro la tabla
        print("-----TABLA-----")
        for i in range(self.__indice_overflow):
            if self.__arreglo[i].dar_contador()!=0:#si hay al menos un elemento en bucket
                    print(f"Bucket numero (indice): {i}")
                    print(f"{self.__arreglo[i].mostrar()}")
                    
        #luego el area de overflow
        print("\n-----OVERFLOW-----")
        i+=1#i por el for ya esta en el area de overflow
        while i < self.__tamano:
            if self.__arreglo[i].dar_contador()!=0:
                print(f"Bucket numero (indice): {i}")
                print(f"{self.__arreglo[i].mostrar()}")
            i+=1