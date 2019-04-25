import networkx as nx
from itertools import combinations
from functions.local_properties import neighbors

#n(G) number of vertices
#m(G) number of matches
#diam(G) diameter of G
#rad(G) radius of G
#maximum_degree(G)
#minimum_degree(G)
#avg_degree(G)
#degree_sequence(G)

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def n(G):
    return len(V(G))

def m(G):
    return len(E(G))

def degree(G, v):
    return len(neighbors(G,v))

def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]
    D.sort(reverse = True)
    return D

def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def average_degree(G):
    return sum(degree_sequence(G))/n(G)


def distance_array(G,v):
    N=[[v]]
    Obs = [v]
    while set(Obs) != set(V(G)):
        temp_neighbors = []
        for x in N[-1]:
            for y in neighbors(G,x):
                if y not in Obs:
                    temp_neighbors.append(y)
                    Obs.append(y)    
        N.append(temp_neighbors)
    return N

def distance (G, v, w):
    D = distance_array(G,v)
    for i in range(len(D)):
        if w in D[i]:
            return i
        
def eccentricity(G, v):
    return len(distance_array(G, v)) - 1

def radius(G):
    return minimum_degree([eccentricity(G, v) for v in V(G)])

def diameter(G):
    return maximum_degree([eccentricity(G, v) for v in V(G)])

def graph_center(G):
    return [v for v in V(G)]
