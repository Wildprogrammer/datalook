import matplotlib.pyplot as plt
from test2 import RandomWalk
rw=RandomWalk(5000)
rw.fill_walk()
plt.scatter(rw.x_value,rw.y_value,c=rw.y_value,cmap=plt.cm.Blues,s=15)
plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red')
plt.show()
