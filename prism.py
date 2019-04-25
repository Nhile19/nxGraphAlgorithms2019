import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def is_spanning(G,H):
    return set(V(G)) == set(V(H))

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
#def incident_edges(G, T):


G = nx.read_weighted_edgelist('graph_library/prismtest.txt')

T = nx.Graph()
T.add_node('d')

while is_spanning(G,T) == False:
    print(*get_min_edge(G,T))
    T.add_edge(*get_min_edge(G,T))
    
nx.draw(T)

