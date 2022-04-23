import pandas as pd
import networkx as nx

df = pd.read_csv('calles_de_medellin_con_acoso.csv', sep = ';')
g = nx.from_pandas_edgelist(df, source = 'origin', target = 'destination', edge_attr = 'harassmentRisk')