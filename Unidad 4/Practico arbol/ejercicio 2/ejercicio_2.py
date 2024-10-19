from clase_arbol import arbol

class arbol_2(arbol):
    #Inciso a)
    def mostrar_hermano_padre(self, elemento):
        if super().dar_raiz()!=None:
            aux_raiz=super().dar_raiz()
            padre=aux_raiz
            
            #busco el nodo
            while aux_raiz!=None and aux_raiz.dar_elemento()!=elemento:
                padre=aux_raiz
                if elemento<aux_raiz.dar_elemento():
                    aux_raiz=aux_raiz.dar_izq()
                else:
                    aux_raiz=aux_raiz.dar_der()
                    
            if aux_raiz==None:#salio por primera condicion
                return "Elemento no encontrado"
            else:#salio por segunda condicion
                if aux_raiz==super().dar_raiz():
                    print("El nodo ingresado es la raiz")
                    
                else:
                    print(f"Nodo: {aux_raiz.dar_elemento()}")
                    print(f"Nodo padre: {padre.dar_elemento()}")
                    hijo_izq=padre.dar_izq()
                    hijo_der=padre.dar_der()
                    
                    if hijo_der==None or hijo_izq==None:
                        print(f"El nodo no tiene hermano")
                    else:
                        if hijo_izq==aux_raiz:
                            print(f"Nodo hermano: {hijo_der.dar_elemento()}")
                        else:
                            print(f"Nodo hermano: {hijo_izq.dar_elemento()}")
        else:
            return "Arbol vacio"
        
    
    #inciso b)
    def contar_nodos(self, aux_raiz):
        if aux_raiz==None:
            return 0
        else:
            return  1+ self.contar_nodos(aux_raiz.dar_der()) + self.contar_nodos(aux_raiz.dar_izq())
        
        
    #incisos c) y d) usaran las funciones heredadas de arbol
    
    #c)
    #def artura()
    
    #d)
    def mostrar_sucesores(self, elemento):
        nodo=super().buscar(elemento)
        if nodo!=None:
            super().preorden(nodo)