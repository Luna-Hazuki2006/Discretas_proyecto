from pprint import pprint

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
    final = list(filter(lambda x: actual in x, Aristas.keys()))
    

def recorrido_busqueda_profundidad():
    Nuevas_Aristas = []
    Nuevos_Vertices = []

def algoritmo_kruskal(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    listaNumerica = []
    todo = max(sorted(list(Aristas.values())))
    for i in range(1, todo): 
        lista = list(filter(lambda x: Aristas[x] == i, Aristas.keys()))
        listaNumerica.append(lista)
    for esto in listaNumerica: 
        for este in esto: 
            primero = este[0]
            segundo = este[2]
            if (primero not in Nuevos_Vertices and 
                segundo not in Nuevos_Vertices): 
                Nuevos_Vertices.append(primero)
                Nuevos_Vertices.append(segundo)
                Nuevas_Aristas.append(este)
            elif (primero not in Nuevos_Vertices and 
                  segundo in Nuevos_Vertices): 
                Nuevos_Vertices.append(primero)
                Nuevas_Aristas.append(este)
            elif (primero in Nuevos_Vertices and 
                  segundo not in Nuevos_Vertices): 
                Nuevos_Vertices.append(segundo)
                Nuevas_Aristas.append(este)
            else: 
                Nuevas_Aristas.append(este)
            # print(Nuevas_Aristas)
        if len(Nuevas_Aristas) is (len(Vertices) - 1): break

    resultado = sum((Aristas[x]) for x in Nuevas_Aristas)
    
    print("*********************************")
    print('Algoritmo de Kruskal')
    print('Aristas: ')
    print(Nuevas_Aristas)
    print(f"La ponderación mínima es de: {resultado}")
    print('*********************************')

def algoritmo_prim(): 
    Nuevas_Aristas = []
    Nuevos_Vertices = []
    Aristas_Restantes = list(Aristas.keys())

    print("*********************************")
    print('Algoritmo de Prim')
    print('Aristas: ')
    print(Nuevas_Aristas)
    print('Aristas restantes: ')
    print(Aristas_Restantes)
    print('Vertices: ')
    print(Nuevos_Vertices)
    print(f"La ponderación mínima es de: 0")
    print('*********************************')

def main(): 
    # recorrido_busqueda_anchura()
    # recorrido_busqueda_profundidad()
    algoritmo_kruskal()
    algoritmo_prim()

if __name__ == '__main__': 
    main()