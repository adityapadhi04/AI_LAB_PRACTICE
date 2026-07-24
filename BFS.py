def bfs(graph,start_node):
    visited=[]
    queue=[start_node]

    while queue:
        current_node=queue.pop(0)

        if current_node not in visited:
            print(f"exploring node: {current_node}")
            visited.append(current_node)

            #.get() prevents errors if a node has no outgoing edges
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited
#user input section----
print("-----build your graph------")
student_graph = {}

#get the total no of connections
num_edges= int(input("how many edges(connections)does your graph have? "))

print("enter ecah edge separated by a space")
#read the input and split it into two variables
u,v=input(f"edge{i+1}:").split()

#initialize the lists if the nodes dont exist in the graph
if u not in student_graph:
    student_graph[u]=[]
if v not in student_graph:
    student_graph[v]=[]

    #add the connection (unidirected graph)
    student_graph[u].append(v)
    student_graph[v].append(u)
