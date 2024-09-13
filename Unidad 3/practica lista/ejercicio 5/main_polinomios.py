from clase_lista_encadenada_contenido import lista_encadenada_contenido
from clase_termino import termino

if __name__ == '__main__':
    polinomio_1=lista_encadenada_contenido()
    polinomio_2=lista_encadenada_contenido()
    
    polinomio_1.insertar(termino(4, 3))
    polinomio_1.insertar(termino(2, 2))
    polinomio_1.insertar(termino(3, 1))
    
    print("------Polinomio 1------")
    polinomio_1.recorrer()
    
    polinomio_2.insertar(termino(4, 3))
    polinomio_2.insertar(termino(5, 1))
    print("------Polinomio 2------")
    polinomio_2.recorrer()

    resultado=lista_encadenada_contenido()
    
    termino_polinomio_1=polinomio_1.primer_elemento()
    termino_polinomio_2=polinomio_2.primer_elemento()
    
    while termino_polinomio_1!=None or termino_polinomio_2!=None:
        if termino_polinomio_1==None:
            termino_sumado=termino_polinomio_2
            resultado.insertar(termino_sumado)
            termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
            
        elif termino_polinomio_2==None:
            termino_sumado=termino_polinomio_1
            resultado.insertar(termino_sumado)
            termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
            
        else:
            termino_sumado=termino_polinomio_1+termino_polinomio_2
            resultado.insertar(termino_sumado)
            
            if termino_sumado==termino_polinomio_1:
                termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
            elif termino_sumado==termino_polinomio_2:
                termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
            else:
                termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
                termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
                
    print("------Suma de los Polinomios------")           
    resultado.recorrer()
    
    
    resultado=lista_encadenada_contenido()
    termino_polinomio_1=polinomio_1.primer_elemento()
    termino_polinomio_2=polinomio_2.primer_elemento()
    while termino_polinomio_1!=None or termino_polinomio_2!=None:
        if termino_polinomio_1==None:
            termino_sumado=termino_polinomio_2
            resultado.insertar(termino_sumado)
            termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
            
        elif termino_polinomio_2==None:
            termino_sumado=termino_polinomio_1
            resultado.insertar(termino_sumado)
            termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
            
        else:
            termino_sumado=termino_polinomio_1-termino_polinomio_2
            resultado.insertar(termino_sumado)
            
            if termino_sumado==termino_polinomio_1:
                termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
            elif termino_sumado==termino_polinomio_2:
                termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
            else:
                termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
                termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
                
    print("------Resta de los Polinomios------")           
    resultado.recorrer()
    
    
    escalar=float(input("Escalar para multiplicar los polinomios: "))
    
    resultado=lista_encadenada_contenido()
    termino_polinomio_1=polinomio_1.primer_elemento()
    
    while termino_polinomio_1!=None:
        resultado.insertar(termino_polinomio_1*escalar)
        termino_polinomio_1=polinomio_1.siguiente(termino_polinomio_1)
    
    print(f"------Polinomio 1 x {escalar}------")
    resultado.recorrer()
    
    resultado=lista_encadenada_contenido()
    termino_polinomio_2=polinomio_2.primer_elemento()
    while termino_polinomio_2!=None:
        resultado.insertar(termino_polinomio_2*escalar)
        termino_polinomio_2=polinomio_2.siguiente(termino_polinomio_2)
    
    print(f"------Polinomio 2 x {escalar}------")
    resultado.recorrer()