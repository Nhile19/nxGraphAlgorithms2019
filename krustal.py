import networkx as nx
from networkx.utils import UnionFind
from functions.global_properties import V,E

#Simple function to get the minimum edge from the set of edges
def get_min_edge(G,edges):
    min_cost = 100000000
    min_edge = None
    for e in edges:
        cost = G[e[0]][e[1]]['weight']
        if cost < min_cost:
            min_cost = cost
            min_edge = e

    return min_edge


        
def krustal(G):
    T = nx.Graph()
    subtrees = UnionFind()
    
    # make list of all edges in G
    edge_pool = list(E(G))
    
    #loop until no more edges left to consider adding
    while len(edge_pool) > 0:
        #get the shortest edge in the edge list, I don't know how to sort yet
        edge = get_min_edge(G,edge_pool)
        #remove the edge from the pool for the next iteration
        edge_pool.remove(edge)
        
        #check if the edge will form a cycle, if not then add it to the tree
        if subtrees[edge[0]] != subtrees[edge[1]]:
            subtrees.union(edge[0], edge[1])
            T.add_edge(*edge)
    return T
    
#Test
G = nx.read_weighted_edgelist('graph_library/prismtest.txt')
nx.draw(krustal(G))