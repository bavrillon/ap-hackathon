import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



dico_cout = {}
for camion in Ls_camion :
    dico_cout[camion] = {[]}


def trajet(camion, usine, client):

    vitesse = 50
    cout_kilometrique = 0.10
    distance = np.sqrt((client.coord_x - usine.coord_x)**2 + (client.coord_y - usine.coord_y)**2)
    temps = distance / vitesse
    cout_trajet = cout_kilometrique * distance
    dico_cout[camion] += [cout_trajet]


def livraison_client_déchargement(camion, client):
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
    stockage_restant_client = client.capacity - client.bouteille_tot
    if stockage_restant_client < 0 :
        print("Problème, trop de bouteilles stockées par rapport à la capacité de stockage")
    elif stockage_restant_client > 80 :
        client.bouteilles_pleines += 80
        camion.bouteilles_pleines -= 80
    else :
        client.bouteilles_pleines += stockage_restant
        camion.bouteille_pleines -= stockage_restant
    
def livraison_client_chargement(camion, client): 
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
    stockage_restant_camion = camion.capacity - camion.bouteille_tot
    if stockage_restant_camion< 0 :
        print("Problème, trop de bouteilles stockées par rapport à la capacité de stockage")
    elif stockage_restant_camion > client.bouteilles_vides :
        camion.bouteilles_vides += client.bouteilles_vides
        client.bouteilles_vides = 0
    else :
        camion.bouteilles_vides += stockage_restant_camion
        client.bouteilles_vides -= stockage_restant_camion
    


# Attention se dictionnaire est pour l'instant journalier, il faudrait refaire usine.refill au bout de 24h
dico_prod = {}
for usine in reseau.usines :
    dico_prod[usine] = [usine.refill]


def chargement_usine(camion, usine):
    if dico_prod[usine][-1] <= 0 :
        print("L'usine atteint sa production maximale journalière !")
    elif dico_prod[usine][-1] > 80 :
        camion.bouteille += 80
        dico_prod[usine][-1] -= 80
    else :
        camion.bouteille += dico_prod[usine][-1]
        dico_prod[usine][-1] = 0


Client
self.bouteilles_pleines = 0
self.bouteilles_vides = init


methode autonomie
self.autonomie = client.bouteilles_pleines
methode bouteille tot
self.bouteille

Usine
self.bouteilles_pleines = init
self.bouteilles_vides = 0

Client
self.bouteilles_pleines = 0
self.bouteilles_vides = 0