from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,24,22,18,15]
plt.figure(figsize=(20,8),dpi=40)#设置图片精度
a=[i/2 for i in range(4,49)]
plt.xticks(a[::3])#传入精度为0.5的数据取取步长3
plt.yticks(range(min(y),max(y)))
plt.plot(x,y)#画图
# plt.savefig("./t1.png")
plt.savefig("./t2.svg")

plt.show()

