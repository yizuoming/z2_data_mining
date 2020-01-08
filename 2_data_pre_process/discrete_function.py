# -*- coding: utf-8 -*-
"""
数据规范化--离散处理
----------------------------------------------------------------------------
为什么需要离散化？
通俗的说，离散化是在不改变数据相对大小的条件下，对数据进行相应的缩小。例如：
原数据：1,999,100000,15；
处理后：1,3,4,2；
原数据：{100,200}，{20,50000}，{1,400}；
处理后：{3,4}，{2,6}，{1,5}；

1**.算法需要：**

比如决策树、朴素贝叶斯等算法，都是基于离散型的数据展开的。如果要使用该类算法，必须将离散型的数据进行。有效的离散化能减小算法的时间和空间开销，提高系统对样本的分类聚类能力和抗噪声能力。

2**.离散化的特征相对于连续型特征更易理解，更接近知识层面的表达**

比如工资收入，月薪2000和月薪20000，从连续型特征来看高低薪的差异还要通过数值层面才能理解，但将其转换为离散型数据（底薪、高薪），则可以更加直观的表达出了我们心中所想的高薪和底薪。

3.可以有效的克服数据中隐藏的缺陷，使模型结果更加稳定

----------------------------------------------------------------------------



https://blog.csdn.net/weixin_40683253/article/details/81780910
https://blog.csdn.net/xzfreewind/article/details/77102835

"""
import algorithms as ams
import base as B

input_file='../0_data_file/pre/discretization_data.xls'
data=B.pd.read_excel(input_file)
data=data[u'肝气郁结证型系数'].copy()
k=4 #设置离散之后的数据段为4
# 等宽离散化(将属性的值域从最小值到最大值分成具有相同宽度的n个区间，n由数据特点决定，往往是需要有业务经验的人进行评估)
d1 = B.pd.cut(data, k, labels=range(k))

# 等频率离散化(将相同数量的记录放在每个区间，保证每个区间的数量基本一致)
w = [1.0 * i / k for i in range(k + 1)]
w = data.describe(percentiles=w)[4:4 + k + 1]  # 使用describe函数自动计算分位数
w[0] = w[0] * (1 - 1e-10)
d2 = B.pd.cut(data, w, labels=range(k))

#k-means聚类离散
kmodel = ams.KMeans(n_clusters=k, n_jobs=4)  # 建立模型，n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data.values.reshape((len(data), 1)))  # 训练模型
c = B.pd.DataFrame(kmodel.cluster_centers_).sort_values(0)  # 输出聚类中心，并且排序（默认是随机序的）
w = c.rolling(2).mean().iloc[1:]  # 相邻两项求中点，作为边界点
w = [0] + list(w[0]) + [data.max()]  # 把首末边界点加上
d3 = B.pd.cut(data, w, labels=range(k))

def cluster_plot(d, k):  # 自定义作图函数来显示聚类结果

    B.plt.figure(figsize=(8, 3))
    for j in range(0, k):
        B.plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    B.plt.ylim(-0.5, k - 0.5)
    return B.plt


cluster_plot(d1, k).show()

cluster_plot(d2, k).show()
cluster_plot(d3, k).show()