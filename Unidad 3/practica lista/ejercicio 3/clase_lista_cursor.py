import numpy
from clase_nodo import nodo

class lista_cursor:
    __max:int
    __cab:int
    __cantidad:int
    __espacio:numpy.empty
    __disponible:int
    
    def __init__(self, max):
        self.__max=max
        self.__cab=-2
        self.__cantidad=0
        self.__espacio=numpy.empty(self.__max, dtype=nodo)
        for i in range(max):
            self.__espacio[i]=nodo()
        self.__disponible=0
        
    def vacia(self):
        return self.__cantidad==0
    
    def dar_disponible(self, disp):
        i=0
        while i<self.__max and self.__espacio[i].dar_siguiente()!=-2:
            i+=1
        
        if i<self.__max:
            self.__disponible=i
            return self.__disponible
        else:
            self.__disponible=-2
            return self.__disponible

    def free_disponible(self, disp):
        if disp>=0 and disp<self.__max:
            self.__espacio[disp].set_siguiente(-2)
            return True
        else:
            return False
    
    def insertar_pos(self, elemento, posicion):#insertar por posicion
        self.__disponible=self.dar_disponible(self.__disponible)
        if self.__cantidad<self.__max and posicion>=0 and posicion<=self.__cantidad and self.__disponible!=-2:
            
            self.__espacio[self.__disponible].set_contenido(elemento)
            anterior=self.__cab
            cabeza=self.__cab
            i=0
            while i<posicion:
                i+=1
                anterior=cabeza
                cabeza=self.__espacio[cabeza].dar_siguiente()
                
            if cabeza==self.__cab:#inserta al incio de la lista
                if self.__cantidad==0:
                    self.__espacio[self.__cab].set_siguiente(-2)
                else:
                    self.__espacio[self.__disponible].set_siguiente(self.__cab)
                self.__cab=self.__disponible
                
            elif cabeza==-2:#inserta al final de la lista
                self.__espacio[self.__disponible].set_siguiente(-2)
                self.__espacio[anterior].set_siguiente(self.__disponible)
            else:
                self.__espacio[self.__disponible].set_siguiente(cabeza)
                self.__espacio[anterior].set_siguiente(self.__disponible)
                
            self.__cantidad+=1
            return True
        
        else:
            print("Espacio lleno o posición incorrecta")
            return False
        
    def insertar_conte(self, elemento):#inserta por contenido
        if self.__cantidad<self.__max and self.dar_disponible(self.__disponible):
            anterior=self.__cab
            cabeza=self.__cab
            i=0
            self.__espacio[self.__disponible].set_contenido(elemento)
            while i<self.__cantidad and cabeza!=-1 and self.__espacio[cabeza].dar_contenido()<elemento:
                i+=1
                anterior=cabeza
                cabeza=self.__espacio[cabeza].dar_siguiente()
            if cabeza==self.__cab:#insertar al inicio
                if self.__cantidad==0:#Lista vacia
                    self.__espacio[self.__cab].set_siguiente(-1)
                else:#Lista con elementos
                    self.__espacio[self.__disponible].set_siguiente(self.__cab)
                self.__cab=self.__disponible
            
            elif cabeza==-1:#Inserta al final
                self.__espacio[self.__disponible].set_siguiente(-1)
                self.__espacio[anterior].set_siguiente(self.__disponible)
                
            else:
                self.__espacio[self.__disponible].set_siguiente(cabeza)
                self.__espacio[anterior].set_siguiente(self.__disponible)
            
            self.__cantidad+=1
            return True
        
        else:
            print("Espacio lleno.")
            return False
        

    def recorrer(self):
        if self.__cantidad!=0:
            cabeza=self.__cab
            while cabeza!=-2:
                print(self.__espacio[cabeza].dar_contenido())
                cabeza=self.__espacio[cabeza].dar_siguiente()
            return True
        
        else:
            print("Lista vacia")
            return False