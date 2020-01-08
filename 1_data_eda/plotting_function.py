"""
可视化函数
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
视图通用设置
"""
#中文显示，避免方框展示
plt.rcParams['font.sans-serif']=['SimHei']
#坐标轴显示负号
plt.rcParams['axes.unicode_minus']=False
#创建图像区域
plt.figure(figsize=(10,8))

#线性图1
# x=np.linspace(0,2*np.pi,100)
# y=np.sin(x)
# plt.plot(x,y,'bp--')
# plt.show()

#线性图2
# plt.figure()
# data=pd.DataFrame([[1,2,3,4,5,6,7,8]])
# data.plot(kind='line',)
# plt.show()

#饼图
# plt.figure()
# labels=["A","B","C","D"]
# sizes=[15,20,35,16]
# colors=['yellow','green','lightskyblue','lightcoral']
# explode=[0,0.5,0,0.1]
# plt.pie(sizes,explode=explode,labels=labels, \
#         colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
# #axis square刻度范围不一定一样，但是一定是方形的
# #axis equal刻度是等长的，但也不一定是方形的
# plt.axis('equal')
# plt.show()

#条形图
# plt.figure()
# x=np.random.randn(500)
# plt.hist(x,10)
# plt.show()

#箱型图
# x=np.random.randn(500)
# plt.figure()
# xxt=pd.DataFrame([x,x+1]).T
# xxt.plot(kind='box')
# plt.show()

#误差条形图
# err=np.random.randn(10)
# y=pd.Series(np.sin(np.arange(10)))
# y.plot(yerr=err)
# plt.figure()
# plt.show()

