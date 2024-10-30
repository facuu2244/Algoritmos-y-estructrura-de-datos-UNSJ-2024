import numpy as np
from clase_cola_secuencial import cola

class digrafo_p:
    __matriz_adyacencia:np.array
    __vertices:list
    __tiempo:int
    
    def __init__(self, vertices, aristas):
        self.__matriz_adyacencia=np.full((len(vertices), len(vertices)), float("inf")) #para poder usasr el algoritmo de floyd
        self.__vertices=vertices
        self.__tiempo=0
    
        for a in aristas:
            self.__matriz_adyacencia[a[0]][a[1]]=a[2] #inserto el peso entre los vertices
            
        print("--------------Matriz de pesos--------------")
        print(self.__matriz_adyacencia)
        
    def buscar_indice(self, vertice):
        i=0
        band=False
        while band!=True and i<len(self.__vertices):
            if self.__vertices[i]==vertice:
                band=True
            i+=1
        
        if band==True:
            return i-1
        else:
            
            return band
        
        
    #recorrido en amplitud
    def REA(self, v_origen):
        vertices_visitados=[float("inf")]*len(self.__vertices)
            
        indice_origen=self.buscar_indice(v_origen)
        vertices_visitados[indice_origen]=0
        cola_secuencial=cola(len(self.__vertices))
        cola_secuencial.insertar(indice_origen)#inserto el vertice origen en la cola
        
        while cola_secuencial.vacia()!=True:
            v=cola_secuencial.suprimir()
            for u in range(len(self.__vertices)):
                if self.__matriz_adyacencia[v][u]!=float("inf") and vertices_visitados[u]==float("inf"):
                    vertices_visitados[u]=vertices_visitados[v]+1
                    cola_secuencial.insertar(u)
                
        return vertices_visitados 
        
    
    def REP_Visita(self, v, t_descubierto, t_finalizacion):
        self.__tiempo += 1
        t_descubierto[v] = self.__tiempo  # marco el vértice como descubierto con el tiempo en el que se encontro
        print(f"Visitando nodo {v}, tiempo de descubrimiento: {self.__tiempo}")

        #recorro los adyacentes de "v"
        for u in range(len(self.__vertices)):
            if self.__matriz_adyacencia[v][u]!=float("inf") and t_descubierto[u] == 0:
                self.REP_Visita(u, t_descubierto, t_finalizacion)
        
        self.__tiempo += 1
        t_finalizacion[v] = self.__tiempo  #marco el tiempo de finalización del vertice "v"
        print(f"Finalizando nodo {v}, tiempo de finalización: {self.__tiempo}")

    def REP(self):
        # inicializo tiempos de descubrimiento y finalización
        t_descubierto= [0] * len(self.__vertices)
        t_finalizacion = [0] * len(self.__vertices)

        #para cada vértice no sido visitado, ejecutar REP_visita
        for v in range(len(self.__vertices)):
            if t_descubierto[v] == 0:
                self.REP_Visita(v, t_descubierto, t_finalizacion)
        
        print("Tiempos de descubrimiento:", t_descubierto)
        print("Tiempos de finalización:", t_finalizacion)
        self.__tiempo=0#reinicio el tiempo para futuros REP
        
        
    def adyacentes(self, vertice):
        indice=self.buscar_indice(vertice)#obtengo el indice asociado al vertice
        
        for u in range(len(self.__vertices)):
            if self.__matriz_adyacencia[indice][u]!=float("inf"):
                print(self.__vertices[u])
            
            
    #reconstruir el camino a partir del arreglo de predecesores
    def reconstruir_camino(self, camino, origen, destino):
        resultado=[]
        actual=destino
        
        #retrocedo desde el destino hasta el origen
        while actual!=-1:
            resultado.insert(0, self.__vertices[actual])#inserto al inicio del arreglo el vertice actual
            actual=camino[actual]
        
        if resultado[0] != self.__vertices[origen]:#si no se llega al origen, no hay un camino válido
            print(f"No hay camino de {self.__vertices[origen]} a {self.__vertices[destino]}")
            return False

        print(resultado)
        return True
        
        
    def camino(self, origen, destino):
        camino=[-1]*len(self.__vertices)#arreglo de predecesores para luego reconstruir el camino desde el destino al origen
        vertices_visitados=[float("inf")]*len(self.__vertices)

        
        indice_origen=self.buscar_indice(origen)
        indice_destino=self.buscar_indice(destino)
  
        cola_secuencial=cola(len(self.__vertices))
        cola_secuencial.insertar(indice_origen)
        vertices_visitados[indice_origen]=0#marco como visitado
        
        while cola_secuencial.vacia()!=True:
            v=cola_secuencial.suprimir()
 
            if v==indice_destino:#se llego al vertice destino
                return self.reconstruir_camino(camino, indice_origen, indice_destino)
            else:
                #recorro los adyacentes a "v"
                for i in range(len(self.__vertices)):
                    if self.__matriz_adyacencia[v][i]!=float("inf") and vertices_visitados[i]==float("inf"):
                        vertices_visitados[i]=0
                        camino[i]=v#agrego "v" como predecesor del siguiente vertice
                        cola_secuencial.insertar(i)
                        
        #sale del while sin encontrar el destino
        print(f"No hay camino de {origen} a {destino}")
        return False
        
        
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
    
    
    def obtener_transpuesto(self):
        #crea el grafo transpuesto invirtiendo las aristas
        transpuesto = digrafo_p(self.__vertices, []) #matriz de 0s en consola por print() en __init__
        for i in range(len(self.__vertices)):
            for j in range(len(self.__vertices)):
                if self.__matriz_adyacencia[i][j] != float("inf"):
                    transpuesto.__matriz_adyacencia[j][i] = self.__matriz_adyacencia[i][j]
                    
        return transpuesto
    
    def fuertemente_conexo(self):
        #recorre el grafo original desde el vertice 0
        visitados_original = self.REA(0)
        if float("inf") in visitados_original:
            return False  #no es fuertemente conexo
    
        #recorre el grafo transpuesto
        grafo_transpuesto = self.obtener_transpuesto()
        visitados_transpuesto = grafo_transpuesto.REA(0)
        if float("inf") in visitados_transpuesto:
            return False  #no es fuertemente conexo

        return True  #es fuertemente conexo


    def es_debilmente_conexo(self):
        #crea el grafo no dirigido eliminando las direcciones de las aristas
        no_dirigido = digrafo_p(self.__vertices, [])#matriz de 0s en consola por print() en __init__
        for i in range(len(self.__vertices)):
            for j in range(len(self.__vertices)):
                if self.__matriz_adyacencia[i][j] != float("inf"):
                    no_dirigido.__matriz_adyacencia[i][j] = self.__matriz_adyacencia[i][j]
                    no_dirigido.__matriz_adyacencia[j][i] = self.__matriz_adyacencia[i][j]

                elif self.__matriz_adyacencia[j][i] != float("inf"):
                    no_dirigido.__matriz_adyacencia[i][j] = self.__matriz_adyacencia[j][i]
                    no_dirigido.__matriz_adyacencia[j][i] = self.__matriz_adyacencia[j][i]
        #recorre el grafo no dirigido
        visitados_no_dirigido = no_dirigido.REA(0)
        if float("inf") in visitados_no_dirigido:
            return False  # Es disconexo

        return True  # Es débilmente conexo

    def conexo_2(self):
        if self.fuertemente_conexo():
            print("El grafo es fuertemente conexo")
        elif self.es_debilmente_conexo():
            print("El grafo es simple conexo")
        else:
            print("El grafo es disconexo")
            
    
    def aciclico_visita(self, v, descubiertos):
        descubiertos[v] = 1 #marco el vértice como en proceso de visita
        
        #recorro los adyacentes de "v"
        for u in range(len(self.__vertices)):
            if self.__matriz_adyacencia[v][u]!=float("inf"):
                if descubiertos[u] == 0:
                    if self.aciclico_visita(u, descubiertos):#avanzo por vertice adyacente
                        return True #para el if de la llamada anterior
                elif descubiertos[u]==1:
                    return True #para detener el for, se encontro un ciclo, se llego al vertice que esta en proceso de visita
            
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
        
        
    def algoritmo_floyd(self):
        matriz_distancias = self.__matriz_adyacencia
        
        for k in range(len(matriz_distancias)):
            for i in range(len(matriz_distancias)):
                for j in range(len(matriz_distancias)):
                    matriz_distancias[i][j] = min(matriz_distancias[i][j], matriz_distancias[i][k] + matriz_distancias[k][j])
        
        for i in range(len(matriz_distancias)):
            self.__matriz_adyacencia[i][i]=None
        return matriz_distancias