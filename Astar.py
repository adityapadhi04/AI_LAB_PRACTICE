def get_user_inputs():
    # 1. Take input for Heuristic Values
    heuristic = {}
    num_nodes = int(input("Enter total number of nodes: "))
    print("\n Enter Heuristic Value h(n) for each node:")
    for _ in range(num_nodes):
        node = input("Node Name: ").strip().upper()
        h_val = float(input(f"Heuristic h({node}): "))
        heuristic[node] = h_val

    # 2. Take input for Graph Edges
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))
    print("\nEnter edges in format (from_node to_node weight):")
    for i in range(num_edges):
        u, v, w = input(f"Edge {i+1}: ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)

        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, weight))

    return graph, heuristic

def astar(graph, heuristic, start, goal):
    # open_list stores tuples of (node, accumulated_g_cost)
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select node with minimum f = g + h
        current = min(open_list, key=lambda x: g_cost[x[0]] + heuristic.get(x[0], 0))
        open_list.remove(current)
        current_node = current[0]

        # Goal check & path reconstruction
        if current_node == goal:
            path = [goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]

        # Neighbor exploration
        for neighbor, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node

                # Prevent adding duplicate node instances to open_list
                if not any(x[0] == neighbor for x in open_list):
                    open_list.append((neighbor, new_cost))

    return None, float('inf')

# --- Main Driver Program ---
if __name__ == "__main__":
    print("=== A* Algorithm Input Setup ===\n")
    graph, heuristic = get_user_inputs()

    print("\n--- Path Finding ---")
    start = input("Enter Start Node: ").strip().upper()
    goal = input("Enter Goal Node: ").strip().upper()

    path, cost = astar(graph, heuristic, start, goal)

    print("\n--- Result ---")
    if path:
        print("Shortest Path:", " -> ".join(path))
        print("Total Path Cost:", cost)
    else:
        print("Path not found.")