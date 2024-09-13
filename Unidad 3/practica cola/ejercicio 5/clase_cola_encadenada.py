from clase_nodo import nodo

class cola:
    __cantidad:int
    __primero:nodo
    __ultimo:nodo
    
    def __init__(self):
        self.__cantidad=0
        self.__primero=None
        self.__ultimo=None
        
    def vacia(self):
        return self.__cantidad==0    
        
    def insertar(self, elemento):
        un_nodo=nodo(elemento)
        
        if self.__ultimo==None:
            self.__primero=un_nodo
        else:
            self.__ultimo.set_siguiente(un_nodo)
        self.__ultimo=un_nodo
        self.__cantidad+=1
        
    def suprimir(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            elemento=self.__primero.dar_contenido()
            self.__primero=self.__primero.dar_siguiente()
            self.__cantidad-=1
            return elemento

    def dar_primero(self):
        return self.__primero
    
    def recorrer(self, aux):
        if aux!=None:
            print(aux.dar_contenido())
            self.recorrer(aux.dar_siguiente())