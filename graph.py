import itertools
def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]
    return total_distance
num_nodes = int(input("Enter the number of nodes: "))
graph = {}
for i in range(num_nodes):
    node_name = input(f"Enter the name of node {i+1}: ")
    num_outgoing_connections = int(input(f"Enter the number of outgoing connections from {node_name}: "))
    connections = {}
    for j in range(num_outgoing_connections):
        connected_node, weight = input(f"Enter connected node and weight (e.g., B 5): ").split()
        connections[connected_node] = int(weight)
    graph[node_name] = connections
start_node = input("Enter the starting node: ")
nodes = list(graph.keys())
nodes.remove(start_node)
permutations = itertools.permutations(nodes)
shortest_path = None
shortest_distance = float('inf')
remaining_paths = []
for perm in permutations:
    current_path = [start_node] + list(perm) + [start_node]
    total_distance = calculate_total_distance(current_path, graph)
    if total_distance < shortest_distance:
        shortest_path = current_path
        shortest_distance = total_distance
    remaining_paths.append((list(perm), total_distance))
print(f"Shortest Path: {' -> '.join(shortest_path)}")
print(f"Shortest Distance: {shortest_distance}")
for path, distance in remaining_paths:
    print(f"Remaining Path from {start_node} to {path[-1]}:{' -> '.join([start_node] + path + [start_node])}")
    print(f"Remaining Distance: {distance}")   
d={1:[2,3,4,5],2:[1,3,4,5],3:[1,2,4,5],4:[1,2,3,5],5:[1,2,3,4]}
va={1:[7,11,12,15],2:[7,20,10,12],3:[11,20,13,17],4:[12,10,13,5],5:[15,12,17,5]}