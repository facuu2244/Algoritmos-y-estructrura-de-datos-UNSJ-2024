from clase_digrafo_ponderado import digrafo_p
#CAMBIAR CONDICIONES DE IF
if __name__ == '__main__':
    #          0    1    2    3    4    5
    vertices=["A", "B", "C", "D", "E", "F"]
    aristas=[(0,1,3), (0,3,6), (1,2,1), (1,4,2), (1,5,1), (2,3,2), (3,1,3), (4,3,3), (4,5,2), (5,0,5), (5,3,1)]#3er numero=peso entre vertices
    digrafo=digrafo_p(vertices, aristas)
    
    distancias_minimas=digrafo.algoritmo_floyd()
    
    v1=input("¿Quien envia el mensaje?: ")
    v2=input("¿Quien lo recibe?: ")
    v1=digrafo.buscar_indice(v1)
    v2=digrafo.buscar_indice(v2)
    distancia_minima_0_2 = int(distancias_minimas[v1][v2])
    print(f"El costo minimo de envio del mensaje es de: {distancia_minima_0_2}")