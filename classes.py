import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from classes import *

class Reseau:
    def __init__(self):
        self.usines = []
        self.clients = []
        self.file_events = FilePrioriteEvenements

class Usine:
    def __init__(self, coord_x,coord_y,capacity,init, refill,ID):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.refill=refill
        self.ID=ID
        self.bouteilles_pleines=init
        self.bouteilles_vides=0

    def bouteilles_tot(self):
        return(self.bouteilles_pleines + self.bouteilles_vides)

    def actualisation(self, detla_t):
        self.bouteilles_pleines += self.refill*delta_t
        self.bouteilles_vides -= self.consumption*delta_t

class Client:
    def __init__(self, coord_x,coord_y,capacity,init, consumption,ID):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.consumption=consumption
        self.ID=ID
        self.bouteilles_pleines=0
        self.bouteilles_vides=init

        def bouteilles_tot(self):
            return(self.bouteilles_pleines + self.bouteilles_vides)

        def autonomy(self):
            return(self.bouteilles_pleines/self.consumption)

        def actualisation(self, detla_t):
            self.bouteilles_pleines -= self.consumption*delta_t
            self.bouteilles_vides += self.consumption*delta_t
        

class Camion:
    def __init__(self,id):
        self.id=id
        self.bouteilles_vides=0
        self.bouteilles_pleines=0
        self.capacity=80
        self.usine = ?
        
    @classmethod
    def parametres_trajet(cls, depart, destination):
        vitesse = 50 * 24 #en km/jour
        cout_kilometrique = 0.10
        distance = np.sqrt((depart.coord_x - depart.coord_x)**2 + (destination.coord_y - destination.coord_y)**2)
        duree_trajet = distance / vitesse
        cout_trajet = cout_kilometrique * distance
        return(duree_trajet, cout_trajet)
    
    def bouteilles_tot(self):
            return(self.bouteilles_pleines + self.bouteilles_vides)

    def livraison_client(self, client):
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
        echange1 = min(client.bouteilles_vides, self.bouteilles_pleines)
        self.bouteilles_pleines -= echange1
        self.bouteilles_vides += echange1
        client.bouteilles_pleines += echange1
        client.bouteilles_vides -= echange1
        COST += echange1 * 100
        if self.bouteilles_pleines == 0 :
            echange_2a = min(self.capacity-self.bouteilles_tot(), client.bouteilles_vides)
            self.bouteilles_vides += echange_2a
            client.bouteilles_vides -= echange_2a
        else:
            echange_2b = min(client.capacity-client.bouteilles_tot(), self.bouteilles_pleines)
            client.bouteilles_pleines += echange_2b
            self.bouteilles_pleines -= echange_2b
            COST += echange2 * 100
        assert(self.bouteilles_tot <= self.capacity)
        assert(usine.bouteilles_tot <= usine.capacity)
        assert(client.bouteilles_tot <= client.capacity)

    def recharge_camion(self, usine):
    # Cas où les camions sont toujours pleins car ils repassent à l'usine après chaque livraison
        echange1 = min(self.bouteilles_vides, usine.bouteilles_pleines)
        usine.bouteilles_pleines -= echange1
        usine.bouteilles_vides += echange1
        self.bouteilles_pleines += echange1
        self.bouteilles_vides -= echange1
        COST -= echange1 * 40
        if usine.bouteilles_pleines == 0 :
            echange_2a = min(usine.capacity-usine.bouteilles_tot(), self.bouteilles_vides)
            usine.bouteilles_vides += echange_2a
            self.bouteilles_vides -= echange_2a
        else:
            echange_2b = min(self.capacity-self.bouteilles_tot(), usine.bouteilles_pleines)
            self.bouteilles_pleines += echange_2b
            usine.bouteilles_pleines -= echange_2b
            COST -= echange2 * 40
        assert(self.bouteilles_tot <= self.capacity)
        assert(usine.bouteilles_tot <= usine.capacity)
        assert(client.bouteilles_tot <= client.capacity)




class FilePrioriteEvenements:
    def __init__(self):
        self.file = []
    
    def ajouter_evenement(self, tps_trajet, depart, destination, usine):
        tps_arrivee = TIME + tps_trajet  
        heapq.heappush(self.file, (tps_arrivee, depart, destination, usine))

    def obtenir_prochain_evenement(self):
        prochain_camion = heapq.heappop(self.file)
        return(prochain_camion)



class Bouteille:
    pass


df_plants= pd.read_csv('data/plants.csv')

df_plants.insert(0, "Index", range(0, len(df_plants)))
df_plants= df_plants.set_index('Index')

for k in range(len(df_plants)):
    reseau.usines.append(Client(df_plants['coord_x'][k],df_plants['coord_y'][k],df_plants['capacity'][k],df_plants['init'][k],df_plants['refill'][k],k))

df_clients=pd.read_csv('data/clients.csv')

df_clients.insert(0, "Index", range(0, len(df_clients)))
df_clients= df_clients.set_index('Index')

for k in range(len(df_clients)):
    reseau.clients.append(Client(df_clients['coord_x'][k],df_clients['coord_y'][k],df_clients['capacity'][k],df_clients['init'][k],df_clients['consumption'][k],k))

 
