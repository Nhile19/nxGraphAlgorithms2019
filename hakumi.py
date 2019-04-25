import networkx as nx
from functions.global_properties import V, degree_sequence
from functions.local_properties import neighbors

#these 3 func go togeather ----------
def Howel_Hakimi_derivative(L):
    x=L[0]
    L.pop(0)
    for i in range(x):
        L[i]-=1
    L.sort(reverse=True)

def is_graphic(L):
    assert len(L)!=0, 'list cant be empty'
    while L[0]>0:
        Howel_Hakimi_derivative(L)
        if L[0]<0:
            print("not graphic")
        elif L[0]==0:
            print("is graphic")
            print("residual =",len(L))
      
def resid(G):
    L = degree_sequence(G)
    is_graphic(L)
#------------------------------------------
