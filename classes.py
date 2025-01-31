import numpy as np 
import pandas as pd



class Reseau:
    def __init__(self):
        self.usines = []
        self.clients = []        

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

        def actualisation(self, detla_t):
            self.bouteilles_pleines -= self.consumption*delta_t
            self.bouteilles_vides += self.consumption*delta_t
        

class Camion:
    def __init__(self,id):
        self.id=id
        self.bouteilles_vides=0
        self.bouteilles_pleines=0
        self.capacity=80
        
    def bouteilles_tot(self):
            return(self.bouteilles_pleines + self.bouteilles_vides)

class Trajet:
    def __init__(self, ID, date_start, date_end, departure, destination, nb_bouteilles):
        self.ID=ID
        
        

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

 
