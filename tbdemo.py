from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# # #练习1：
# my_font=font_manager.FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc",size=14)#设置字体大小
# x=range(0,120)
# y=[random.randint(20,35) for i in range(120)]
#
#
# correspond_x=["10点{}分".format(i) for i in range(60)]
# correspond_x+=["11点{}分".format(i) for i in  range(60)]
#
#
# plt.xticks(list(x)[::6],correspond_x[::6],rotation=45,fontproperties=my_font)
# plt.plot(x,y)
# plt.xlabel("时间 单位(min)",fontproperties=my_font)
# plt.ylabel("温度 单位(℃)",fontproperties=my_font)
# plt.title("10点到13点实时温度表",fontproperties=my_font)
# plt.grid(alpha=0.4)#设置网格，括号内为透明度
# plt.show()

# #练习二:双折线图
# my_font=font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc",size=14)
# y_1=[1,2,5,5,6,4,5,6,3,3,6,8,4,3,2,4,5,3,5,2]
# y_2=[4,2,4,5,6,7,4,1,3,4,1,5,6,3,2,4,5,6,3,1]
# x=range(11,31)
#
# plt.figure(figsize=(26,18),dpi=60)
# plt.plot(x,y_1,label="甲",color="red",linestyle="--")#图例样式
# plt.plot(x,y_2,label="乙",color="#3232CD",linestyle="-.")
#
# correspond_x=["{}岁".format(i) for i in  range(11,31)]
# plt.xticks(x,correspond_x,fontproperties=my_font)
#
# plt.grid(alpha=0.3,linestyle=":")#设置网格透明度，样式
#
# plt.legend(prop=my_font,loc="upper left")#设置中文，只有这里参数名不一样,设置图裂位置
# plt.show()
#

# #练习3散点图
# my_font=font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc",size=16)
# # 准备数据
# x_3=range(1,32)
# x_10=range(51,82)
# y_3=[11,17,16,13,18,16,13,4,5,7,12,12,16,18,18,16,24,23,21,23,22,23,12,14,12,23,31,23,12,12,22]
# y_10=[23,21,12,13,21,23,12,21,31,21,21,12,22,22,21,14,14,15,17,15,14,13,23,21,23,14,12,13,12,7,8,]
#
# #设置图像大小
# plt.figure(figsize=(12,8),dpi=40)
# #画点
# plt.scatter(x_3,y_3,label="3月份")
# plt.scatter(x_10,y_10,label="10月份")
# #调整刻度
# _x=list(x_3)+list(x_10)
# corrspond_x=["3月{}日".format(i) for i in x_3]
# corrspond_x+=["10月{}日".format(i+50) for i in x_10]
# plt.xticks(_x[::6],corrspond_x[::6],fontproperties=my_font,rotation=45)
#
# #设置行属性
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度",fontproperties=my_font)
# plt.title("气温图",fontproperties=my_font)
#
# plt.show()
#

# # 练习4:条形图
# my_font=font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc",size=16)
# a=["叶问4","暗杀","芳华"]
# b_16=[5764,2321,4491]
# b_15=[4451,2001,3984]
# b_14=[3888,1889,3902]
#
# bar_width=0.1
# x_14=list(range(len(a)))
# x_15=[i+bar_width for i in x_14]
# x_16=[i+bar_width*2 for i in x_14]
#
# plt.figure(figsize=(20,8),dpi=60)
#
# plt.bar(x_14,b_14,width=bar_width,label="12月14日")
# plt.bar(x_15,b_15,width=bar_width,label="12月15日")
# plt.bar(x_16,b_16,width=bar_width,label="12月16日")
#
# plt.xticks(x_15,a,fontproperties=my_font,rotation=270)
#
# plt.legend(prop=my_font)
# plt.show()

# 练习5:直方图
a=[185,123,212,121,242,241,241,211,121,211,121,212,242,142,154,186,151,151,189,194,249,158,264,244,267,244,194,156,134,134,184,146,167,177,271,173]
#合理计算组距，组数

d=25
temp=max(a)-min(a)
num_bins=temp//d#组数=列表A的最大值-最小值整除组距，组数保持整除可使图像位置准确
print(num_bins,temp)

plt.figure(figsize=(12,8),dpi=60)
plt.hist(a,num_bins,data=True)#画直方图，按百分比,传数据列表和组数

plt.xticks(range(min(a),max(a)+d,d))#x轴以min(a)为起点，max(a)为终点(+d是为了使最后一格显示完整），步长为d，和前面图对应关系不同
plt.grid()
plt.show()
