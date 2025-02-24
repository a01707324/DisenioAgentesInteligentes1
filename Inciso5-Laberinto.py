from simpleai.search import astar, SearchProblem

# Laberinto 1
laberinto = [
    "++++++++++++++++++++++",
    "+ O +   ++    +      +",
    "+   +   ++ + + + + + +",
    "+ + + ++ +    +      +",
    "+   + ++   +  + + +  +",
    "+    +      + ++   + +",
    "+++++ +++  +    + + ++",
    "+++++   ++ +    + + + ",
    "+        ++ + + +     +",
    "+++++ + + +    + + X +",
    "++++++++++++++++++++++"
]

# Laberinto 1
laberinto1 = [
    "++++++++++++++++++++++",
    "+ O  +  +++    ++    +",
    "+   ++   ++++  +++++ +",
    "+ + ++  +    ++   + + ",
    "+ + +  + +    +  + +  +",
    "+    +   +  + + +    +",
    "+++++   ++++    ++   +",
    "+++++ +  +  +  +     +",
    "+    + +   + + + +    +",
    "++++++    +   +    X +",
    "++++++++++++++++++++++"
]

# Laberinto 2
laberinto2 = [
    "++++++++++++++++++++++",
    "+ O     +    + +     +",
    "+ ++ +++  +++    +    +",
    "+  +     + + +  + + + +",
    "+    +    + +    +   +",
    "+   +  +     + +      +",
    "+++++  +   +  +++ + + +",
    "+++++   + ++  +  +  ++",
    "+  +   ++    +   + + +",
    "+++++ +     +    + X +",
    "++++++++++++++++++++++"
]

# Laberinto 3
laberinto3 = [
    "++++++++++++++++++++++",
    "+ O        +   +    +",
    "+  + ++++  ++ + +    +",
    "+  +    +   + +  +++ +",
    "+  + +++ +  +   +    +",
    "+     +  +  +    + + +",
    "++++++  + +    + +   +",
    "+   +  +   +   +  + ++",
    "+ +     + ++    +    +",
    "+++++  + +    +   X  +",
    "++++++++++++++++++++++"
]



# Encontrar posiciones
def encontrar_posicion(laberinto):
    inicio = None
    final = None
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            if laberinto[fila][columna] == "O":
                inicio = (fila, columna)
            elif laberinto[fila][columna] == "X":
                final = (fila, columna)
    return inicio, final

# Definir el problema
class Laberinto(SearchProblem):
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.inicio, self.meta = encontrar_posicion(laberinto)
        SearchProblem.__init__(self, self.inicio)

    def actions(self, state):
        fila, col = state
        acciones = []
        movimientos = [
            (-1, 0),  # Arriba
            (1, 0),   # Abajo
            (0, -1),  # Izquierda
            (0, 1)    # Derecha
        ]
        
        for mov_fila, mov_col in movimientos:
            nueva_fila, nueva_col = fila + mov_fila, col + mov_col
            
            # Verificar que la nueva posición esté dentro del laberinto
            if 0 <= nueva_fila < len(self.laberinto) and 0 <= nueva_col < len(self.laberinto[0]):
                # Evitar moverse a una pared "+"
                if self.laberinto[nueva_fila][nueva_col] != "+":
                    acciones.append((nueva_fila, nueva_col))
        
        return acciones


    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.meta  # Se cambió `self.final` a `self.meta`

    def cost(self, state1, action, state2):
        return 1
    
    def heuristic(self, state):
        fila, col = state
        fila_meta, col_meta = self.meta
        return abs(fila - fila_meta) + abs(col - col_meta) # Distancia 



def imprimir_laberinto_con_camino(laberinto, camino):
    # Convertir el laberinto a una lista de listas para modificarlo
    laberinto_modificable = [list(fila) for fila in laberinto]

    # Marcar la ruta en el laberinto con '.'
    for paso in camino:
        estado = paso[1]
        if estado is not None:
            fila, col = estado
            if laberinto_modificable[fila][col] not in ("O", "X"):
                laberinto_modificable[fila][col] = "-"

    # Convertir de vuelta a lista de strings para imprimir
    laberinto_actualizado = ["".join(fila) for fila in laberinto_modificable]

    # Imprimir el laberinto con el camino
    for fila in laberinto_actualizado:
        print(fila)
    print("\n")


# Resolver el problema
problema = Laberinto(laberinto)
resultado = astar(problema)

# Mostrar la solución e imprimir el laberinto en cada paso
for i, (_, estado) in enumerate(resultado.path()):
    print(f"Paso {i}: Moverse a {estado}")
    imprimir_laberinto_con_camino(laberinto, resultado.path()[:i+1])  # Imprimir hasta el paso actual
