import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,y=load_iris(return_X_y=True)
sc=StandardScaler(); X=sc.fit_transform(X)
pca=PCA(1); X=pca.fit_transform(X)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression().fit(Xtr,ytr)
print("Accuracy:",accuracy_score(yte,model.predict(Xte)))
new=np.array([[5.1,3.5,1.4,0.2]]); new=pca.transform(sc.transform(new))
print("Predicted Species:", load_iris().target_names[model.predict(new)][0])