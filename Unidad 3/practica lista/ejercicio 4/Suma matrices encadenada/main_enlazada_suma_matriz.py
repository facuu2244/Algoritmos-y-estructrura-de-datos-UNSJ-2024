import numpy as np
from clase_lista_encadenada_contenido import lista_encadenada_contenido
from clase_fila import fila

if __name__ == '__main__':
    lista_1=lista_encadenada_contenido()
    lista_2=lista_encadenada_contenido()

    #tamaño de la matriz
    rows = 5
    cols = 5
    densidad = 0.15  # Densidad de elementos distintos de cero (15%)

    # creo matriz_1
    matriz_1 = np.random.randint(1, 11, size=(rows, cols))
    # creo una máscara para hacer que algunos elementos sean cero, sera una matriz de True y False
    mascara = np.random.rand(rows, cols) > densidad
    # aplico la máscara a la matriz, donde en la máscara haya True en la posicion i,j pondra un 0 en matriz_1
    matriz_1[mascara] = 0
    
    #cargo la lista_1
    for i in range(rows):
        for j in range(cols):
            if matriz_1[i,j]!=0:
                una_fila=fila(i,j,matriz_1[i,j])
                lista_1.insertar(una_fila)
    
    #creo matriz_2
    matriz_2 = np.random.randint(1, 11, size=(rows, cols))
    mascara = np.random.rand(rows, cols) > densidad
    matriz_2[mascara] = 0
    #cargo lista_2
    for i in range(rows):
        for j in range(cols):
            if matriz_2[i,j]!=0:
                una_fila=fila(i,j,matriz_2[i,j])
                lista_2.insertar(una_fila)
        
        
    print("---------Matriz 1---------")    
    print(matriz_1)
    print("---------Matriz 2---------")   
    print(matriz_2)
    
    #Lista que reprecenta la matiz sumada
    suma_matrices=lista_encadenada_contenido()    
    #Creo 2 variables auxiliares que serviran para recorrer la lista
    aux_lista_1=lista_1.primer_elemento()
    aux_lista_2=lista_2.primer_elemento()
    
    while aux_lista_1!="El elemento ingresado es el ultimo" or aux_lista_2!="El elemento ingresado es el ultimo":
        #evaluo si una de las listas llego al final, u tranajo solo con la otra 
        if type(aux_lista_1)==str:
            fila_sumada=aux_lista_2
            suma_matrices.insertar(fila_sumada)
            aux_lista_2=lista_2.siguiente(aux_lista_2)
        elif type(aux_lista_2)==str:
            fila_sumada=aux_lista_1
            suma_matrices.insertar(fila_sumada)
            aux_lista_1=lista_1.siguiente(aux_lista_1)
        else:
            fila_sumada=aux_lista_1+aux_lista_2 #sumo las filas, en caso de tener diferente fila o columna, se retorna la menor
            suma_matrices.insertar(fila_sumada)
            
            if fila_sumada==aux_lista_1:#Si se retorno fila de la matriz_1 por ser menor
                aux_lista_1=lista_1.siguiente(aux_lista_1)#avanzo un componente solamente en esa lista
            elif fila_sumada==aux_lista_2:#Si se retorno fila de la matriz_2 por ser menor
                aux_lista_2=lista_2.siguiente(aux_lista_2)#avanzo un componente solamente en esa lista
            else:#Se realizo la suma por tener fila y columna iguales, avanzo en ambas listas
                aux_lista_1=lista_1.siguiente(aux_lista_1)
                aux_lista_2=lista_2.siguiente(aux_lista_2)
        
    print("\nLista que representa la suma de las matrices 1 y 2:")
    print("-----------------------")
    suma_matrices.recorrer()
    print("-----------------------")