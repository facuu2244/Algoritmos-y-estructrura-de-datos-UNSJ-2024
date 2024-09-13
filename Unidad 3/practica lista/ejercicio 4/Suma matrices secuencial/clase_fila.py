class fila():
    __fila:int
    __columna:int
    __valor:int
    
    def __init__(self, f, c, v) -> None:
        self.__fila=f
        self.__columna=c
        self.__valor=v
    
    def __str__(self) -> str:
        return f"{self.__fila}, {self.__columna}, {self.__valor}"
    
    def __gt__(self, otro):
        if self.__fila<otro.__fila:
            return False
        else:
            return True
        
    def __add__(self, otro):
        #si alguna de las filas llego al final, el elemento sera 'El elemento ingresado es el ultimo'
        if self.__fila<otro.__fila or otro==None:
            return self
        elif self.__fila==otro.__fila:
            if self.__columna<otro.__columna:
                return self
            elif self.__columna==otro.__columna:
                return fila(self.__fila, self.__columna, self.__valor+otro.__valor)
            else:
                return otro
        else:
            return otro