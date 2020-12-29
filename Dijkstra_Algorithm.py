""" Prim's Algorithm"""

graph = {
            'a': [('b',4),('h',8)],
            'b': [('h',11),('c',8)],
            'c': [('i',2),('f',4),('d',7)],
            'd': [('e',6),('f',14)],
            'e': [('f',10)],
            'f': [('g',2)],
            'g': [('i',6),('h',1)],
            'h': [('i',7)],
            'i': [('g',6)]
        }

len_graph = len(graph)

# Initialising 3 empty Arrays of fixed length
visited = [0]*len_graph
cost = [-1]*len_graph
parent = [0]*len_graph


# Vertices --> List of all keys in graph
vertices = list(graph.keys())
print("Nodes of Graph :", vertices, "\n")


# initially zeroth index element of key of graph
vertex = vertices[0]


# Interating through len(graph) --> 0,1,2,3,4,5 (here)
for k in range(len(graph)):
    visited[vertices.index(vertex)] = 1
    '''
    finding index of vertex(min) from vertices(key of graphs) and 
    putting it as visited array's index value, 
    to mark the visited element (vertex) as marked (1)
    syntax --> list.index(value)
    '''

    print("=====================================================\n")
    # Iterating through the tuples (ie.adjacents with their weights)
    print("Current vertex : ", vertex)
    print("All neighbors : ", graph[vertex])
    ind_currNode = vertices.index(vertex)
    print("ind_currNode : ",ind_currNode)
    for i in graph[vertex]:
        print("Current neighbor (node,weight) : ", i)
        # Finding index of current adjacent node in vertices
        ind_cur = vertices.index(i[0])
        print("Current's index in Graph : ", ind_cur, "\n")

        # conditions (if cost it -1 update it to its edge's weight)
        # & update its parent accordingly
        if cost[ind_cur] == -1:
            cost[ind_cur] = i[1]
            parent[ind_cur] = vertex

        # If marked unvisited check the edge's weight and if less than the ...
        # present one is found , update it in cost & change its parent
        elif visited[ind_cur] != 1:
            if i[1] + cost[ind_currNode] < cost[ind_cur]:
                cost[ind_cur] = i[1] + cost[ind_currNode]
                parent[ind_cur] = vertex


    minim = -1
    for ind in range(len(cost)):
        # Finding min element -- (if unvisited, cost is not -1,min is -1 & new found is lesser)
        if cost[ind] != -1 and visited[ind] != 1:
            if minim == -1 or minim > cost[ind]:
                minim = cost[ind]
                min_index = ind

    vertex = vertices[min_index]

    print(f"Minimum {minim}, Index_min = {min_index}")
    print("VISITED = ",visited)
    print("COST = ",cost)
    print("PARENT = ",parent)
    print("\n\n")

parent[0] = 0
cost[0] = 0

print("----------- Final Arrays -----------------------------")
print( "VISITED = ", visited )
print( "COST = ", cost )
print( "PARENT = ", parent )


count = 0
for i in cost:
    count += i
print("\nMST of Given Graph : ",count)
print("-----------------------------------------------------")

# Graph
import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()

# Adding nodes to Graph
g.add_node('a',pos=(-10,0))
g.add_node('b',pos=(0,5))
g.add_node('c',pos=(10,5))
g.add_node('d',pos=(20,5))
g.add_node('e',pos=(30,0))
g.add_node('f',pos=(20,-5))
g.add_node('g',pos=(10,-5))
g.add_node('h',pos=(0,-5))
g.add_node('i',pos=(5,0))


# Joining the vertices through edge
g.add_edge('a', 'b',weight= 4)
g.add_edge('b', 'c',weight= 12)
g.add_edge('c', 'd',weight=19)
g.add_edge('d', 'e',weight=21)
g.add_edge('g', 'h',weight=11)
g.add_edge('c','i',weight=9)
g.add_edge('c','f',weight=8)
g.add_edge('f','g',weight=14)

# Assigning nodes & edges
pos = nx.get_node_attributes(g,'pos')
labels = nx.get_edge_attributes(g,'weight')

# Drawing graph
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
nx.draw(g, pos,with_labels=True)
nx.draw_networkx(g,pos, with_labels=True,node_color = 'yellow')

# Printing & displaying MST
print("\nGraph Traversal from each node :-\n")
print(nx.shortest_path(g,source='a'))
plt.show()

print("\nCode Executed Successfully!\n")