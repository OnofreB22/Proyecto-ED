import pandas as pd
import networkx as nx
import gmplot

df = pd.read_csv('calles_de_medellin_con_acoso.csv')

#grafo
g = nx.DiGraph()

#iterar dataframe para agregar nodos y vertices
for index, row in df.iterrows():
    g.add_weighted_edges_from([(row['origin'],row['destination'],row['harassmentRisk'])])

#calcular ruta con menos acoso usando el algoritmo Dijkstra
ruta = nx.dijkstra_path(g,'-75.5778046, 6.2029412','-75.6101004, 6.2312125', weight = True)

#promedio de acoso de la ruta
valor = 0
for i in range(len(ruta)-1):
    peso = g[ruta[i]][ruta[i+1]]['weight']
    valor += peso

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