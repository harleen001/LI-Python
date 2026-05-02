import time
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn import metrics
from sklearn.datasets import make_blobs
n_samples = [10,20,50,100,200,500,1000,2000,3000,5000,7500,10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_ms = []
homo_ms=[]
complete_ms=[]

for i in tqdm(n_samples):
    X,labels_true = make_blobs(n_samples=i, centers=centers, cluster_std=0.4,random_state=101)
    t1 = time.time()
    ms_model = MeanShift().fit(X)
    t2=time.time()
    t_ms.append(t2-t1)
    homo_ms.append(metrics.homogeneity_score(labels_true,ms_model.labels_))
    complete_ms.append(metrics.completeness_score(labels_true,ms_model.labels_))
plt.figure(figsize=(8,5))
plt.title("Time complexity of Mean Shift\n",fontsize=20)
plt.scatter(n_samples,t_ms,edgecolors='k',c='green',s=100)
plt.plot(n_samples,t_ms,'k--',lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples",fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Time taken for model (sec)",fontsize=15)
plt.show()