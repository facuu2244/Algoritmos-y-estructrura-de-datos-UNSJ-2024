from typing import Any


class termino:
    __coeficiente:int
    __exponente:int
    
    def __init__(self, coeficiente, exponente) -> None:
        self.__coeficiente=coeficiente
        self.__exponente=exponente
        
    def __gt__(self, otro):
        if self.__exponente>otro.__exponente:
            return True
        else:
            return False
        
    def __add__(self, otro):
        if self.__exponente==otro.__exponente:
            return termino(self.__coeficiente+otro.__coeficiente, self.__exponente)
        else:
            if self.__exponente>otro.__exponente:
                return otro
            else:
                return self
            
    def __sub__(self, otro):
        if self.__exponente==otro.__exponente:
            return termino(self.__coeficiente-otro.__coeficiente, self.__exponente)
        else:
            if self.__exponente>otro.__exponente:
                return otro
            else:
                return self
            
    def __mul__(self, escalar):
        return termino(self.__coeficiente*escalar, self.__exponente)
            
    def __str__(self):
        return f"{self.__coeficiente}X^{self.__exponente}"