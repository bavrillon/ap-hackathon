import heapq
import ....


reseau = Reseau()
TIME = 0

class FilePrioriteEvenements:
    def __init__(self):
        self.file = []
    
    def ajouter_evenement(self, destination, tps_trajet):
        tps_arrivee = TIME + tps_trajet  
        heapq.heappush(self.file, (tps_arrivee, destination))

    def recuperer_prochain_evenement(self):
        return heapq.heappop(self.file)
