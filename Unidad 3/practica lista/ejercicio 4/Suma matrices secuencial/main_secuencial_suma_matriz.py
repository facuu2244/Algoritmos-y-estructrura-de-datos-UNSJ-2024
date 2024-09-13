import numpy
from clase_lista_secuencial_por_contenido import lista_secuencial_por_contenido
from clase_fila import fila

if __name__ == '__main__':
    matriz_1=lista_secuencial_por_contenido()
    matriz_2=lista_secuencial_por_contenido()
    
    #Cargo Matriz_1
    matriz_1.insertar(fila(0, 1, 5))
    matriz_1.insertar(fila(2, 0, 6))
    matriz_1.insertar(fila(2, 4, 2))
    matriz_1.insertar(fila(3, 3, 9))
    matriz_1.insertar(fila(4, 4, 10))
    
    #Cargo Matriz_2
    matriz_2.insertar(fila(0, 1, 1))
    matriz_2.insertar(fila(1, 4, 6))
    matriz_2.insertar(fila(3, 1, 7))
    matriz_2.insertar(fila(3, 4, 10))
    
    #Suma
    suma_matrices=lista_secuencial_por_contenido()
    
    aux_matriz_1=matriz_1.primer_elemento() 
    aux_matriz_2=matriz_2.primer_elemento() 
    
    # while  aux_matriz_1!=None or aux_matriz_2!=None:
    #     if aux_matriz_1==None:
    #         fila_sumada=aux_matriz_2
    #         suma_matrices.insertar(fila_sumada)
    #         aux_matriz_2=matriz_2.recuperar(matriz_2.obtener_posicion(aux_matriz_2))
            
    #     elif aux_matriz_2==None:
    #         fila_sumada=aux_matriz_1
    #         suma_matrices.insertar(fila_sumada)
    #         aux_matriz_1=matriz_1.recuperar(matriz_1.obtener_posicion(aux_matriz_1))
    #     else:
    #         fila_sumada=aux_matriz_1+aux_matriz_2 #sumo las filas, en caso de tener diferente fila o columna, se retorna la menor
    #         suma_matrices.insertar(fila_sumada)
            
    #         if fila_sumada==aux_matriz_1:#Si se retorno fila de la matriz_1 por ser menor
    #             aux_matriz_1=matriz_1.recuperar(matriz_1.obtener_posicion(aux_matriz_1))#avanzo un componente solamente en esa lista
    #         elif fila_sumada==aux_matriz_2:#Si se retorno fila de la matriz_2 por ser menor
    #             aux_matriz_2=matriz_2.recuperar(matriz_2.obtener_posicion(aux_matriz_2))#avanzo un componente solamente en esa lista
    #         else:#Se realizo la suma por tener fila y columna iguales, avanzo en ambas listas
    #             aux_matriz_1=matriz_1.recuperar(matriz_1.obtener_posicion(aux_matriz_1))
    #             aux_matriz_2=matriz_2.recuperar(matriz_2.obtener_posicion(aux_matriz_2))
                
    # suma_matrices.recorrer()