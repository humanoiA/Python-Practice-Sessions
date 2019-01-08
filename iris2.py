import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets
iris=datasets.load_iris()
x=iris.data[:,:2]
#print(x)
y=iris.target
c=1.0
svc=svm.SVC(kernel='linear',C=1,gamma=0.001).fit(x,y)
x_min,x_max=x[:,0].min()-1,x[:,0].max()+1
y_min,y_max=x[:,0].min()-1,x[:,0].max()+1
h=(x_max/x_min)/100
xx,xy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
plt.subplot(1,1,1)
z=svc.predict(np.c_[xx.ravel(),xy.ravel()])
z=z.reshape(xx.shape)
plt.contourf(xx,xy,z,cmp=plt.cm.Paired,alpha=0.8)
plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.Paired)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.xlim(xx.min(),xx.max())
plt.title('Mera Jadoo')
plt.show()