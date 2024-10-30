#operaciones analogas a las de grafo en representacion secuencial, reemplazando el metodo de recorrido de vertices adyacentes
import numpy as np
from clase_lista_encadenada_contenido import lista_encadenada_contenido
from clase_cola_secuencial import cola

class digrafo:
    __arreglo:np.array
    __vertices:list
    
    
    def __init__(self, vertices, aristas):
        self.__vertices=vertices
        self.__arreglo=np.empty(len(vertices), dtype=object)
        
        for i in range(len(self.__arreglo)):
            self.__arreglo[i]=lista_encadenada_contenido()
            
        for a in aristas:
            #insertara numeros, que se usaran como indices de self.__vertices
            self.__arreglo[a[0]].insertar(a[1])
            
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
    
    
    def REA(self, v_origen):#recorrido en amplitud
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
                
        return vertices_visitados
       
       
    def REP_visita(self, v, t_descubierto,t_finalizacion):
        global tiempo
        tiempo+=1
        t_descubierto[v]=tiempo
        print(f"Visitando nodo {v}, tiempo de descubrimiento: {tiempo}")
        
        #recorro los adyacentes a "v"
        aux=self.__arreglo[v].dar_cabeza()
        while aux!=None:
            adyacente=aux.dar_contenido()
            if t_descubierto[adyacente]==0:
                self.REP_visita(adyacente, t_descubierto, t_finalizacion)
            aux=aux.dar_siguiente()
                
        tiempo+=1
        t_finalizacion[v]=tiempo
        print(f"Finalizando nodo {v}, tiempo de finalización: {tiempo}")
        
        
    def REP(self):#recorrido en profundidad
        # inicializo tiempos de descubrimiento y finalización
        t_descubierto=[0]*len(self.__arreglo)
        t_finalizacion=[0]*len(self.__arreglo)
        global tiempo #el tiempo sera una variable global y no un atributo
        tiempo=0
        
        for v in range(len(self.__arreglo)):
            if t_descubierto[v]==0:
                self.REP_visita(v, t_descubierto,t_finalizacion)
                
        print("Tiempos de descubrimiento:", t_descubierto)
        print("Tiempos de finalización:", t_finalizacion)
        
    
    
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
    
    
    def conexo_1(self):
        #recorre el grafo en amplitud por cada vertice  
        cont=0
        for i in self.__vertices:
            visitados=self.REA(i)
            if float("inf") in visitados:
                cont+=1
        if cont==len(self.__vertices):
            return print("El grafo es disconexo")#en todos los recorridos hubieron vertices sin visitar
        elif cont==0:
            return print("El grafo es fuertemente conexo")#nunca hubieron vertices sin visitar
        else:
            return print("El grafo simple conexo")
        
        
    def aciclico_visita(self, v, descubiertos):
        descubiertos[v] = 1 #marco el vértice como en proceso de visita
        
        #recorro los adyacentes de "v"
        aux=self.__arreglo[v].dar_cabeza()
        while aux!=None:
            adyacente=aux.dar_contenido()
            if descubiertos[adyacente] == 0:
                if self.aciclico_visita(adyacente, descubiertos):#avanzo por vertice adyacente
                    return True #para el if de la llamada anterior
            elif descubiertos[adyacente]==1:
                return True #para detener el for, se encontro un ciclo, se llego al vertice que esta en proceso de visita
            aux=aux.dar_siguiente()
            
        descubiertos[v]=2 #vertice recorrido completamente
        return False #no hay ciclos
        
    def aciclico(self):
        #arreglo con 3 estados para vertices (0 no descubierto, 1 en proceso de visita, 2 completamente visitado/recorrido)
        descubiertos = [0] * len(self.__vertices)
        
        #para cada vértice no sido visitado, ejecutar aciclico_visita
        for v in range(len(self.__vertices)):
            if descubiertos[v] == 0:
                if self.aciclico_visita(v, descubiertos)==True:#llamada a funcion recursiva
                    print("Tiene ciclos")#retorno true, se detiene el bucle
                    return

        print("No tiene ciclos")
        
        
    def grado_salida(self, vertice): #recorro la lista del vertice
        cont=0
        indice=self.buscar_indice(vertice)
        aux=self.__arreglo[indice].dar_cabeza()
        
        while aux!=None:
            cont+=1
            aux=aux.dar_siguiente()    
    
        return cont
    
    
    def grado_entrada(self, vertice): #recorro todo el arrglo y las listas para buscar entradas
        cont=0
        indice=self.buscar_indice(vertice)
        for v in self.__arreglo:
            aux=v.dar_cabeza()
            while aux!=None:
                if aux.dar_contenido()==indice:
                    cont+=1
                aux=aux.dar_siguiente()   
        
        return cont
    
    
    def nodo_fuente(self, vertice):
        grado_salida=self.grado_salida(vertice)
        grado_entrada=self.grado_entrada(vertice)
        if grado_salida>0 and grado_entrada==0:
            print("El vertice es fuente")
        else:
            print("El vertice no es fuente")
    
    
    def nodo_pozo(self, vertice):
        grado_salida=self.grado_salida(vertice)
        grado_entrada=self.grado_entrada(vertice)
        if grado_entrada>0 and grado_salida==0:
            print("El vertice es pozo")
        else:
            print("El vertice no es pozo")
            
            
    def orden_topologico(self, v, descubiertos, ordenados):
        descubiertos[v]=1
        
        aux=self.__arreglo[v].dar_cabeza()
        while aux!=None:
            if descubiertos[aux.dar_contenido()]==0:
                self.orden_topologico(aux.dar_contenido(), descubiertos, ordenados)
            aux=aux.dar_siguiente()
        ordenados.insert(0, self.__vertices[v])
    
    def REP_topologico(self): #modificacion de REP
        descubiertos=[0]*len(self.__arreglo)
        ordenados=[]
        for v in range(len(self.__arreglo)):
            if descubiertos[v]==0:
                self.orden_topologico(v, descubiertos, ordenados)
                
        print(ordenados)
   