class nodo:
    __contenido:int
    __siguiente:object
    
    def __init__(self, elemento):
        self.__contenido=elemento
        self.__siguiente=None
    
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
        
    def dar_contenido(self):
        return self.__contenido
    def dar_siguiente(self):
        return self.__siguiente