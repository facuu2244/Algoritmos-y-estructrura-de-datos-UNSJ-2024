from clase_nodo import nodo
class colaEnl:
    __pr:nodo
    __ul:nodo
    __cant:int

    def __init__(self):
        self.__pr=None
        self.__ul=None
        self.__cant=0

    def insertar(self,elem):
        unnodo=nodo(elem)
        if self.__ul==None:
            self.__pr=unnodo
        else:
            self.__ul.set_siguiente(unnodo)
        self.__ul=unnodo
        self.__cant+=1

    def vacia(self):
        return self.__cant==0
    
    def suprimir(self):
        if self.vacia():
            return "La cola esta vacia"
        else:
            x=self.__pr.dar_contenido()
            self.__pr=self.__pr.dar_siguiente()
            self.__cant-=1
            if self.__pr==None:
                self.__ul=None
            return x
    
    def recorrer(self,aux):
        if aux!=None:
            print(aux.getdato())
            self.recorrer(aux.getsig())

    def getpr(self):
        return self.__pr


