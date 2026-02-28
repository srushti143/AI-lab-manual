import numpy as np, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X,y=np.arange(1,11).reshape(-1,1),np.array([35000,38000,42000,46000,50000,55000,60000,65000,70000,75000])
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)

lr=LinearRegression().fit(Xtr,ytr)
poly=PolynomialFeatures(2); pr=LinearRegression().fit(poly.fit_transform(Xtr),ytr)

print("R² Linear:", r2_score(yte,lr.predict(Xte)))
print("R² Poly:", r2_score(yte,pr.predict(poly.transform(Xte))))

plt.scatter(X,y)
plt.plot(X,lr.predict(X),'r',X,pr.predict(poly.transform(X)),'g'); plt.show()