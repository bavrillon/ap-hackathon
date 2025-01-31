import numpy as np 
import pandas as pd



class Reseau:
    def __init__(self):
        self.usines = []
        self.clients = []
        
reseau = Reseau()
        

class Usine:
    def __init__(self, coord_x,coord_y,capacity,init, refill,id):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.refill=refill
        self.id=id

class Client:
    def __init__(self, coord_x,coord_y,capacity,init, consumption,id):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.consumption=consumption
        self.id=id
        

class Camion:
    def __init__(self,id):
        self.id=id

class Trajet:
    def __init__(self,ID,start,stop,nb_bouteilles):
        self.ID=ID
        

class Bouteille:
    pass


df_plants= pd.read_csv('plants.csv')

df_plants.insert(0, "Index", range(0, len(df_plants)))
df_plants= df_plants.set_index('Index')

for k in range(len(df_plants)):
    reseau.usines.append(Client(df_plants['coord_x'][k],df_plants['coord_y'][k],df_plants['capacity'][k],df_plants['init'][k],df_plants['refill'][k],id))

df_clients=pd.read_csv('clients.csv')

df_clients.insert(0, "Index", range(0, len(df_clients)))
df_clients= df_clients.set_index('Index')

for k in range(len(df_clients)):
    reseau.clients.append(Client(df_clients['coord_x'][k],df_clients['coord_y'][k],df_clients['capacity'][k],df_clients['init'][k],df_clients['consumption'][k],id))

 
