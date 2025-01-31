import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import Point, Polygon
from classes import *

dfc = pd.read_csv("data/clients.csv")
dfp = pd.read_csv("data/plants.csv")

plt.scatter(dfc.coord_x, dfc.coord_y, s=1)
plt.scatter(dfp.coord_x, dfp.coord_y, s=10, marker="^", c='r')
plt.show()



#Création du diagramme de Voronoï
vor = Voronoi(dfp[['coord_x','coord_y']])

#Récupérer les polygones de Voronoï
polygones = []
for ind_regions in vor.regions: #pour chaque région (cellule), vor.regions renvoie la liste des indices des sommets
    if -1 not in ind_regions and len(ind_regions)>0: #pour éviter les régions infinis (sommets d'indice -1) et la première liste qui est vide
        p = []
        for i in ind_regions :
            p.append(vor.vertices[i]) #vor.vertices est la liste des coord des sommets
        polygones.append(Polygon(p)) #ajout d'un objet de type Polygon

#Rajoutons les 8 régions infinies manuellement (on part du coin gauche et on tourne sens horaire)
polygones.append(Polygon(((-5.96478111e+01,  4.83509302e+03), (-100,5000), (-400, 5000), (-5.02933323e+02,  4.34002199e+03))))
polygones.append(Polygon(((190,5000), (600,5000), (600, 4880), (5.06701804e+02,  4.91140884e+03), (2.52501704e+02,  4.87987120e+03))))
polygones.append(Polygon(((620,5000), (6.28103679e+02,  4.97466720e+03),(6.47034415e+02,  4.82843013e+03), (8.38530541e+02,  4.58856069e+03), (4550, 1000), (1000, 5000))))
polygones.append(Polygon(((1000,4550), (8.38530541e+02,  4.58856069e+03), (7.47256110e+02,  4.51509876e+03), (7.27998606e+02,  4.36689902e+03), (9.94573638e+02,  2.13669886e+03))))
polygones.append(Polygon(((9.94573638e+02,  2.13669886e+03),(6.33711876e+02,  4.36523849e+03),(5.18692719e+02,  4.38682316e+03), (520, 4280))))
polygones.append(Polygon(((-9.98837816e+03, -5.78835852e+06), (2.86524977e+02,  4.51234121e+03), (5.06866815e+02,  4.43754076e+03), (5.18692719e+02,  4.38682316e+03), (520, 4280))))
polygones.append(Polygon(((-20, 4290), (9.25157515e+01,  4.58029393e+03), (1.27552153e+02,  4.57363754e+03), (-9.98837816e+03, -5.78835852e+06))))
polygones.append(Polygon(((-5.02933323e+02,  4.34002199e+03), (4.73252103e+01,  4.61536577e+03), (9.25157515e+01,  4.58029393e+03), (-20, 4290))))

#Test d'appartenance des clients aux polygones
du = {poly : [] for poly in polygones}  #dictionnaire qui lie usines et polygones
for poly in du:
    for usine in reseau.usines:
        if poly.contains(Point(usine.coord_x, usine.coord_y)):
            du[poly]=usine        

d1 = {poly : [] for poly in polygones}
d2 = {usine : [] for usine in reseau.usines}    #dictionnaire à donner au groupe !
for k in range(dfc.shape[0]):   #on parcourt les clients
    client = Point(dfc.iloc[k, 0:2]) #on récupère les coord des clients, on en fait un objet de type Point
    for poly in polygones:
        if poly.contains(client): #si le client est dans la zone d'influence de l'usine
            d1[poly].append(client)
            for cli in reseau.clients:
                if cli.coord_x==client.x and cli.coord_y==client.y:
                    d2[du[poly]].append(cli)

            
#Affichage des zones
voronoi_plot_2d(vor, show_vertices=False, line_width = 0.5)
for poly in d1:
    x = [client.x for client in d1[poly]]
    y = [client.y for client in d1[poly]]
    plt.scatter(x, y, s=0.4)
#plt.xlim(-2000, 2000)
#plt.ylim(3000, 5500)
plt.show()

voronoi_plot_2d(vor, show_vertices=False, line_width = 0.5)
plt.scatter(dfc.coord_x, dfc.coord_y, s=0.2, color='r')
plt.show()

#Vérifions s'il manque des clients (il en manque 21 à cause de la récolte manuelle)
cpt=0
for cle in d1:
    cpt+=len(d1[cle])
print(cpt)

