import numpy as np

class bucket:
    __arreglo:np.array
    __contador:int
    
    def __init__(self, tamano):
        self.__arreglo=np.zeros(tamano, dtype=object)
        self.__contador=0

        
    def dar_contador(self):
        return self.__contador
    
    def disponible(self):
        return self.__contador<len(self.__arreglo)
    
    def overflow(self):
        return self.__contador>len(self.__arreglo)#true si hay elementos en overflow
    
    def insertar(self, clave):
        if self.__contador<len(self.__arreglo):#Hay espacio en el bucket
            self.__arreglo[self.__contador]=clave
            self.__contador+=1
            return True
        else:
            self.__contador+=1#aumento contador para saber que hay un elemento en overflow
            return "overflow"
        

    def buscar_en_bucket(self, clave):
        indice=0
        band=False
        while indice<len(self.__arreglo) and band==False:
            if self.__arreglo[indice]==clave:
                band=True
            indice+=1
            
        if band==True:
            return True
        else:
            return False


    def mostrar(self):
        for i in self.__arreglo:
            print(f"bucket {i}")
        
        return ""