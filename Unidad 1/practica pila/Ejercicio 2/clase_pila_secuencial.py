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
            print("La cola esta llena")
        else:
            self.__pila[self.__tope]=int(elemento)
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
            print("La pila esta vacia")
        else:
            valor=self.__pila[self.__tope-1]
            self.__pila[self.__tope-1]=None
            self.__tope=self.__tope-1
            return valor
    
    def recorrer(self):
        i=self.__tope
        
        while i!=0:
            i-=1
            print(self.__pila[i])