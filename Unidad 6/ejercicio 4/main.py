from clase_digrafo import digrafo

if __name__ == '__main__':
    #            0         1       2       3       4         5
    vertices=["A-EII", "A-EIII", "EDI", "EDII", "EDIII", "Trad-Int"]
    aristas=[(0,1),(2,1),(2,3),(3,4),(4,5),(1,5)]#3er numero=peso entre vertices
    digrafo=digrafo(vertices, aristas)
    
    print("Materias en orden topologico: ")
    digrafo.REP_topologico()