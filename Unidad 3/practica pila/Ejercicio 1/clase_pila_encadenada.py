from clase_nodo import nodo

class pila:
    __comienzo:nodo#comienzo=tope
    __cantidad:int

    def __init__(self):
        self.__comienzo=None
        self.__cantidad=0

    def insertar(self,elemento):
        self.__cantidad += 1
        un_nodo = nodo(elemento)
        un_nodo.set_siguiente(self.__comienzo) 
        self.__comienzo = un_nodo

    def suprimir(self):
        if self.__comienzo is None:
            return None
        else:
            self.__cantidad-=1
            valor=self.__comienzo.dar_contenido()
            self.__comienzo=self.__comienzo.dar_siguiente()
            return valor

    def recorrer(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.dar_contenido())
            aux=aux.dar_siguiente()
        
    def vacia(self):
        if self.__cantidad==0:
            return True
        else:
            return False