import heapq
from Classes import *


TIME = 0 # en jours
BILAN = 0

while TIME <= 30 :
    camion_arrivee = reseau.file_events.obtenir_prochain_evenement()
    tps_arrivee, depart, destination, camion = camion_arrivee
    BILAN += Camion.parametres_trajet(destination, camion.usine)[1]      # On facture le dernier trajet
    delta_t = TIME
    TIME = prochain_camion[0]
    delta_t = TIME - delta_t
    for usine in reseau.usines :            # On actualise le stock des usines
        usine.actualisation(delta_t)
    for client in reseau.clients :          # On actualise le stock des clients
        client.actualisation(delta_t)
    
    # On traite et redirige le camion :
    position_actuelle = destination
    if position_actuelle.nature == usine :
        camion.recharge_camion(position_actuelle)
        prochain_client = camion.usine.clients[0]
        autonomie_min = 200000
        for client in camion.usine.clients :      
            if client.autonomy() <= autonomie_min :
                prochain_client = client
        prochain_arret = prochain_client
    elif position_actuelle.nature == client :
        camion.livraison_client(position_actuelle)
        prochain_arret = camion.usine
    tps_trajet = Camion.parametres_trajet(position_actuelle, prochain_arret)[0]
    reseau.file_events.ajouter_evenement(tps_trajet, position_actuelle, prochain_arret, camion.usine)
