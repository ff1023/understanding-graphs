import networkx as nx
import matplotlib.pyplot as plt

''' --------------------------------- degree centrality ---------------------------------- '''
'''
Degree centrality measures how connected a node is to other nodes in the graph.
Degree centrality calculation: counting the number of neighbours a node has.

In the below function, we go over all the nodes in the graph, and calculate degree centrality per each node.
'''


def degree_centrality(G):
    # creating a dictionary that will hold each node's degree
    degrees_dict = {node: 0 for node in G.nodes}

    # counting the number of edges that are attached to each node in the graph
    for edge in G.edges:
        degrees_dict[edge[0]] += 1
        degrees_dict[edge[1]] += 1

    return degrees_dict


''' -------------------------------- closeness centrality -------------------------------- '''
'''
Closeness centrality measures how close a node to other nodes in a graph.
Closeness centrality calculation: 
1/(sum of all shortest paths lengths from the node to all the other reachable nodes) 

In the below function, we go over all the nodes in the graph, and calculate closeness centrality per each node.   
'''


def closeness_centrality(G):
    # creating a dictionary that will hold each node's closeness degree
    closeness_dict = {node: 0 for node in G.nodes}

    for node in G.nodes:
        # finding the lengths of the shortests paths from 'node' to every other node in the graph
        short_path_lengths = nx.single_source_shortest_path_length(G, node)
        # summing the lengths
        for length in short_path_lengths.values():
            closeness_dict[node] += length
        # connecting the results to the closeness centrality formula: 1/sum_distances
        if closeness_dict[node] != 0:
            closeness_dict[node] = 1 / closeness_dict[node]

    return closeness_dict


''' ------------------------------- betweenness centrality ------------------------------- '''
'''
Betweenness centrality measures how crucial a node is to shortest paths between pairs of nodes in the graph.
Betweenness centrality calculation:
(sum of all shortest paths lengths between every pair of nodes, that go through node i)/
(sum of all shortest paths lengths between every pair of nodes)
If the graph is not connected, then betweenness centrality is calculated per each component.

In the below functions we first check if the graph is connected("betweenness_centrality" function).
According to this function's output, we proceed with "betweenness_centrality_connected" function.
This function goes over all the nodes in the graph (or component, if the original graph was 
unconnected and we sent a component), and calculates their betweenness centrality.  
'''


def betweenness_centrality_connected(G):
    # creating a dictionary that will hold each node's betweenness degree
    betweenness_dict = {node: 0 for node in G.nodes}

    for node in G.nodes:
        # for every pair of nodes in the graph that are not 'node'
        for i in range(len(G.nodes)):
            node1 = list(G.nodes)[i]
            if node1 != node:
                for j in range(i, len(G.nodes)):
                    node2 = list(G.nodes)[j]
                    if node2 != node:
                        through_node = 0
                        general = 0
                        # computing all the shortest paths between the pair
                        short_paths = nx.all_shortest_paths(G, node1, node2)
                        # calculating the number of paths that go through 'node'
                        for short_path in short_paths:
                            if node in short_path:
                                through_node += 1
                            general += 1
                        # adding the result of this pair to the current node's betweenness value
                        betweenness_dict[node] += through_node / general
    return betweenness_dict


def betweenness_centrality(G):
    if nx.is_connected(G):
        return betweenness_centrality_connected(G)
    else:
        # creating the final dictionary that will hold all the nodes in G and their betweenness centrality values
        # the dictionary per each component will be merged into this dictionary
        betweenness_dict = {}
        # finding G's components
        con_comp = nx.connected_components(G)
        # creating graphs out of G's components
        graphs = (G.subgraph(cc) for cc in con_comp)
        # calculating betweenness centrality per each node in each component, per it's component
        for graph in graphs:
            betweenness_dict.update(betweenness_centrality_connected(graph))
        return betweenness_dict


''' ------------------------------------ top 5 nodes ------------------------------------- '''
'''
The below function sorts an input dictionary (by value, descending order) and returns its top 5 key-value elements
'''


def top_five_nodes(dict):
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    top_five = sorted_dict[:5]
    return top_five


# creating a random gnp graph of size 15 with edge probability 0.5
myGnpGraph = nx.gnp_random_graph(15, 0.5, seed=None, directed=False)

# printing the top 5 nodes of the random graph, according to their degree centrality values
degree_dict = degree_centrality(myGnpGraph)
top_five = top_five_nodes(degree_dict)
print("Top five nodes ordered by degree centrality in descending order - (node, degree): ", top_five)

# printing the top 5 nodes of the random graph, according to their closeness centrality values
closeness_dict = closeness_centrality(myGnpGraph)
top_five = top_five_nodes(closeness_dict)
print("Top five nodes ordered by closeness centrality in descending order - (node, closeness): ", top_five)

# printing the top 5 nodes of the random graph, according to their betweenness centrality values
betweenness_dict = betweenness_centrality(myGnpGraph)
top_five = top_five_nodes(betweenness_dict)
print("Top five nodes ordered by betweenness centrality in descending order - (node, betweenness): ", top_five)


''' ----------------------------------- visualization ------------------------------------ '''

# plotting the random graph, with nodes of size proportional to their degree centrality value
plt.figure(1)
nx.draw(myGnpGraph, with_labels=True, font_size=10, node_size=[v * 100 for v in degree_dict.values()])
plt.show()

# plotting the random graph, with nodes of size proportional to their closeness centrality value
plt.figure(2)
nx.draw(myGnpGraph, with_labels=True, font_size=10, node_size=[v * 10000 for v in closeness_dict.values()])
plt.show()

# plotting the random graph, with nodes of size proportional to their betweenness centrality value
plt.figure(3)
nx.draw(myGnpGraph, with_labels=True, font_size=10, node_size=[v * 100 for v in betweenness_dict.values()])
plt.show()