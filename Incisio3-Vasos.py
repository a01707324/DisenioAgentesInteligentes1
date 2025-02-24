from simpleai.search import breadth_first, SearchProblem


"""Para el código se implemento: BUSQUEDA EN AMPLITUD :D"""
# Capacidades de las jarras
A_CAP, B_CAP, C_CAP = 8, 5, 3

# Estado inicial: A llena, B y C vacías
INITIAL_STATE = (8, 0, 0)

# Estado objetivo: A y B con 4 litros cada uno, C vacía
GOAL_STATE = (4, 4, 0)

# Definir el problema de búsqueda
class JarrasProblem(SearchProblem):
    def is_goal(self, state):
        """Verifica si hemos alcanzado el estado objetivo"""
        return state == GOAL_STATE

    def actions(self, state):
        """Genera las acciones posibles (transvases)"""
        a, b, c = state
        acciones = []
        
        # Lista de transvases posibles
        movimientos = [
            (a, b, B_CAP, "A", "B"),  # A -> B
            (a, c, C_CAP, "A", "C"),  # A -> C
            (b, a, A_CAP, "B", "A"),  # B -> A
            (b, c, C_CAP, "B", "C"),  # B -> C
            (c, a, A_CAP, "C", "A"),  # C -> A
            (c, b, B_CAP, "C", "B")   # C -> B
        ]
        
        for origen, destino, max_destino, jarra_origen, jarra_destino in movimientos:
            if origen > 0 and destino < max_destino:
                acciones.append((jarra_origen, jarra_destino))
        
        return acciones

    def result(self, state, action):
        """Genera el nuevo estado después de aplicar la acción"""
        a, b, c = state
        jarra_origen, jarra_destino = action
        
        nuevo_estado = list(state)
        
        # Identificar las jarras afectadas por la acción
        if jarra_origen == "A":
            origen, origen_idx = a, 0
        elif jarra_origen == "B":
            origen, origen_idx = b, 1
        else:
            origen, origen_idx = c, 2
        
        if jarra_destino == "A":
            destino, destino_idx, max_destino = a, 0, A_CAP
        elif jarra_destino == "B":
            destino, destino_idx, max_destino = b, 1, B_CAP
        else:
            destino, destino_idx, max_destino = c, 2, C_CAP
        
        # Transferir el agua
        cantidad_a_transferir = min(origen, max_destino - destino)
        nuevo_estado[origen_idx] -= cantidad_a_transferir
        nuevo_estado[destino_idx] += cantidad_a_transferir
        
        return tuple(nuevo_estado)

    def cost(self, state1, action, state2):
        """Costo uniforme: cada transvase tiene costo 1"""
        return 1

# Resolver el problema con BFS
problema = JarrasProblem(INITIAL_STATE)
resultado = breadth_first(problema)

# Imprimir los pasos de la solución
if resultado is None:
    print("No se encontró solución.")
else:
    for i, (accion, estado) in enumerate(resultado.path()):
        if accion is not None:
            print(f"Paso {i}: Transferir de {accion[0]} a {accion[1]} - Estado: {estado}")
from simpleai.search import breadth_first, SearchProblem

# Capacidades de las jarras
A_CAP, B_CAP, C_CAP = 8, 5, 3

# Estado inicial: A llena, B y C vacías
INITIAL_STATE = (8, 0, 0)
# Estado objetivo: A y B con 4 litros cada uno, C vacía
GOAL_STATE = (4, 4, 0)

# Definir el problema de búsqueda
class JarrasProblem(SearchProblem):
    def is_goal(self, state):
        """Verifica si hemos alcanzado el estado objetivo"""
        return state == GOAL_STATE

    def actions(self, state):
        """Genera las acciones posibles (transvases)"""
        a, b, c = state
        acciones = []
        
        # Lista de transvases posibles
        movimientos = [
            (a, b, B_CAP, "A", "B"),  # A -> B
            (a, c, C_CAP, "A", "C"),  # A -> C
            (b, a, A_CAP, "B", "A"),  # B -> A
            (b, c, C_CAP, "B", "C"),  # B -> C
            (c, a, A_CAP, "C", "A"),  # C -> A
            (c, b, B_CAP, "C", "B")   # C -> B
        ]
        
        for origen, destino, max_destino, jarra_origen, jarra_destino in movimientos:
            if origen > 0 and destino < max_destino:
                acciones.append((jarra_origen, jarra_destino))
        
        return acciones

    def result(self, state, action):
        """Genera el nuevo estado después de aplicar la acción"""
        a, b, c = state
        jarra_origen, jarra_destino = action
        
        nuevo_estado = list(state)
        
        # Identificar las jarras afectadas por la acción
        if jarra_origen == "A":
            origen, origen_idx = a, 0
        elif jarra_origen == "B":
            origen, origen_idx = b, 1
        else:
            origen, origen_idx = c, 2
        
        if jarra_destino == "A":
            destino, destino_idx, max_destino = a, 0, A_CAP
        elif jarra_destino == "B":
            destino, destino_idx, max_destino = b, 1, B_CAP
        else:
            destino, destino_idx, max_destino = c, 2, C_CAP
        
        # Transferir el agua
        cantidad_a_transferir = min(origen, max_destino - destino)
        nuevo_estado[origen_idx] -= cantidad_a_transferir
        nuevo_estado[destino_idx] += cantidad_a_transferir
        
        return tuple(nuevo_estado)

    def cost(self, state1, action, state2):
        """Costo uniforme: cada transvase tiene costo 1"""
        return 1

# Resolver el problema con BFS
problema = JarrasProblem(INITIAL_STATE)
resultado = breadth_first(problema)

# Imprimir los pasos de la solución
if resultado is None:
    print("No se encontró solución.")
else:
    for i, (accion, estado) in enumerate(resultado.path()):
        if accion is not None:
            print(f"Paso {i}: Transferir de {accion[0]} a {accion[1]} - Estado: {estado}")
