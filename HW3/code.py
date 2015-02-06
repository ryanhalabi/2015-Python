
from itertools import combinations
import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

pattern = re.compile(r'''
    [^^]        # Not the beginning of a string
    (?<!\.\s)   # Exclude the period
    (?<!\!\s)   # Exclude the exclamation point
    (?<!\?\s)   # Exclude the question
    [A-Z]       # A single capital letter
    [a-z]{1,}   # Rest of the word
    ''', flags=re.VERBOSE)


#warfile = open( 'warpeace.txt', 'r')
warfile = open( 'work2.txt', 'r')
war = warfile.read()
warfile.close()

a = pattern.findall(war)

for i in range(0,len(a)):
    a[i] = a[i].replace( '\n', ' ').replace( ' ', '').replace( '/', '').lstrip('"').lstrip("'").lstrip('(').lstrip('-')

b = list(set(a))



sentences = re.split('[.!?\n]', war)

for i in range(0,len(sentences)):
    sentences[i] = sentences[i].lstrip()

mat = np.zeros((len(b), len(b)))


for x in sentences:
    names = pattern.findall(x)
        
    print(x , '\n')
        
    for k in range(0, len(names)):
        names[k] = re.sub(r'[\W_]+', '', names[k])
    names = list(set(names))
    if len(names) > 2:
        namepairs = list(set(combinations(names, 2)))
                
        for y in namepairs:
            print(y[0])
            print('and')
            print(y[1])
                        
            xx  = b.index(y[0])
            yy  = b.index(y[1])
            mat[xx,yy] = mat[xx,yy] + 1
            mat[yy,xx] = mat[yy,xx] + 1

#
#D= nx.Graph()
#D.add_nodes_from(['hi','bye','great'])
#D.add_edge( 'hi','bye', weight = 10)
#D.add_edge( 'great','bye', weight = 10)
#D.add_edge( 'hi','great', weight = 10)


G = nx.Graph()
G.add_nodes_from(b)

for i in range(1,len(b)):
    print(i)
    for j in range(0,i-1):
        G.add_edge(  b[i], b[j]  , weight = mat[i][j])

plt.ion()
plt.clf()
nx.draw_networkx(G, node_size=50, alpha=0.15)
plt.show()