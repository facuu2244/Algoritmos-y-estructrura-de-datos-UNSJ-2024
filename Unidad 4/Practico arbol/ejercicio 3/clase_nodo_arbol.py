class nodo:
    __elemento:object
    __frecuencia:int
    __izquierdo:object
    __derecho:object
   
    def __init__(self,elemento, frecuencia=0):
        self.__elemento=elemento
        self.__frecuencia=frecuencia
        self.__izquierdo=None
        self.__derecho=None
        
    
    def __gt__(self, otro):
        if self.__frecuencia>otro.__frecuencia:
            return True
        elif self.__frecuencia==otro.__frecuencia:
            if self.__elemento>otro.__elemento:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, otro):
        if self.__frecuencia<otro.__frecuencia:
            return True
        elif self.__frecuencia==otro.__frecuencia:
            if self.__elemento<otro.__elemento:
                return True
            else:
                return False
        else:
            return False
        
    def __add__(self, otro):
        nodo_sumado=nodo(self.__elemento+otro.__elemento, self.__frecuencia+otro.__frecuencia)
        if self.__frecuencia>otro.__frecuencia:
            nodo_sumado.cargar_der(self)
            nodo_sumado.cargar_izq(otro)
        
        elif self.__frecuencia==otro.__frecuencia:
            if self.__elemento>otro.__elemento:
                nodo_sumado.cargar_der(self)
                nodo_sumado.cargar_izq(otro)
                
            else:
                nodo_sumado.cargar_izq(self)
                nodo_sumado.cargar_der(otro)
                
        else:
            nodo_sumado.cargar_izq(self)
            nodo_sumado.cargar_der(otro)
        
        return nodo_sumado
        
    def cargar_elemento(self, elemento):
        self.__elemento=elemento
    def cargar_frecuencia(self, frecuencia):
        self.__frecuencia=frecuencia
    def cargar_izq(self, puntero):
        self.__izquierdo=puntero
        return self.__izquierdo
    def cargar_der(self, puntero):
        self.__derecho=puntero
        return self.__derecho
    
    def dar_elemento(self):
        return self.__elemento
    def dar_frecuencia(self):
        return self.__frecuencia
    def dar_der(self):
        return self.__derecho
    def dar_izq(self):
        return self.__izquierdo
    
    