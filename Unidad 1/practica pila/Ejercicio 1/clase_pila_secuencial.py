import numpy

class pila:
    __pila:numpy.array
    __tope:int
    
    def __init__(self):
        self.__capacidad=50
        self.__tope=0
        self.__pila=numpy.empty(self.__capacidad)
        
    def insertar(self, elemento):
        if self.llena()==True:
            return None
        else:
            self.__pila[self.__tope]=elemento
            self.__tope+=1
        
    def llena(self):
        if self.__tope==self.__capacidad:
            return True
        else:
            return False
    def vacia(self):
        if self.__tope==0:
            return True
        else:
            return False
        
    def suprimir(self):
        if self.vacia():
            return "La pila esta vacia"
        else:
            valor=self.__pila[self.__tope-1]
            self.__pila[self.__tope-1]=None
            self.__tope=self.__tope-1
            return valor