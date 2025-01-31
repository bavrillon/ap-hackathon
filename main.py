import heapq
from Classes import *


reseau = Reseau()
TIME = 0 # en jours
BILAN = 0

while TIME <= 30 :
    camion_arrivee = reseau.file_events.obtenir_prochain_evenement()
    tps_arrivee, depart, destination, camion = camion_arrivee
    BILAN += Camion.parametres_trajet(destination, camion.usine)[1]      # On facture le trajet usine -> client_arrivée
    delta_t = TIME
    TIME = prochain_camion[0]
    delta_t = TIME - delta_t
    for usine in reseau.usines :            # On actualise le stock des usines
        usine.actualisation(delta_t)
    for client in reseau.clients :          # On actualise le stock des clients
        client.actualisation(delta_t)
    # On redirige le camion :
    prochain_client = 20000
    autonomie_min = 20000
    for client in usine.clients :      
        if client.autonomy() <= autonomie_min :
            prochain_client = client.ID
    tps_trajet = Camion.parametres_trajet(destination, camion.usine)[0] + Camion.parametres_trajet(prochain_client, camion.usine)[0]
    reseau.file_events.ajouter_evenement(tps_trajet, destination, prochain_client, camion.usine)
    BILAN += Camion.parametres_trajet(destination, camion.usine)[1]                          # On facture le trajet client_depart -> usine
