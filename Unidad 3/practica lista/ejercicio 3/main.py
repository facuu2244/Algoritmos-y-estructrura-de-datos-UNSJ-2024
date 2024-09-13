from clase_lista_cursor import lista_cursor

if __name__ == '__main__':
    lista=lista_cursor(10)
    
    lista.insertar_pos(1,0)
    lista.insertar_pos(2,1)
    lista.insertar_pos(3,2)
    
    lista.recorrer()