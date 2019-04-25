import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def greedy_color(G):
    results = {}

    #init with none color
    for v in V(G):
        results[v]=None

    for v in V(G):

        neighbor_colors = []
        for n in neighbors(G,v):
            if results[n] != None:
                neighbor_colors.append(results[n])
        
        color = 0
        flag = False
        while not flag:
            if color not in neighbor_colors:
                flag = True
            else:
                color += 1

        results[v] = color
        
    return results

