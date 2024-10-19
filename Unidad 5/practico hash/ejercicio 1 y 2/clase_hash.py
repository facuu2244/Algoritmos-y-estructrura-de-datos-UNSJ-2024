import numpy as np

class tabla_hash:
    __arreglo:np.array
    __tamano:int
    
    
    def __init__(self, tamano):
        self.__tamano=tamano
        self.__arreglo=np.zeros(self.__tamano, dtype=object)
    
    
    def metodo_division(self, clave):
        return clave%self.__tamano
    

    def metodo_extraccion(self, clave):#Extraera los digitos centrales de la clave
        clave_cadena=str(clave)
        longitud=len(clave_cadena)
        #calculo el indice desde y hasta donde cortare la cadena
        inicio=(longitud//2)-2      
        fin=(longitud//2)+1
        #corto la cadena y la convierto en entero
        indice=int(clave_cadena[inicio:fin])
        return indice%self.__tamano
    
    
    def metodo_plegado(self, clave):#separara la clave en 2 digitos y la sumara
        indice=0
        clave_cadena=str(clave)
        #se toman los primeros 2 digitos
        inicio=0
        fin=2
        for i in range(len(clave_cadena)//2):#se repite la midad de veces de lo que mide la clave
            indice+=int(clave_cadena[inicio:fin])#sumo la cadena cortada
            inicio=fin
            fin+=2
            
        return indice%self.__tamano
    
    
    def metodo_cuadrado_medio(self, clave):
        clave=clave**2#elevo la clave al cuadrado
        #la convierto a cadena y extraigo los digitos del medio
        clave_cadena=str(clave)
        longitud=len(clave_cadena)
        inicio=(longitud//2)-2
        fin=(longitud//2)+1
        
        indice=int(clave_cadena[inicio:fin])

        return indice%self.__tamano
    
    
    #Claves alfanumericas
    def ascci_simple(self, clave):
        clave=str(clave)
        valores_ascii = [ord(caracter) for caracter in clave]#comprension de lista, almacena en la lista el valor ascci de cada caracter
        
        indice=0
        for valor in valores_ascii:
            indice+=valor#sumo los valores
        return indice%self.__tamano
    
    
    def ascci_con_posicion(self, clave):
        base=36#base del sistema de codificacion usado(26 letras + 10 numeros)
        clave=str(clave)
        valores_ascii = [ord(caracter) for caracter in clave.upper()]#comprension de lista, almacena en la lista el valor ascci de cada caracter
        indice=0
        for i in range(len(valores_ascii)):
            indice+=valores_ascii[i]*(base**i)#sumo los valores * base elevado la posicion del caracter en la cadena
            
        return indice%self.__tamano
        
    
    def insertar(self, clave):
        indice=self.ascci_simple(clave) 
        if self.__arreglo[indice]==0:#si esta disponible
            self.__arreglo[indice]=clave#se inserta
            
        else:
            #política manejo de colisiones direccionamiento abierto, secuencia de Prueba Lineal
            while self.__arreglo[indice]!=0:#mientras la posicion no este vacia
                indice=(indice+1)%self.__tamano#avanzo al siguiente elemento
                
            self.__arreglo[indice]=clave
                
    
    def buscar(self, clave):
        indice=self.ascci_simple(clave)
        
        if self.__arreglo[indice]==clave:
            print(f"Enecontrado: {clave}, una sola pregunta")
        else:
            preguntas=1
            while self.__arreglo[indice]!=clave and preguntas<=self.__tamano:#mientras la posicion no este vacia
                indice=(indice+1)%self.__tamano#avanzo al siguiente elemento
                preguntas+=1
                
            if preguntas>self.__tamano:
                print(f"No encontrado, {preguntas} preguntas realizadas")
            else:
                print(f"Enecontrado: {clave}, {preguntas} preguntas realizadas")
                                
    def recorrer(self):
        indice=0
        for i in self.__arreglo:
            print(f"indice: {indice}, valor= {i}")
            indice+=1