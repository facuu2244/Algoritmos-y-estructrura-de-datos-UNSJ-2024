from clase_grafo import grafo_secuencial

if __name__ == '__main__':
    vertices=["0", "1", "2", "3", "4"]
    aristas=[(0,1), (0,3), (0,4), (1,2)]#los numeros reprecentan indices de vertices en el arreglo
    
    grafo=grafo_secuencial(vertices, aristas)

    grafo.camino("1","4")