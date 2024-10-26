import numpy

class cola:
    __cola:numpy.empty
    __primero:int
    __ultimo:int
    __cantidad:int
    __max:int
    
    def __init__(self, maximo):
        self.__cantidad=0 
        self.__max=maximo
        self.__cola=numpy.empty(self.__max, dtype=int)
        self.__primero=0
        self.__ultimo=0
          
    def insertar(self, elemento):
        if self.llena():
            print("La cola esta llena")
        else: 
            self.__cola[self.__ultimo]=elemento
            self.__ultimo=(self.__ultimo+1)%self.__max
            self.__cantidad+=1
            
    def suprimir(self):
        if self.vacia():
            return None  
        else:
            valor=self.__cola[self.__primero]
            self.__primero=(self.__primero+1)%self.__max
            self.__cantidad-=1
            return valor
    
    def recorrer(self):
        if self.vacia()==False:
            i=self.__primero
            for j in range(self.__cantidad):
                print(self.__cola[i])
                i=(i+1)%self.__max

    
    def llena(self):
        return self.__cantidad==self.__max
    def vacia(self):
        return self.__cantidad==0