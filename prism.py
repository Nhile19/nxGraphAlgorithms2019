import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def is_spanning(G,H):
    return set(V(G)) == set(V(H))

# simple function to return the minimum edge based on the neighbors of all current vertices in the tree T
def get_min_edge(G,T):
    min_cost = 100000000
    min_edge = None
    for v in V(T):
        candidates = neighbors(G,v)
        for c in candidates:
            if G[v][c]['weight'] < min_cost and c not in V(T):
                min_cost = G[v][c]['weight']
                min_edge = (v,c)

    return min_edge


def prism(G):
    T = nx.Graph()
    #add the first vertice to the empty tree
    T.add_node(list(V(G))[0])
    while is_spanning(G,T) == False:
        #print(get_min_edge(G,T)[0])
        T.add_edge(*get_min_edge(G,T))
    
    return T

#Test
G = nx.read_weighted_edgelist('graph_library/prismtest.txt')
prism(G)