#las operaciones son analogas a las de grafo en representacion secuencial, reemplazando el metodo de recorrido de vertices adyacentes
import numpy as np
from clase_lista_encadenada_contenido import lista_encadenada_contenido
from clase_cola_secuencial import cola

class grafo_encadenada:
    __arreglo:np.array
    __vertices:list
    __tiempo:int #para REP. No es parte del objeto de dato
    
    
    def __init__(self, vertices, aristas):
        self.__arreglo=np.empty(len(vertices), dtype=object)
        self.__vertices=vertices
        self.__tiempo=0
        
        #cada vertice (componente del arreglo) sera una lista encadenada de adyacentes
        for i in range(len(self.__arreglo)):
            self.__arreglo[i]=lista_encadenada_contenido()
            
        #cargo los adyacentes
        for a in aristas:
            #insertara numeros, que se usaran como indices de self.__vertices
            self.__arreglo[a[0]].insertar(a[1])
            self.__arreglo[a[1]].insertar(a[0])
    
    
    def buscar_indice(self, vertice):
        i=0
        band=False
        while band!=True and i<=len(self.__arreglo):
            if self.__vertices[i]==vertice:
                band=True
            i+=1
        
        if band==True:
            return i-1
        else:
            return band
    
    
    def REA(self, v_origen):
        vertices_visitados=[float("inf")]*len(self.__arreglo)
   
        indice_origen=self.buscar_indice(v_origen)#busco el indice que tiene el vertice en el arreglo self.__vertices
        vertices_visitados[indice_origen]=0#lo marco como vertice de origen
        cola_secuencial=cola(len(self.__vertices))#creo cola con tamaño para guardar todos los vertices en caso de requerirlo
        cola_secuencial.insertar(indice_origen)#inserto el vertice origen en la cola

        while cola_secuencial.vacia()!=True:
            v=cola_secuencial.suprimir()
            #recorro la lista enlazada correspondiente al vertice "v"
            aux=self.__arreglo[v].dar_cabeza()
            while aux!=None:
                adyacente=aux.dar_contenido()#adyacente a "v"
                if vertices_visitados[adyacente]==float("inf"):#el adyacente no fue visitado
                    vertices_visitados[adyacente]=vertices_visitados[v]+1
                    cola_secuencial.insertar(adyacente)
                aux=aux.dar_siguiente()#avanzo en la lista. dar_siguiente() metodo de clase "nodo"
        print(vertices_visitados)
       
       
    def REP_visita(self, v, t_descubierto,t_finalizacion):
        self.__tiempo+=1
        t_descubierto[v]=self.__tiempo
        print(f"Visitando nodo {v}, tiempo de descubrimiento: {self.__tiempo}")
        
        #recorro los adyacentes a "v"
        aux=self.__arreglo[v].dar_cabeza()
        while aux!=None:
            adyacente=aux.dar_contenido()
            if t_descubierto[adyacente]==0:
                self.REP_visita(adyacente, t_descubierto, t_finalizacion)
            aux=aux.dar_siguiente()
                
        self.__tiempo+=1
        t_finalizacion[v]=self.__tiempo
        print(f"Finalizando nodo {v}, tiempo de finalización: {self.__tiempo}")
        
        
    def REP(self):
        # inicializo tiempos de descubrimiento y finalización
        t_descubierto=[0]*len(self.__arreglo)
        t_finalizacion=[0]*len(self.__arreglo)
        
        for v in range(len(self.__arreglo)):
            if t_descubierto[v]==0:
                self.REP_visita(v, t_descubierto,t_finalizacion)
                
        print("Tiempos de descubrimiento:", t_descubierto)
        print("Tiempos de finalización:", t_finalizacion)
        self.__tiempo=0#reinicio el tiempo para futuros REP
    
    
    def adyacentes(self, vertice):
        indice_origen=self.buscar_indice(vertice)
        aux=self.__arreglo[indice_origen].dar_cabeza()
        while aux!=None:
            adyacente=aux.dar_contenido()#indice del vertice adyacente en self.__vertices
            print(self.__vertices[adyacente])
            aux=aux.dar_siguiente()
        
    
    #reconstruir el camino a partir del arreglo de predecesores
    def reconstruir_camino(self, camino, origen, destino):
        resultado=[]
        actual=destino
        
        #retrocedo desde el destino hasta el origen
        while actual!=-1:
            resultado.insert(0, self.__vertices[actual])#inserto al inicio del arreglo el vertice actual
            actual=camino[actual]
        
        if resultado[0] != self.__vertices[origen]:#si no se llega al origen, no hay un camino válido
            return print(f"No hay camino de {self.__vertices[origen]} a {self.__vertices[destino]}")
        
        return print(resultado)
    
    
    def camino(self, origen, destino):
        camino=[-1]*len(self.__arreglo)#arreglo de predecesores para luego reconstruir el camino desde el destino al origen
        vertices_visitados=[float("inf")]*len(self.__arreglo)
      
        indice_origen=self.buscar_indice(origen)
        indice_destino=self.buscar_indice(destino)
  
        cola_secuencial=cola(len(self.__arreglo))
        cola_secuencial.insertar(indice_origen)
        vertices_visitados[indice_origen]=0#marco como visitado
        
        while cola_secuencial.vacia()!=True:
            v=cola_secuencial.suprimir()
 
            if v==indice_destino:#se llego al vertice destino
                return self.reconstruir_camino(camino, indice_origen, indice_destino)
            else:
                #recorro los adyacentes a "v"
                aux=self.__arreglo[v].dar_cabeza()
                while aux!=None:
                    adyacente=aux.dar_contenido()
                    if vertices_visitados[adyacente]==float("inf"):
                        vertices_visitados[adyacente]=0
                        camino[adyacente]=v#agrego "v" como predecesor del siguiente vertice
                        cola_secuencial.insertar(adyacente)
                    aux=aux.dar_siguiente()
        #sale del while sin encontrar el destino
        print(f"No hay camino de {origen} a {destino}")
    
    
    def conexo(self):
        visitados=[float("inf")]*len(self.__arreglo)
        
        visitados[0]=0#comienzo visitando el primer veritice
        cola_secuencial=cola(len(self.__vertices))
        cola_secuencial.insertar(0)
        
        while cola_secuencial.vacia()!=True:
            v=cola_secuencial.suprimir()
            #recorro la lista enlazada correspondiente al vertice "v"
            aux=self.__arreglo[v].dar_cabeza()
            while aux!=None:
                adyacente=aux.dar_contenido()#adyacente a "v"
                if visitados[adyacente]==float("inf"):#el adyacente no fue visitado
                    visitados[adyacente]=visitados[v]+1
                    cola_secuencial.insertar(adyacente)
                aux=aux.dar_siguiente()#avanzo en la lista. dar_siguiente() metodo de clase "nodo"
                
        if float("inf") in visitados:
            return print("El grafo NO es conexo")
        
        else:
            return print("El grafo es conexo")
        
        
    def aciclico(self):
        print("El grafo tiene ciclos pues es un grafo no dirigido")