from ejercicio_2 import arbol_2

if __name__ == '__main__':
    arbol=arbol_2()
    
    arbol.insertar(8)
    arbol.insertar(3)
    arbol.insertar(10)
    arbol.insertar(1)
    arbol.insertar(6)
    arbol.insertar(14)
    arbol.insertar(4)
    arbol.insertar(7)
    arbol.insertar(13)
    
    arbol.mostrar_sucesores(5)