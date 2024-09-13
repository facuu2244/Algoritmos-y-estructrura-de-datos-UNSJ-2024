from clase_pila_encadenada import pila

if __name__ == '__main__':
    print("-------------Torres de Hanoi-------------")
    try:
        discos=int(input("Con cuantos discos desea jugar: "))
        jugadas_minimas=(2**discos)-1

        #Diccionario de pilas
        pilas={"1":pila(), #pila 1 (izquierda)
               "2":pila(), #pila 2 (centro)
               "3":pila()  #pila 3 (derecha)
               }
        #Cargo la pila 1 con los discos
        for i in range(discos):
            pilas["1"].insertar(discos)
            discos-=1
        
        #Empieza el juego
        gano=False
        jugadas=0
        pila_origen=0
        pila_destino=0
        while gano==False:
            if pilas["1"].vacia() and pilas["2"].vacia(): #Todos los discos entan en la pila 3
                gano=True
                print("\n¡¡Has ganado!!\n")
                print(f"Numero de jugadas: {jugadas}")
                print(f"Jugadas minimas posibles segun el numero de discos elegido: {jugadas_minimas}")
          #Sigue el juego
            else:
                print("-------------Estado del juego-------------")
                print("---Pila 1 (izquierda)---")
                pilas["1"].recorrer()
                print("---Pila 2 (centro)---")
                pilas["2"].recorrer()
                print("---Pila 3 (derecha)---")
                pilas["3"].recorrer()
          
                try:
                    #Pide desde y hasta donde mover el disco
                    pila_origen=int(input("\nPila de donde se quiere sacar el disco: "))
                    pila_destino=int(input("Pila a donde se quiere mover el disco: "))
                    assert pila_origen<=3 and pila_origen>0
                    assert pila_destino<=3 and pila_destino>0
                    
                    
                    if pilas[str(pila_origen)].vacia():#La pila de origen seleccionada esta vacia
                        print("\nLa pila de donde quiere sacar el disco esta vacia")
                        
                    #Pila destino vacia o movimiento valido, se ejecuta la jugada
                    elif pilas[str(pila_destino)].vacia() or pilas[str(pila_origen)].ultimo() < pilas[str(pila_destino)].ultimo():
                        disco_mover=pilas[str(pila_origen)].suprimir()
                        pilas[str(pila_destino)].insertar(disco_mover)
                        jugadas+=1
                    
                    else:#Movimiento invalido
                        print("\nNo se puede colocar un disco arriba de uno mas pequeño")
              
                except AssertionError:
                    print("Numero de pila invalido")
    except ValueError:
        print("Se esperaba un valor entero")