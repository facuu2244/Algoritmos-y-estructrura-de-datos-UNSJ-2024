from clase_nodo import nodo

class arbol:
    __raiz:nodo
    
    
    def __init__(self):
        self.__raiz=None


    def dar_raiz(self):
        return self.__raiz
    
    
    def buscar(self, elemento):#recibe clave a buscar
        if self.__raiz!=None:
            aux_raiz=self.__raiz
            
            while aux_raiz!=None and aux_raiz.dar_elemento()!=elemento:#recorre arbol
                if elemento<aux_raiz.dar_elemento():
                    aux_raiz=aux_raiz.dar_izq()#baja por izquierda
                    
                elif elemento>aux_raiz.dar_elemento():
                    aux_raiz=aux_raiz.dar_der()#baja por derecha
                    
            if aux_raiz==None:#salio del while por primera condicion, no se encontro
                return None
            else:#salio del while por segunda condicion, se encontro
                return aux_raiz
        
        else:
            return "Arbol vacio"
    
    
    def dar_infimo(self, aux_raiz):
        infimo=aux_raiz.dar_izq()#tomo el menor de los hijos del nodo a eliminar
        anterior=aux_raiz #padre del nodo a eliminar
        while infimo.dar_der()!=None:
            anterior=infimo
            infimo=infimo.dar_der()
            
        return infimo, anterior
    
    
    def insertar(self, elemento, aux_raiz=None):#auz_raiz=None si no se envia por parametro, esta vacio
        if aux_raiz == None:
            aux_raiz = self.__raiz 
        
        if self.__raiz==None:#inserta por raiz, si el arbol esta vacio
            un_nodo=nodo(elemento)
            self.__raiz=un_nodo
            
        else:
            if elemento<aux_raiz.dar_elemento():#elemento a insertar menor al de la raiz
                if aux_raiz.dar_izq()==None:#izquiero vacio, inserta en izquierdo
                    un_nodo=nodo(elemento)
                    aux_raiz.cargar_izq(un_nodo)
                else:
                    self.insertar(elemento,aux_raiz.dar_izq())#baja por lado izquierdo del arbol

            elif elemento>aux_raiz.dar_elemento():#elemento a insertar mayor al de la raiz
                if aux_raiz.dar_der()==None:#derecho vacio, inserta en derecho
                    un_nodo=nodo(elemento)
                    aux_raiz.cargar_der(un_nodo)
                else:
                    self.insertar(elemento,aux_raiz.dar_der())#baja por lado derecho del arbol

            else:
                print("el dato ya esta en el arbol")
              
                
    def suprimir_v1(self, elemento):#cambia los punteros del padre del nodo a eliminar
        if self.__raiz!=None:
            aux_raiz=self.__raiz
            anterior=aux_raiz#tengo el padre del nodo a eliminar para cambiar los punteros
            while aux_raiz!=None and aux_raiz.dar_elemento()!=elemento:#recorro el arbol
                if elemento<aux_raiz.dar_elemento():
                    anterior=aux_raiz
                    aux_raiz=aux_raiz.dar_izq()
                elif elemento>aux_raiz.dar_elemento():
                    anterior=aux_raiz
                    aux_raiz=aux_raiz.dar_der()
          
            if aux_raiz==None:#salio por primera condicion
                return "No se encontro elemento"
      
            else:#segunda condicion del while
                #guardo hijos del nodo padre del que quiero eliminar (su hermano en caso de tener).
                anterior_hijo_izq=anterior.dar_izq()
                anterior_hijo_der=anterior.dar_der()
          
                #verifico cuantos hijos tiene el nodo a eliminar
                if aux_raiz.dar_izq()==None and aux_raiz.dar_der()==None:#no tiene hijos
                    if anterior_hijo_der!=None and anterior_hijo_der.dar_elemento()==elemento:#elimino hijo derecho
                        anterior.cargar_der(None)
                    elif anterior_hijo_izq!=None and anterior_hijo_izq.dar_elemento()==elemento:#elimino hijo izquierdo
                        anterior.cargar_izq(None)
                elif aux_raiz.dar_izq()!=None and aux_raiz.dar_der()==None:#tiene un hijo izquierdo
                    if anterior_hijo_der!= None and anterior_hijo_der.dar_elemento()==elemento:#elimino hijo derecho del padre
                        anterior.cargar_der(aux_raiz.dar_izq())
                    elif anterior_hijo_izq!=None and anterior_hijo_izq.dar_elemento()==elemento:#elimino hijo izquierdo del padre
                        anterior.cargar_izq(aux_raiz.dar_izq())
              
                elif aux_raiz.dar_der()!=None and aux_raiz.dar_izq()==None:#tiene un hijo derecho
                    if anterior_hijo_der!= None and anterior_hijo_der.dar_elemento()==elemento:#elimino hijo derecho del padre
                        anterior.cargar_der(aux_raiz.dar_der())
                    elif anterior_hijo_izq!=None and anterior_hijo_izq.dar_elemento()==elemento:#elimino hijo izquierdo del padre
                        anterior.cargar_izq(aux_raiz.dar_der())
              
                else:#tiene 2 hijos
                    infimo, padre_infimo=self.dar_infimo(aux_raiz)#busco el mayor de los hijos menores
                    aux_raiz.cargar_elemento(infimo.dar_elemento())#reemplazo el nodo a eliminar
              
                    #cambio los punteros del padre del infimo
                    if infimo.dar_elemento() > padre_infimo.dar_elemento():
                        padre_infimo.cargar_der(None)
                    else:
                        padre_infimo.cargar_izq(None)
      
        else:
            return "Arbol vacio"
        
        
    def suprimir_v2(self, elemento):#cambia el contenido del nodo a eliminar
        if self.__raiz!=None:
            aux_raiz=self.__raiz
            anterior=aux_raiz#tengo el padre del nodo a eliminar para cambiar los punteros
            while aux_raiz!=None and aux_raiz.dar_elemento()!=elemento:#recorro el arbol
                if elemento<aux_raiz.dar_elemento():
                    anterior=aux_raiz
                    aux_raiz=aux_raiz.dar_izq()
                elif elemento>aux_raiz.dar_elemento():
                    anterior=aux_raiz
                    aux_raiz=aux_raiz.dar_der()
          
            if aux_raiz==None:#salio por primera condicion
                return "No se encontro elemento"
            else:#segunda condicion del while
                #verifico cuantos hijos tiene el nodo a eliminar
                if aux_raiz.dar_izq()==None and aux_raiz.dar_der()==None:#no tiene hijos
                    if elemento > anterior.dar_elemento():
                        anterior.cargar_der(None)
                    else:
                        anterior.cargar_izq(None)
                elif (aux_raiz.dar_izq() != None and aux_raiz.dar_der() == None) or (aux_raiz.dar_izq() == None and aux_raiz.dar_der() != None): #tiene un hijo
                    if aux_raiz.dar_der() != None: #busco el hijo, si es el de la derecha
                        hijo= aux_raiz.dar_der()
                    else:#es el izquierdo
                        hijo= aux_raiz.dar_izq()
                    #cambio los datos del nodo a suprumir por los del hijo
                    aux_raiz.cargar_elemento(hijo.dar_elemento())
                    aux_raiz.cargar_der(hijo.dar_der())
                    aux_raiz.cargar_izq(hijo.dar_izq())
                  
                else:#tiene 2 hijos
                    infimo, padre_infimo=self.dar_infimo(aux_raiz)#busco el mayor de los hijos menores
                    aux_raiz.cargar_elemento(infimo.dar_elemento())#reemplazo el nodo a eliminar
              
                    #cambio los punteros del padre del infimo
                    if infimo.dar_elemento() > padre_infimo.dar_elemento():
                        padre_infimo.cargar_der(None)
                    else:
                        padre_infimo.cargar_izq(None)
      
        else:
            return "Arbol vacio"
    
    
    def hijo(self, hijo, padre):#recibe las claves de los nodos, y no el nodo como tal
        nodo_padre=self.buscar(padre)#busca nodo padre

        if nodo_padre!=None:#si existe, trae a sus hijos
            hijo_izq=nodo_padre.dar_izq()
            hijo_der=nodo_padre.dar_der()
            
            if hijo_izq!=None and hijo==hijo_izq.dar_elemento():#es hijo
                return True
            if hijo_der!=None and hijo==hijo_der.dar_elemento():#es hijo
                return True
            else:#no es hijo
                return None
  
        else:
            return "No se encontro al nodo padre"
        
        
    def padre(self, padre, hijo):#recibe las claves de los nodos, y no el nodo como tal
        nodo_padre=self.buscar(padre)
        
        if nodo_padre!=None:#si existe el padre, trae a sus hijos
            hijo_izq=nodo_padre.dar_izq()
            hijo_der=nodo_padre.dar_der()
            
            #alguno de sus hijos es igual al hijo ingresado por parametro, el nodo es padre
            if hijo_izq!=None and hijo==hijo_izq.dar_elemento():
                return True
            if hijo_der!=None and hijo==hijo_der.dar_elemento():
                return True
            else:
                return False
                
        else:
            return "No se encontro al nodo padre"
        
        
    def nivel(self, elemento):
        if self.__raiz!=None:
            aux_raiz=self.__raiz
            nivel=0#Si se devuelve 0, el elemento esta en la raiz

            while aux_raiz!=None and aux_raiz.dar_elemento()!=elemento:#recorre el arbol segun corresponda
                if elemento<aux_raiz.dar_elemento():
                    aux_raiz=aux_raiz.dar_izq()
                elif elemento>aux_raiz.dar_elemento():
                    aux_raiz=aux_raiz.dar_der()
                nivel+=1
                
            if aux_raiz!=None:#salio por la segunda condicion del while
                return nivel
            else:
                return "no encotrado"
            
        else:
            return "Arbol vacio"

    
    def altura(self, nodo):
        if nodo is None:
            return -1
        else:
            altura_izquierda = 1+self.altura(nodo.dar_izq())
            altura_derecha = 1+self.altura(nodo.dar_der())
        return max(altura_izquierda, altura_derecha)
    
    
    def camino(self, comienzo, final):#recibe claves de nodos comienzo y final
        if self.__raiz!=None:
            #busca ambos nodos
            nodo_comienzo=self.buscar(comienzo)#se movera hasta llegar al final, similar a aux_raiz
            nodo_final=self.buscar(final)
            
            if nodo_comienzo!=None and nodo_final!=None:#si ambos existen
                camino="" #cadena que representa el camino, se devuelve vacia si no exite camino entre los nodos. 0=izquierda ; 1=derecha
                while nodo_comienzo!=None and nodo_comienzo!=nodo_final:
                    if nodo_final.dar_elemento()<nodo_comienzo.dar_elemento():
                        nodo_comienzo=nodo_comienzo.dar_izq()#Baja por izquierda
                        camino+="0 "#concatena 0 a la cadena camino
                    elif nodo_final.dar_elemento()>nodo_comienzo.dar_elemento():
                        nodo_comienzo=nodo_comienzo.dar_der()
                        camino+="1 "#concatena 1 a la cadena camino
                        
                if nodo_comienzo==nodo_final:#salio por segunda condicion
                    return camino
                else:
                    return None
        else:
            return "Arbol vacio"
        
        
    def inorden(self, aux_raiz):
        if aux_raiz!=None:
            self.inorden(aux_raiz.dar_izq())
            
            print(aux_raiz.dar_elemento())
            
            self.inorden(aux_raiz.dar_der())
            
    
    def preorden(self, aux_raiz):
        if aux_raiz!=None:
            print(aux_raiz.dar_elemento())
            self.preorden(aux_raiz.dar_izq())
            self.preorden(aux_raiz.dar_der())
            
    
    def postorden(self, aux_raiz):
        if aux_raiz!=None:
            self.postorden(aux_raiz.dar_izq())
            self.postorden(aux_raiz.dar_der())
            print(aux_raiz.dar_elemento())