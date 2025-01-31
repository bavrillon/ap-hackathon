import numpy as np 
import pandas as pd



class Reseau:
    def __init__(self):
        self.usines = []
        self.clients = []
        
reseau = Reseau()
        

class Usine:
    def __init__(self, coord_x,coord_y,capacity,init, refill,ID):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.refill=refill
        self.ID=ID
        self.bp=init
        self.bv=0
        self.btot=self.bp+self.bv

class Client:
    def __init__(self, coord_x,coord_y,capacity,init, consumption,ID):
        self.coord_x=coord_x
        self.coord_y=coord_y
        self.capacity=capacity
        self.init=init
        self.consumption=consumption
        self.ID=ID
        self.bp=0
        self.bv=init
        self.btot=self.bp+self.bv
        

class Camion:
    def __init__(self,id):
        self.id=id
        self.bv=0
        self.bp=0
        self.btot=self.bp+self.bv

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

 
