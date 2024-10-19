from clase_lista_encadenada_contenido import lista_encadenada_contenido
from clase_nodo_arbol import nodo
from clase_arbol import arbol

if __name__ == '__main__':
    lista= lista_encadenada_contenido()
    
    #Frase de pueba: "el asesino es el secretario"
    #inserto en la lista nodos tipo nodo_arbol que contienen caracter y numero de veces que aparece en la frase
    lista.insertar(nodo("e", 6))
    lista.insertar(nodo("l", 2))
    lista.insertar(nodo("a", 2))
    lista.insertar(nodo("s", 3))
    lista.insertar(nodo("i", 2))
    lista.insertar(nodo("n", 1))
    lista.insertar(nodo("o", 2))
    lista.insertar(nodo("r", 2))
    lista.insertar(nodo("t", 1))
    
    #voy a ir suprimiendo los primeros 2 elementos de la lista 
    aux_lista=lista.suprimir(lista.dar_cabeza().dar_contenido())#dar_contenido() develve un objeto nodo_arbol
    siguiente=lista.suprimir(aux_lista.dar_siguiente().dar_contenido())
    #los cuales sumo e inserto el nodo sumado de nuevo en la lista
    nodo_sumado=None
    
    while aux_lista.dar_siguiente()!=None:
        #sumo los nodos e inserto de nuevo
        nodo_sumado=aux_lista.dar_contenido()+siguiente.dar_contenido()
        lista.insertar(nodo_sumado)
        
        #avanzo en la lista suprimiendo los siguientes 2 nodos
        aux_lista=lista.suprimir(lista.dar_cabeza().dar_contenido())
        if aux_lista.dar_siguiente()!=None:
            siguiente=lista.suprimir(aux_lista.dar_siguiente().dar_contenido())
            

    arbol=arbol()
    arbol.insertar_raiz(nodo_sumado)
    arbol.mostar(arbol.dar_raiz())