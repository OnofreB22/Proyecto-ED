import pandas as pd
import networkx as nx
import gmplot

df = pd.read_csv('calles_de_medellin_con_acoso.csv')

#eliminar calles con riesgo mayor a r
r = 0.9
df = df[df['harassmentRisk'] < r]

#ruta con menos acoso usando el algoritmo Dijkstra
g = nx.from_pandas_edgelist(df, source = 'origin', target = 'destination', edge_attr = 'harassmentRisk')
ruta = nx.dijkstra_path(g,'-75.5666527, 6.2091202','-75.5715105, 6.2063061', weight = True)

#listas de coordenadas
lat = []
lang = []

for coordenadas in ruta:
    com = coordenadas.find(',')
    lang.append(float(coordenadas[0:com]))
    lat.append(float(coordenadas[com+1:]))

#mostrar la ruta
gmap = gmplot.GoogleMapPlotter(lat[0],lang[0], 15)
gmap.marker(lat[0], lang[0], color='cornflowerblue')
gmap.marker(lat[-1], lang[-1], color='cornflowerblue')
gmap.plot(lat, lang, 'blue', edge_width=2.5)
gmap.draw('map.html')