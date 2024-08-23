from clase_pila_secuencial import pila

if __name__ == "__main__":
        pila=pila()
        try:
            numero=int(input("Ingrese numero entero del intevalo [0, 50] para calcular su factorial: "))
            assert numero<=50 and numero>=0
            #Apilo los numeros
            numero_apilar=numero 
            for i in range(numero):
                pila.insertar(numero_apilar)
                numero_apilar-=1
            #Calculo el factorial multiplicando los numeros apilados
            factorial=1
            for i in range(numero):
                factorial=factorial*pila.suprimir()
            print(f"{numero}! = {factorial}")
            
        except ValueError:
            print("Tipo de dato incorrecto, se esperaba un entero positivo")
        except AssertionError:
            print("Numero invalido")