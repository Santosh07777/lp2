
import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    def prim(self, start):
        shortest_distances = {node: float('inf') for node in self.graph}
        shortest_distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > shortest_distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_distances

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_node = 'A'
shortest_paths = graph.prim(start_node)

print("Shortest paths from", start_node, ":", shortest_paths)
