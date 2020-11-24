A program that calculates the degree, closeness and betweenness centralities of nodes of a graph:

Degree Centrality:

Degree centrality measures how connected a node is to other nodes in the graph.
Degree centrality calculation: counting the number of neighbours a node has.

Closeness Centrality:

Closeness centrality measures how close a node to other nodes in a graph.
Closeness centrality calculation: 
1/(sum of all shortest paths lengths from the node to all the other reachable nodes)

Betweenness Centrality:

Betweenness centrality measures how crucial a node is to shortest paths between pairs of nodes in the graph.
Betweenness centrality calculation:
(sum of all shortest paths lengths between every pair of nodes, that go through node i)/
(sum of all shortest paths lengths between every pair of nodes)
If the graph is not connected, then betweenness centrality is calculated per each component.




