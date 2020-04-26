import numpy as np


def fill_ndarry(t1):
    for i in  range(t1.shape[1]):#shape[1]为二维数组的列数即(3,4)的第二个参数
        temp=t1[:,i]#遍历取到所有列
        nan_num=np.count_nonzero(temp!=temp)#计算0的个数原理是找F,T个数(0/1)及np.nan!=np.nan
        if nan_num:
            avg_array=temp[temp==temp]#取不为TRUE的值计算平均值
            temp[np.isnan(temp)]=avg_array.mean()#平均值赋给nan值

t1=np.arange(12).reshape((3,4)).astype("float")#定义为浮点型因为nan也为浮点不然报错
t1[1,2:]=np.nan
fill_ndarry(t1)
print(t1)