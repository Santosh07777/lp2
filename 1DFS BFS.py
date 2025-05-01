graph = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(visited_node, graph, new_node):
    visited_node.append(new_node)
    queue = []
    queue.append(new_node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited_node:
                visited_node.append(neighbour)
                queue.append(neighbour)

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("DFS output:")
dfs([], graph, 'A')

print("BFS output:")
bfs([], graph, 'A')
