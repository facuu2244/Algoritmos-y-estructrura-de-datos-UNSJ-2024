from clase_nodo import nodo

class lista_encadenada_contenido:
    __cabeza:nodo
    __cantidad:int
    
    def __init__(self):
        self.__cabeza=None
        self.__cantidad=0 # = indice+1
        
    def vacia(self):
        return self.__cantidad==0

    def buscar_posicion(self, elemento):
        pos=0
        aux=self.__cabeza
        while aux!=None and elemento>aux.dar_contenido() and pos<self.__cantidad:
            pos+=1
            aux=aux.dar_siguiente()
        return pos

    def insertar(self, elemento):
        un_nodo=nodo(elemento)
        posicion=self.buscar_posicion(elemento)
        
        if self.vacia() or posicion==0:#inserta por cabeza
            un_nodo.set_siguiente(self.__cabeza)
            self.__cabeza=un_nodo
            self.__cantidad+=1
            
        elif 0<posicion<=self.__cantidad:#inserta por el medio
            aux=self.__cabeza
            contador=0
            while aux.dar_siguiente()!=None and contador!=posicion-1:
                aux=aux.dar_siguiente()
                contador+=1

            un_nodo.set_siguiente(aux.dar_siguiente())
            aux.set_siguiente(un_nodo)
            self.__cantidad+=1
            
        elif posicion==self.__cantidad+1:#inserta al final
            aux=self.__cabeza
            while aux.dar_siguiente()!=None:
                aux=aux.dar_siguiente()

            aux.set_siguiente(un_nodo)
            un_nodo.set_siguiente(None)
            self.__cantidad+=1
            
        else:
            print("Posicion invalida")
            
    def suprimir(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        
        else:
            posicion=self.buscar(elemento)
            if posicion==0:
                self.__cabeza=self.__cabeza.dar_siguiente() 
                self.__cantidad-=1
            elif 0<posicion<=self.__cantidad:
                aux=self.__cabeza
                contador=0
                anterior=aux
                while aux.dar_siguiente()!=None and contador!=posicion:
                    anterior=aux
                    aux=aux.dar_siguiente()
                    contador+=1
                
                anterior.set_siguiente(aux.dar_siguiente())
                self.__cantidad-=1
                
            elif posicion==self.__cantidad+1:
                aux=self.__cabeza
                anterior=aux
                while aux.dar_siguiente()!=None:
                    anterior=aux
                    aux=aux.dar_siguiente()
                
                anterior.set_siguiente(None)
                self.__cantidad-=1
            
            else:
                return "Elemento no encontrado"
                     
    def recuperar(self, posicion):
        if self.vacia():
            return "La lista esta vacia"
        elif 0<=posicion<self.__cantidad:
            aux=self.__cabeza
            contador=0
            while aux!=None and contador!=posicion:
                aux=aux.dar_siguiente()
                contador+=1
                
            return aux.dar_contenido()
        else:
            return "Elemento no encontrado"
    
    def buscar(self, elemento):
        if self.vacia(): 
            return "La lista esta vacia"
        else:
            aux=self.__cabeza
            band=False
            contador=0
            posicion=-1
            
            while aux!=None and band!=True:
                if aux.dar_contenido()==elemento:
                    band=True
                    posicion=contador
                aux=aux.dar_siguiente()
                contador+=1
                
            return posicion #sera distinto de -1 si lo encontro 
                   
    def primer_elemento(self):
        if self.vacia():
            return "La lista esta vacia"
        else:  
            return self.__cabeza.dar_contenido()
        
    def ultimo_elemento(self):
        if self.vacia():
            return "La lista esta vacia"
        else:
            aux=self.__cabeza
            while aux.dar_siguiente()!=None:
                aux=aux.dar_siguiente()
            
            return aux.dar_contenido()
        
    def siguiente(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        else:
            posicion=self.buscar(elemento)
            if posicion == self.__cantidad-1:#La posicion es la ultima del arreglo
                return "El elemento ingresado es el ultimo"
            elif 0<=posicion<=self.__cantidad:
                aux=self.__cabeza
                contador=0
                while aux.dar_siguiente()!=None and contador!=posicion:
                    aux=aux.dar_siguiente()
                    contador+=1
                return aux.dar_siguiente().dar_contenido()
            else:
                return "Elemento no encontrado"
            
    def anterior(self, elemento):
        if self.vacia():
            return "La lista esta vacia"
        else:
            posicion=self.buscar(elemento)
            if posicion==0:
                return "El elemento ingresado es el primero"
            elif 0<=posicion<=self.__cantidad:
                aux=self.__cabeza
                contador=0
                anterior=aux
                while aux.dar_siguiente()!=None and contador!=posicion:
                    anterior=aux
                    aux=aux.dar_siguiente()
                    contador+=1
                return anterior.dar_contenido()
            else:
                return "Elemento no encontrado"

    def recorrer(self):
        if self.vacia():
            return "La lista esta vacia"
        else:
            aux=self.__cabeza
            print(aux.dar_contenido())
            
            while aux.dar_siguiente()!=None:
                aux=aux.dar_siguiente()
                print(aux.dar_contenido())