import numpy as np, matplotlib.pyplot as plt

X=np.array([[2,120,70,20,80,25,0.5,30],[4,150,80,25,90,30,0.7,45],
            [1,85,60,18,60,22,0.3,25],[6,180,90,30,120,35,0.9,50],
            [3,95,65,20,70,23,0.4,28],[5,160,85,28,100,33,0.8,48]])
y=np.array([0,1,0,1,0,1])

X=(X-X.mean(0))/X.std(0)
def knn(X,y,q,k=3): d=np.sqrt(((X-q)**2).sum(1)); return int(round(y[np.argsort(d)[:k]].mean()))

q=np.array([2,130,72,22,85,26,0.6,32]); q=(q-X.mean(0))/X.std(0)
print("Prediction (1=Diabetic,0=Not):", knn(X,y,q))

plt.scatter(X[:,1],X[:,7],c=y,cmap="coolwarm",s=100)
plt.xlabel("Glucose"); plt.ylabel("Age"); plt.title("Diabetes Prediction using KNN"); plt.show()