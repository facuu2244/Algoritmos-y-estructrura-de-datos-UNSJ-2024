import numpy as np
from clase_lista_encadenada_contenido import lista_encadenada_contenido

class tabla_hash:
    __arreglo:np.array
    __tamano:int
    
    
    def __init__(self, tamano):
        self.__tamano=tamano
        self.__arreglo=np.zeros(self.__tamano, dtype=object)


    def metodo_plegado(self, clave):#separara la clave en 2 digitos y la sumara
        indice=0
        clave_cadena=str(clave)
        #se toman los primeros 2 digitos
        inicio=0
        fin=2
        for i in range(len(clave_cadena)//2):#se repite la midad de veces de lo que mide la clave
            indice+=int(clave_cadena[inicio:fin])#sumo la cadena cortada
            inicio=fin
            fin+=2
        return indice%self.__tamano
    
    
    def insertar(self, clave):
        indice=self.metodo_plegado(clave) 
        if self.__arreglo[indice]==0:#si esta vacia
            self.__arreglo[indice]=lista_encadenada_contenido()
            self.__arreglo[indice].insertar(clave)
            
        else:
            #política manejo de colisiones encadenamiento
            self.__arreglo[indice].insertar(clave)
        
                
    def buscar(self, clave):
        indice=self.metodo_plegado(clave)
        
        if self.__arreglo[indice]==0:
            print("No encontrado")
            
        elif self.__arreglo[indice].buscar(clave)!=-1:
            print(f"Enecontrado: {clave}")
            
        else:
            print(f"No encontrado")
                                

    def recorrer(self):
        indice=0
        for i in self.__arreglo:
            if type(i)==int:
                print(f"indice: {indice}, vacio")
            else:
                print(f"indice: {indice}, valores:")
                i.recorrer()
                
            indice+=1