import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

from sklearn.datasets.samples_generator import make_blobs

fig=plt.figure(1)
ax=axisartist.Axes(fig,[0.1,0.1,0.8,0.8])
fig.add_axes(ax)
ax.axis["bottom"].set_axisline_style("->",size=2.0)
ax.axis["left"].set_axisline_style("->",size=2.0)
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)
ax.set_xlabel('X1')
ax.set_ylabel('X2')

data,target=make_blobs(n_samples=30,n_features=2,centers=[[1.5,1],[1,1.5]],cluster_std=0.2,random_state=9)

for i in range(30):
    if target[i]==0:
        plt.scatter(data[i,0],data[i,1],marker='o',facecolors='none',edgecolors='k')
    else:
        plt.plot(data[i,0],data[i,1],'o',marker='x',markeredgecolor="k")
x=np.linspace(0.4, 2.1, 50)
k=0.70
y1=k*x+0.375
y2=k*x+0.50
y3=k*x+0.25
plt.plot(x,y1,color='black')
lx=1.9
plt.annotate('One Hyperplane',xy=(lx,k*lx+0.375),xytext=(lx-0.55,k*lx+0.375+0.2),arrowprops=dict(arrowstyle='->'),)
plt.plot(x,y2,color='black',linestyle='--')
plt.plot(x,y3,color='black',linestyle='--')
plt.xticks([])
plt.yticks([])

plt.savefig("D:/figure1.png")
plt.show()