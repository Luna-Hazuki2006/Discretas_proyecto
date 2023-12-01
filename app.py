from pprint import pprint
import matplotlib.pyplot as graficador
import networkx as grafo_Oficial

Vertices = [
    'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'P'
]

Aristas = {
    'A-B': 8, 'A-E': 4, 'A-D': 5, 
    'B-E': 12, 'B-F': 4, 'B-C': 3, 
    'C-F': 9, 'C-G': 11, 
    'D-E': 9, 'D-H': 6, 
    'E-F': 3, 'E-J': 5, 'E-I': 8, 
    'F-G': 1, 'F-K': 8, 
    'G-L': 7, 'G-K': 8, 
    'H-I': 2, 'H-M': 7, 
    'I-J': 10, 'I-M': 6, 
    'J-K': 6, 'J-N': 9, 
    'K-L': 5, 'K-P': 7, 
    'L-P': 6, 
    'M-N': 2, 
    'N-P': 12
}

Nuevas_Aristas = []
Nuevos_Vertices = []

def recorrido_busqueda_anchura(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    data = []
    actual = Vertices[0]
    while len(Vertices) - 1 == len(Nuevas_Aristas): 
        cercanos = list(filter(lambda x: x.__contains__(actual), Aristas.keys()))
        for esto in cercanos: 
            print(esto)
    resultado = 0
    print("*********************************")
    print('Recorrido de busqueda anchura')
    print('Aristas: ')
    print(Nuevas_Aristas)
    print(f"La ponderación mínima es de: {resultado}")
    print('*********************************')
    return Nuevas_Aristas

def recorrido_busqueda_profundidad():
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    return Nuevas_Aristas

def algoritmo_kruskal(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    listaNumerica = []
    todo = max(sorted(list(Aristas.values())))
    for i in range(1, todo + 1): 
        lista = list(filter(lambda x: Aristas[x] == i, Aristas.keys()))
        listaNumerica.append(lista)
    for esto in listaNumerica: 
        for este in esto: 
            primero = este[0]
            segundo = este[2]
            if (not Nuevos_Vertices.__contains__(primero) and 
                not Nuevos_Vertices.__contains__(segundo)): 
                Nuevos_Vertices.append(primero)
                Nuevos_Vertices.append(segundo)
                Nuevas_Aristas.append(este)
            elif (not Nuevos_Vertices.__contains__(primero) and 
                  Nuevos_Vertices.__contains__(segundo)): 
                Nuevos_Vertices.append(primero)
                Nuevas_Aristas.append(este)
            elif (Nuevos_Vertices.__contains__(primero) and 
                  not Nuevos_Vertices.__contains__(segundo)): 
                Nuevos_Vertices.append(segundo)
                Nuevas_Aristas.append(este)
            else: 
                Nuevas_Aristas.append(este)
            if len(Nuevas_Aristas) is (len(Vertices) - 1): break
        if len(Nuevas_Aristas) is (len(Vertices) - 1): break

    resultado = sum((Aristas[x]) for x in Nuevas_Aristas)
    # print(listaNumerica)
    print("*********************************")
    print('Algoritmo de Kruskal')
    print('Aristas: ')
    print(Nuevas_Aristas)
    print(f"La ponderación mínima es de: {resultado}")
    print('*********************************')
    return Nuevas_Aristas

def algoritmo_prim(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    Aristas_Restantes = []
    maximo = len(Vertices) - 1
    actual = Vertices[0]
    todo = max(sorted(list(Aristas.values())))
    for i in range(1, todo + 1): 
        lista = list(filter(lambda x: Aristas[x] == i, Aristas.keys()))
        for esto in lista: Aristas_Restantes.append(esto)
    # print(Aristas_Restantes)

    while (len(Nuevas_Aristas) < maximo) and (len(Nuevos_Vertices) != len(Vertices)): 
        print(actual)
        if not Nuevos_Vertices.__contains__(actual): 
            Nuevos_Vertices.append(actual)
        lista = []
        for esto in Nuevos_Vertices: 
            prueba = list(filter(lambda x: (esto in x), 
                                            Aristas_Restantes))
            print(prueba)
            for este in prueba: lista.append(este)
        
        lista = list(set(lista))
       
        lista = sorted(lista, key=lambda x: Aristas[x])
        # print(lista)
        menor = lista[0]
        # if actual == 'C' or actual == 'B': 
        Nuevas_Aristas.append(menor)
        Aristas_Restantes = list(filter(lambda x: x != menor, Aristas_Restantes))
        primero = menor[0]
        segundo = menor[2]
        verdad = [primero, segundo]
        for este in verdad: Nuevos_Vertices.append(este)
        Nuevos_Vertices = list(set(Nuevos_Vertices))
        if primero != menor: 
            actual = segundo
        elif segundo != menor: 
            actual = primero

    
    # retorno = Nuevas_Aristas.pop()
    # Nuevas_Aristas.append(Aristas_Restantes[0])
    # Aristas_Restantes.remove(Aristas_Restantes[0])
    # Aristas_Restantes.append(retorno)

    # for esto in Vertices: 
    #     Nuevos_Vertices.append(esto)
    #     lista = list(filter(lambda x: esto in x, Aristas.keys()))
    #     lista = sorted(lista, key=lambda x: Aristas[x])
    #     menor = lista[0]
    #     if Aristas_Restantes.__contains__(menor): 
    #         Nuevas_Aristas.append(menor)
    #         Aristas_Restantes.remove(menor)
        # if not Nuevos_Vertices.__contains__(esto): 
        #     Nuevos_Vertices.append(esto)
        # lista = list(filter(lambda x: esto in x, Aristas))
        # lista = sorted(lista, key=lambda x: Aristas[x])
        # menor = lista[0]
        # if (not Nuevos_Vertices.__contains__(menor) and 
        #     not Nuevas_Aristas.__contains__(esto)): 
        #     Nuevas_Aristas.append(menor)
            # Aristas_Restantes.remove(menor)
            # lista = list(filter(lambda x: (Aristas[x] == Aristas[menor]), lista))
            # if len(lista) == 1: 
            #     Nuevas_Aristas.append(menor)
            #     Aristas_Restantes.remove(menor)
            # elif len(list(filter(lambda x: Nuevas_Aristas.__contains__(x), lista))) == 0: 
            #     Nuevas_Aristas.append(menor)
            #     Aristas_Restantes.remove(menor)
    
    resultado = sum((Aristas[x]) for x in Nuevas_Aristas)

    print("*********************************")
    print('Algoritmo de Prim')
    print('Aristas restantes: ')
    print(Aristas_Restantes)
    print('Aristas: ')
    print(Nuevas_Aristas)
    print('Vertices: ')
    print(Nuevos_Vertices)
    print(f"La ponderación mínima es de: {resultado}")
    print('*********************************')
    return Nuevas_Aristas

def main(): 
    lista = recorrido_busqueda_anchura()
    # recorrido_busqueda_profundidad()
    lista = algoritmo_kruskal()
    # algoritmo_prim()
    print("Cierra la ventana para continuar...")
    GRAFO = grafo_Oficial.Graph()
    print(Nuevas_Aristas)
    lista = list(map(lambda x: (x[0], x[2], Aristas[x]), lista))
    print('litas')
    print(lista)
    GRAFO.add_weighted_edges_from(lista)

    pos=grafo_Oficial.spring_layout(GRAFO, seed=4)
    grafo_Oficial.draw_networkx(GRAFO,pos)
    labels = grafo_Oficial.get_edge_attributes(GRAFO,'weight')
    grafo_Oficial.draw_networkx_edge_labels(GRAFO,pos,edge_labels=labels)
    # graficador.show()

if __name__ == '__main__': 
    main()