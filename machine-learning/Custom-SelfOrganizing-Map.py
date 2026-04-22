import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Credit_Card_Applications.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
X=X[:,1:]
from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
X=sc.fit_transform(X)

from minisom import MiniSom
som=MiniSom(x=10,y=10,input_len=14,sigma=1,learning_rate=0.5)
som.random_weights_init(X)
som.train_random(data=X,num_iteration=100)

#Visualising results

from pylab import bone,pcolor,colorbar,show,plot
bone()
pcolor(som.distance_map().T) #used to get mean internodal dist for all
colorbar()
markers=['o','s']
colors=['r','g']
for i,x in enumerate(X):
    w=som.winner(x) #To get the winner node
    plot(w[0]+0.5,w[1]+0.5,markers[y[i]],markeredgecolor=colors[y[i]],markerfacecolor='None',markersize=10,markeredgewidth=2)
show()

#Identifying fraud customers
mappings=som.win_map(X)
# Get the list of data points mapped to neuron (6,4). Use .get() to handle cases where the key might not exist.
frauds_at_6_4 = mappings.get((6,4), [])

# Check if the list of frauds for this neuron is not empty before inverse transforming
if frauds_at_6_4:
    # Convert the list of arrays to a 2D numpy array
    frauds = np.array(frauds_at_6_4)
    # Inverse transform the scaled fraud data to get original values
    frauds = sc.inverse_transform(frauds)
    print(f"Number of potential fraud customers mapped to neuron (6,4): {len(frauds)}")
    print("Original data of potential fraud customers:\n", frauds)
else:
    frauds = np.array([]) # Assign an empty numpy array if no frauds found
    print("No customers mapped to neuron (6,4).")
