import pandas as pd
import networkx as nx

df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep = ';')
g = nx.from_pandas_edgelist(df, source = 'origin', target = 'destination', edge_attr = 'harassmentRisk')

#ruta con menos acoso usando el algoritmo Dijkstra
print(nx.dijkstra_path(g,"(-75.5728593, 6.2115169)","(-75.5736973, 6.2109569)"))