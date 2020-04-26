import numpy as np
import random
# a=np.array(range(6),dtype="f2")#f2为float类型16位
# b=np.arange(6)
# c=b.astype("int8")#重定义类型
# d=[random.random() for i in range(4)]#random()中不要写范围，自动生成0到1小数
# e=np.array(d)
# f=np.round(e,2)#np取2位小数
# h=round(random.random(),2)#python中取小数操作，只能对数实用，不能对列表使用
# j="%.2f"%random.random()#效果和上面一样
#
# print(a,b,c,b.dtype,f,h,j)
#

# #处理数组
# a=np.arange(12)
# b=a.reshape((3,4))
# c=a.reshape(2,2,3)
# d=c.flatten()
# print(b,c,d,a.shape)

#数组计算
# a=np.arange(12)
# b=a.reshape((3,4))
#数组和数计算广播机制，一维数组和二维数组相同机制计算(行同或列同，或都同)，0也可以计算
#二维数组和三维数组(3,3,2)与(3,2),(3,3)能算(3,3,3)与(3,3)能与(3,2)不能

# numpy中读数据方法np.loadtxt(frame.dtype=np.float，delimiter=None,skiprows=O,usecols=None,unpack=False)#delimiter为按什么分割
#skiprows为跳过哪一行，usecols为索引，uppack列表变换
# t1=np.arange(24).reshape((4,6))
# t1.transpose()#还可用t1.T或t1.swapaxes(1,0)
# c=b[1:]#取行
# d=b[[0,1]]#取0,1行
# e=b[1,:]#取列
# f=b[1:,:]
# g=b[[0,2],:]
# h=b[:,0]#取第一列
# j=b[1,2]
# print(c,d,e,f,g,j)
# k=b[0:3]
# print(k)
# b[b>10]=15
# print(b)
# p=b.clip(6,8)#小于6的替换6，大于8替换为8
# print(p)
# n=np.where(p<=6,3,10)#np操作列表<=6替换为3，大于替换为10
# print(n)

# #练习
# # numpy统计方法
# print(np.nan==np.nan)#nan值不同
# a=np.arange(24).reshape((4,6))
# b=np.sum(a)#数据中有一个nan值就为nan
# c=np.sum(a,axis=1)#选的为1为列，计算行的值，和别说的行列不同，我理解的行
# d=a.sum()
# e=a.mean(axis=1)#计算均值
# f=np.median(a)#中值
# g=np.ptp(a)#极值
# h=np.std(a)#标准差，与平均数间差值，反应波动
# print(b,c,e,f)

# a=np.eye(5)#对角为1正方
# b=np.zeros((5,1))#5行1列数组
# c=np.hstack((a,b))#水平拼接行同a列同b
# c[[1,2],:]=c[[1,1],:]#交换
# e=c.copy()#防止互相影响给副本
# print(c)
#
a=np.array(range(10)).reshape((2,5))
print(type(a))
c=np.array([[1,2],[3,4]])#用了tolist方法后类型就为list类，用不了flatten()方法
d=c.flatten()
print(type(c))
b=a.flatten()
print(c)
print(a)
print(b)
print(d)


