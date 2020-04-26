import pandas as pd
import numpy as np
# t1=pd.Series([1,3,5,9,4],index=list("abcde"))
# print(t1)
# t2=pd.Series({"id":111,"name":"李磊"})
# a=t2[["name","id"]]#布尔索引取name和id行
# print(t2,t2.values,t2.index)
# print(a)

#读取外部数据
# t1=pd.DataFrame([{"name":"xiaoming","age":18},{"name":"xiaoli","age":24}])#Dataframe可读取序列化的数据
# print(t1)

# #dataFrame中排序的方法
# df=df.sort_values(by= "Count_ Ani ma LName" ,ascending=False)
# # print(df .head(5) )
# #pandas取行或者列的注意点,
# # -方括号写数组，表示取行，对行进行操作
# # -写字符串，表示的去列索引，对列进行操作
# print(df[:20])
# print (df["Row_ Labels"])
# print (tyep(df))

#loc（索引）,iloc（数字）取数据通过标签和位置获取数据
t1=pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("WXYZ"))
print(t1)
t2=t1.loc[['a','c'],['X','Z']]#取a,c对应xz结果是dataframe
t3=t1.loc['a':'c',['X','Z']]#取切片的时候loc方法可以去到'c
t1.iloc[1:,2:]=np.nan
print(t2,t3)
print(t1)
print(t1[(t1['X']>4)&(t1['X']<9)])#取t1列表中x列的值大于4小于9的那一列的值
#.str.split('/').tolist()
print(pd.isnull(t1))
# t1.dropna(axis=0,how="all",inplace=True)#删除行，全为nan的行，改any为只要出现nan,inplace为结果替换当前处理dataframe
t4=np.ones((1,4))
t5=np.vstack((t1,t4))
print(t1,t4,t5)
t5=pd.DataFrame(t5,index=list("abcd"),columns=list("WXYZ"))

t6=t5.fillna(t5.median())#t1.fillna(0),t1.
print(t6)
