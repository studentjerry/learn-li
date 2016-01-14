import numpy as np
import matplotlib.pyplot as plt

data=[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]
dataT=np.mat(data).T
plt.scatter(dataT[0],dataT[1],c='red',marker='o')
x=np.linspace(0,10,100)
y=2*x+1
plt.plot(x,y)
plt.show()

