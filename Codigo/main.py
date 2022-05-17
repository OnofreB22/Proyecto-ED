import pandas as pd
import networkx as nx
import gmplot

df = pd.read_csv('calles_de_medellin_con_acoso.csv')

#grafo
g = nx.DiGraph()

for index, row in df.iterrows():
    if row['oneway'] == 'True':
        g.add_weighted_edges_from([(row['origin'],row['destination'],row['length']), (row['destiny'],row['origin'])])
    else:
        g.add_weighted_edges_from([(row['origin'],row['destination'],row['length'])])

#ruta con menos acoso usando el algoritmo Dijkstra
ruta = nx.dijkstra_path(g,'-75.5778046, 6.2029412','-75.6101004, 6.2312125', weight = True)

#distancia mas corta o riesgo de acoso
valor = 0

for geo in range (len(ruta)-1):
    condition = df[(df['origin'] == ruta[geo]) & (df['destination'] == ruta[geo+1])].index.values.astype(int)
    valor = valor + df.iloc[int(condition)]['harassmentRisk']

print(valor/len(ruta))

#listas de coordenadas
lat = []
lang = []

for coordenadas in ruta:
    com = coordenadas.find(',')
    lang.append(float(coordenadas[0:com]))
    lat.append(float(coordenadas[com+1:]))

#mostrar la ruta
gmap = gmplot.GoogleMapPlotter(lat[0],lang[0], 15)
gmap.marker(lat[0], lang[0], color='green')
gmap.marker(lat[-1], lang[-1], color='red')
gmap.plot(lat, lang, 'blue', edge_width=4)
gmap.draw('map.html')