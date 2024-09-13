class cliente:
    __tiempo_requerido:int
    __minuto_ingreso:int
    __espera:int
    
    def __init__(self, tiempo_requerido, reloj) -> None:
        self.__tiempo_requerido=tiempo_requerido
        self.__minuto_ingreso=reloj
        self.__espera=0
        
    def set_espera(self, reloj):
        self.__espera=reloj-self.__minuto_ingreso
        return self.__espera
    def dar_requerido(self):
        return self.__tiempo_requerido