import numpy

class lista_secuencial_por_contenido:
    __lista:numpy.empty
    __ultimo:int
    
    def __init__(self):
        self.__lista=numpy.empty(5,dtype=object)
        self.__ultimo=0
        
    def llena(self):
        return self.__ultimo==5    
    def vacia(self):
        return self.__ultimo==0
    
    def obtener_posicion(self, elemento):
        pos=0
        while pos < self.__ultimo and self.__lista[pos] < elemento:
            pos += 1
        return pos
    
    def insertar(self, elemento):
        if self.llena():
            print("La lista esta llena")
        else:
            pos=self.obtener_posicion(elemento)
            if pos>=0 and pos<=self.__ultimo:
                for i in range(self.__ultimo, pos, -1):
                    self.__lista[i]=self.__lista[i-1]
                    
                self.__lista[pos]=elemento
                self.__ultimo+=1
                
            else:
                self.__lista[pos]=elemento
                self.__ultimo+=1
                                       
    def suprimir(self, elemento):
        posicion=self.obtener_posicion(elemento)
        
        if self.vacia():
            print("La lista esta vacia")
            
        elif posicion<=self.__ultimo:
            valor=self.__lista[posicion]
            for i in range(posicion, self.__ultimo):
                self.__lista[i]=self.__lista[i+1]
            self.__ultimo-=1
            return valor
        
        else:
            print("Posicion invalida")
            return None
    
    def recuperar(self, posicion):
        if self.vacia():
            return "La lista esta vacia"
            
        else:
            if 0<=posicion<=self.__ultimo:
                return self.__lista[posicion]
            else:
                return "Posicion invalida"
    
    def buscar(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        else:
            indice=0
            band=False
            indice_devolver=-1
            while indice<=self.__ultimo and band==False:
                if self.__lista[indice]==elemento:
                    indice_devolver=indice
                    band=True
                indice+=1
                
            return indice_devolver
        
    def primer_elemento(self):
        if self.vacia():
            return "La lista esta vacia"
        else:
            return self.__lista[0]
        
    def ultimo_elemento(self):
        if self.vacia():
            return "La lista esta vacia"
        else:
            return self.__lista[self.__ultimo-1]    
    
    def siguiente(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        else:
            pos=self.buscar(elemento)
            if pos==self.__ultimo:
                return "No hay siguiente"
            else:
                return self.__lista[pos+1]
            
    def anterior(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        else:
            pos=self.buscar(elemento)
            if pos==0:
                return "No hay anterior"
            else:
                return self.__lista[pos-1]
            
    def recorrer(self):
        for i in self.__lista:
            print(i)