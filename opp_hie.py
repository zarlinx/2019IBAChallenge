import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

df = pd.read_csv("Opp_sorted_FINAL.csv", usecols = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38])
data = df.values

import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))  
plt.title("opportunity Dendograms")  
dend = shc.dendrogram(shc.linkage(data, method='ward'))