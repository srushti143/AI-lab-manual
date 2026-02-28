import pandas as pd, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.DataFrame({'Age':[22,25,47,52,46,56,55,60,28,30],
                 'Experience':[1,3,20,25,18,30,28,35,5,7],
                 'Income':[15000,20000,85000,100000,80000,120000,110000,150000,30000,35000]})

print("Employee Dataset:\n", df)
data_scaled = StandardScaler().fit_transform(df)
df['Cluster'] = KMeans(n_clusters=3, random_state=42).fit_predict(data_scaled)

plt.scatter(df['Experience'],df['Income'],c=df['Cluster'],cmap='viridis')
plt.xlabel('Experience'); plt.ylabel('Income'); plt.title('Employee Income Clusters'); 
plt.show()