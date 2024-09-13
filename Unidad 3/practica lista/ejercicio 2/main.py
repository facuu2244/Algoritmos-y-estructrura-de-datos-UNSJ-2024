from clase_lista_encadenada_contenido import lista_encadenada_contenido

if __name__ == '__main__':
    lista=lista_encadenada_contenido()
    
    lista.insertar("a")
    lista.insertar("c")
    lista.insertar("b")
    print(lista.recuperar(3))
