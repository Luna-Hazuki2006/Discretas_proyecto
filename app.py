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

def recorrido_busqueda_anchura(): 
    pass

def recorrido_busqueda_profundidad():
    pass

def algoritmo_kruskal(): 
    listaNumerica = []
    todo = max(sorted(list(Aristas.values())))
    for i in range(todo): 
        lista = list(filter(lambda x: Aristas[x] == i + 1, Aristas.keys()))
        listaNumerica.append(lista)
    print(listaNumerica)
    print('hola mundo')

def algoritmo_prim(): 
    pass

def main(): 
    recorrido_busqueda_anchura()
    recorrido_busqueda_profundidad()
    algoritmo_kruskal()
    algoritmo_prim()

if __name__ == '__main__': 
    main()