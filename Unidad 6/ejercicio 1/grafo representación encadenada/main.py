from clase_grafo import grafo_encadenada

if __name__ == '__main__':
    vertices=["0", "1", "2", "3", "4"]
    aristas=[(0,1), (0,3), (0,4), (1,2), (1,3), (2,3)]#los numeros representan indices de vertices en el arreglo
    
    grafo=grafo_encadenada(vertices, aristas)
    grafo.camino("2", "4")