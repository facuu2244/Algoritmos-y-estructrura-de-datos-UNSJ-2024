import numpy

class lista_secuencial:
    __lista:numpy.empty
    __ultimo:int
    
    def __init__(self):
        self.__lista=numpy.empty(5,dtype=object)
        self.__ultimo=0
        
    def llena(self):
        return self.__ultimo==5    
    def vacia(self):
        return self.__ultimo==0
    
    
    def insertar(self, posicion, elemento):
        if self.llena():
            print("La lista esta llena")
        else:
            if posicion>=0 and posicion<=self.__ultimo:
                for i in range(self.__ultimo, posicion, -1):
                    self.__lista[i]=self.__lista[i-1]
                    
                self.__lista[posicion]=elemento
                self.__ultimo+=1
            
            else: 
                if posicion==self.__ultimo+1:
                    self.__lista[posicion]=elemento
                    self.__ultimo+=1
                
                else:
                    print("Posicion invalida")
                    
    def suprimir(self, posicion):
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
            indice=-1
            band=False
            while indice<=self.__ultimo and band==False:
                if self.__lista[indice]==elemento:
                    band=True
                indice+=1
                
            return indice
        
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
    
    def siguiente(self, posicion):
        if self.vacia():
            return "La lista esta vacia"
        else:
            sig_p=None
            if 0<=posicion<self.__ultimo:
                sig_p=posicion+1
                return self.__lista[sig_p]

            else:
                return "Posicion invalida"

    def anterior(self, posicion):
        if self.vacia():
            return "La lista esta vacia"
        else:
            sig_p=None
            if 0<posicion<=self.__ultimo:
                sig_p=posicion-1
                return self.__lista[sig_p]

            else:
                return "Posicion invalida"
            
    def recorrer(self):
        for i in range(self.__ultimo):
            print(self.__lista[i])