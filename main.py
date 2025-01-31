import heapq
from Classes import *


reseau = Reseau()
TIME = 0 # en jours
COST = 0

while TIME <= 30 :
    reseau.file_events.obtenir_prochain_evenement()
