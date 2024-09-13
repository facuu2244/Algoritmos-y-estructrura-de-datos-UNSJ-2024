class trabajo:
    __tiempo_requerido:int
    __minuto_ingresado:int
    __tiempo_espera:int
    
    def __init__(self, tiempo, minuto):
        self.__tiempo_requerido=tiempo
        self.__minuto_ingresado=minuto
        self.__tiempo_espera=0
        
    def set_espera(self, minuto_atendido):
        self.__tiempo_espera+=minuto_atendido-self.__minuto_ingresado#se suma la espera si es que fue reinsertado
        return self.__tiempo_espera

    def imprimir(self, tiempo_atencion_impresora):
        self.__tiempo_requerido=self.__tiempo_requerido-tiempo_atencion_impresora
        
    def dar_requerido(self):
        return self.__tiempo_requerido
    def actualizar_ingreso(self, reloj):
        self.__minuto_ingresado=reloj