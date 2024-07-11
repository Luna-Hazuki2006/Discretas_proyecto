from pprint import pprint
from collections import defaultdict
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
    'H-I': 1, 'H-M': 1, 
    'I-J': 10, 'I-M': 1, 
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
    print()
    data.append(actual)
    while len(Vertices) != len(Nuevas_Aristas): 
        prueba = []
        for esto in data: 
            cercanos = list(filter(lambda x: esto in x , Aristas.keys()))
            for este in cercanos: 
                # print(este)
                # prueba.append(este)
                primero = este[0]
                segundo = este[1]
                if primero not in Nuevos_Vertices: 
                    Nuevos_Vertices.append(primero)
                    prueba.append(primero)
                if segundo not in Nuevos_Vertices: 
                    Nuevos_Vertices.append(segundo)
                    prueba.append(segundo)
                Nuevas_Aristas.append(este)
            print(cercanos)
        data = prueba
    
    resultado = sum((Aristas[x]) for x in Nuevas_Aristas)

    print("*********************************")
    print('Recorrido de busqueda anchura')
    print('Vertices: ')
    print(Nuevos_Vertices)
    print('Aristas: ')
    print(Nuevas_Aristas)
    print(f"La ponderación es de: {resultado}")
    print('*********************************')
    return Nuevas_Aristas

def recorrido_busqueda_profundidad():
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    data = []
    actual = Vertices[0]
    print()
    data.append(actual)
    while len(Vertices) != len(Nuevas_Aristas): 
        prueba = []
        for esto in data: 
            cercanos = list(filter(lambda x: esto in x , Aristas.keys()))
            for este in cercanos: 
                # print(este)
                # prueba.append(este)
                primero = este[0]
                segundo = este[1]
                if primero not in Nuevos_Vertices: 
                    Nuevos_Vertices.append(primero)
                    prueba.append(primero)
                if segundo not in Nuevos_Vertices: 
                    Nuevos_Vertices.append(segundo)
                    prueba.append(segundo)
                Nuevas_Aristas.append(este)
            print(cercanos)
        data = prueba
    
    resultado = sum((Aristas[x]) for x in Nuevas_Aristas)

    print("*********************************")
    print('Recorrido de busqueda anchura')
    print('Vertices: ')
    print(Nuevos_Vertices)
    print('Aristas: ')
    print(Nuevas_Aristas)
    print(f"La ponderación es de: {resultado}")
    print('*********************************')
    return Nuevas_Aristas

def algoritmo_kruskal(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    listaNumerica = []
    todo = max(sorted(list(Aristas.values())))
    for i in range(1, todo + 1): 
        lista = list(filter(lambda x: Aristas[x] == i, Aristas.keys()))
        listaNumerica.append(lista)
    print(listaNumerica)
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
            # elif len(Nuevos_Vertices) == len(Vertices): 
                # Nuevas_Aristas.append(este)
            elif len(Nuevos_Vertices) != len(Vertices): 
                lista1 = list(filter(lambda x: primero in x, Nuevas_Aristas))
                lista2 = list(filter(lambda x: segundo in x, Nuevas_Aristas))
                if probar_Ciclo(lista1, lista2, primero, segundo): 
                    Nuevas_Aristas.append(este)
                print(lista1)
                print(lista2)
                # lista1, lista2 = probar_Ciclo(primero, segundo)
                # print(lista1)
                # lista1 = list(filter(lambda x: x[0] in Nuevas_Aristas, lista1))
                # lista1 = list(map(lambda x: x[0], lista1))
                # print(lista1)
                # print(lista2)
                # lista2 = list(filter(lambda x: x[0] in Nuevas_Aristas, lista2))
                # lista2 = list(map(lambda x: x[0], lista2))
                # print(lista2)
                # if len(lista1) == len(lista2): 
                #     # print('iguales')
                #     # for e in lista1: 
                #     #     if not lista2.__contains__(e): 
                #     #         Nuevas_Aristas.append(este)
                #     #         break

                # else: 
                #     print('desiguales')
                #     Nuevas_Aristas.append(este)
            if len(Nuevas_Aristas) == (len(Vertices)): break
        if len(Nuevas_Aristas) == (len(Vertices)): break

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
    maximo = len(Vertices) 
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

def probar_Ciclo(primero, segundo, v1, v2):
    primero = list(map(lambda x: x[0] if x[0] != v1 else x[2], primero))
    segundo = list(map(lambda x: x[0] if x[0] != v2 else x[2], segundo))
    print(primero)
    print(segundo)
    for e in primero: 
        for i in segundo: 
            if e == i: return False
    return True
    # primera_lista = []
    # segunda_lista = [] 
    # lista = obtener_listas(primero, primera_lista)
    # for i in lista: 
    #     esto = obtener_listas(i, primera_lista)
    #     primera_lista.append(esto)
    # lista = obtener_listas(segundo, segunda_lista)
    # for i in lista: 
    #     esto = obtener_listas(i, segunda_lista)
    #     segunda_lista.append(esto)
    # return primera_lista, segunda_lista

# def obtener_listas(busqueda, prueba): 
#     print(f'busqueda de {busqueda}')
#     lista = list(filter(lambda x: busqueda in x and busqueda not in prueba, Aristas))
#     return lista

def main(): 

    print('Bienvenido a la calculadora de grafos :D')
    print('elige una de las siguientes opciones: ')
    print('a. Conseguir busqueda de anchura')
    print('b. Conseguir busqueda de profundidad')
    print('c. Conseguir árbol de expansión mínimo con Kruskal')
    print('d. Conseguir árbol de expansión mínimo con Prim')
    decision = input('e. Salir sin nada\n')
    if decision == 'a': lista = recorrido_busqueda_anchura()
    elif decision == 'b': lista = recorrido_busqueda_profundidad()
    elif decision == 'c': lista = algoritmo_kruskal()
    elif decision == 'd': lista = algoritmo_prim()
    elif decision == 'e': print('Chao, que le vaya bien :D')
    else: print('Esa no era una opción >:v')
    print("Cierra la ventana para continuar...")
    GRAFO = grafo_Oficial.Graph()
    lista = list(map(lambda x: (x[0], x[2], Aristas[x]), lista))
    print('litas')
    print(lista)
    GRAFO.add_nodes_from(Vertices)
    GRAFO.add_weighted_edges_from(lista)

    pos=grafo_Oficial.spring_layout(GRAFO, seed=4)
    grafo_Oficial.draw_networkx(GRAFO, pos)
    labels = grafo_Oficial.get_edge_attributes(GRAFO, 'weight')
    grafo_Oficial.draw_networkx_edge_labels(GRAFO, pos, edge_labels=labels)
    graficador.show()

if __name__ == '__main__': 
    main()