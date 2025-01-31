import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from classes import *




dico_cout = {}
for camion in Ls_camion :
    dico_cout[camion] = {[]}


def livraison_client(camion, client):
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
    echange1 = min(client.bouteilles_vides, camion.bouteilles_pleines)
    camion.bouteilles_pleines -= echange1
    camion.bouteilles_vides += echange1
    client.bouteilles_pleines += echange1
    client.bouteilles_vides -= echange1
    COST += echange1 * 100
    if camion.bouteilles_pleines == 0 :
        echange_2a = min(camion.capacity-camion.bouteilles_tot(), client.bouteilles_vides)
        camion.bouteilles_vides += echange_2a
        client.bouteilles_vides -= echange_2a
    else:
        echange_2b = min(client.capacity-client.bouteilles_tot(), camion.bouteilles_pleines)
        client.bouteilles_pleines += echange_2b
        camion.bouteilles_pleines -= echange_2b
        COST += echange2 * 100
    assert(camion.bouteilles_tot <= camion.capacity)
    assert(usine.bouteilles_tot <= usine.capacity)
    assert(client.bouteilles_tot <= client.capacity)




def recharge_camion(camion, client):
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
    echange1 = min(camion.bouteilles_vides, usine.bouteilles_pleines)
    usine.bouteilles_pleines -= echange1
    usine.bouteilles_vides += echange1
    camion.bouteilles_pleines += echange1
    camion.bouteilles_vides -= echange1
    COST -= echange1 * 40
    if usine.bouteilles_pleines == 0 :
        echange_2a = min(usine.capacity-usine.bouteilles_tot(), camion.bouteilles_vides)
        usine.bouteilles_vides += echange_2a
        camion.bouteilles_vides -= echange_2a
    else:
        echange_2b = min(camion.capacity-camion.bouteilles_tot(), usine.bouteilles_pleines)
        camion.bouteilles_pleines += echange_2b
        usine.bouteilles_pleines -= echange_2b
        COST -= echange1 * 40
        assert(camion.bouteilles_tot <= camion.capacity)
    assert(usine.bouteilles_tot <= usine.capacity)
    assert(client.bouteilles_tot <= client.capacity)





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
