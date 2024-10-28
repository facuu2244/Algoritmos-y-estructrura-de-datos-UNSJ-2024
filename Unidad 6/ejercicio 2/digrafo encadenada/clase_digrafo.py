import numpy as np
from clase_lista_encadenada_contenido import lista_encadenada_contenido

class digrafo:
    __arreglo:np.array
    __vertices:list
    
    
    def __init__(self, vertices, aristas):
        self.__vertices=vertices
        self.__arreglo=np.empty(len(vertices), dtype=object)
        
        for i in range(len(self.__arreglo)):
            self.__arreglo[i]=lista_encadenada_contenido()
            
        for a in aristas:
            self.__arreglo[a[0]].insertar(a[1])
        
        
        for i in range(len(self.__arreglo)):
            print(f"vertice {i}")
            self.__arreglo[i].recorrer()