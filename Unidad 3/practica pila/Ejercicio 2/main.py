from clase_pila_secuencial import pila

if __name__ == '__main__':
    pila=pila()
    numero=int(input("Ingrese numero para representarlo en binario: "))
    while numero!=0:
        resto=int(numero%2)
        numero=numero//2
        pila.insertar(resto)
    
    while pila.vacia()==False:
        print(pila.suprimir())