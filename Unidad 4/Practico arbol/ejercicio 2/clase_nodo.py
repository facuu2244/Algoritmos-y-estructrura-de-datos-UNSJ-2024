class nodo:
    __elemento:object
    __izquierdo:object
    __derecho:object
   
    def __init__(self,elemento):
        self.__elemento=elemento
        self.__izquierdo=None
        self.__derecho=None

    def cargar_izq(self, puntero):
        self.__izquierdo=puntero
        return self.__izquierdo
    def cargar_der(self, puntero):
        self.__derecho=puntero
        return self.__derecho
    
    def dar_elemento(self):
        return self.__elemento
    def dar_der(self):
        return self.__derecho
    def dar_izq(self):
        return self.__izquierdo
    
    