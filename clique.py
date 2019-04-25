import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def is_clique(G,s):
    for v in s:
        L = list(s)
        L.remove(v)
        for w in L:
            if w not in list(neighbors(G,v)):
                return False
    return True


def maximum_clique_set(G):
    n = len(V(G))
    for k in range(n, 1, -1):
        for s in combinations(V(G),k):
            if is_clique(G,list(s)) == True:
                return list(s)

def clique_numbers(G):
    #convert directed graph to undirected because nx.find_cliques only accept undirected graphs
    if nx.is_directed(G):
        C = G.to_undirected()
    else
        C = G

    # get list of cliques
    cliques = nx.find_cliques(C)
    return len(cliques)