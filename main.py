import heapq
from Classes import *


reseau = Reseau()
TIME = 0 # en jours
COST = 0

while TIME <= 30 :
    reseau.file_events.obtenir_prochain_evenement()

class FilePrioriteEvenements:
    def __init__(self):
        self.file = []
    
    def ajouter_evenement(self, tps_trajet, destination):
        tps_arrivee = TIME + tps_trajet  
        heapq.heappush(self.file, (tps_arrivee, destination))

    def obtenir_prochain_evenement(self):
        prochain_evenement = heapq.heappop(self.file)
        COUT += ## Cout du trajet qui vient d'être effectué
        delta_t = TIME
        TIME = prochain_evenement[0]
        delta_t = TIME - delta_t
        for usine in reseau.usines :
            usine.actualisation(delta_t)
        for client in reseau.clients :
            client.actualisation(delta_t)
        
        
