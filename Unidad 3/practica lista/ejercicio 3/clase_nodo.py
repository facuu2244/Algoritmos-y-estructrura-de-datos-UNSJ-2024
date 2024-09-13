class nodo:
    __contenido:int
    __siguiente:int
    
    def __init__(self):
        self.__siguiente=-2 #equivalente a None
    
    def set_contenido(self, elemento):
        self.__contenido=elemento
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
        
    def dar_contenido(self):
        return self.__contenido
    def dar_siguiente(self):
        return self.__siguiente