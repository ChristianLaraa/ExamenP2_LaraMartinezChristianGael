# Examen Practico - Lara Martinez Christian Gael

class Node:
    def __init__(self, value, left=None, right=None, color="red"):
        self.value = value
        self.left = left
        self.right = right
        self.color = color

    def __str__(self):
        return f"{self.value} ({self.color})"


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0


    visited = set()

   
    current = start

    while current not in visited:
        visited.add(current)

        # Actualizar distancias de los nodos adyacentes
        for neighbor, weight in graph[current].items():
            if distances[neighbor] > distances[current] + weight:
                distances[neighbor] = distances[current] + weight

       
        current = min(distances, key=distances.get)

    return distances



graph = {
    "A": {"B": 3, "C": 1},
    "B": {"D": 4},
    "C": {"E": 2, "F": 6},
    "D": {"G": 5},
    "E": {"F": 2},
}


distances = dijkstra(graph, "A")


for node, distance in distances.items():
    print(f"{node}: {distance}")