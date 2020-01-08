# -*- coding: utf-8 -*-
"""
贡献度分析，重要程度
"""
import base as B

input_file='../0_data_file/eda/catering_dish_profit.xls'
df=B.in_excel(input_file,u"菜品名")
#单独提取一列
col_df=df[u'盈利'].copy()
#降序
col_df.sort_values(ascending=False)
print(col_df)
B.plt.figure()
col_df.plot(kind='bar')
B.plt.ylabel("盈利(元)")
p=1.0*col_df.cumsum() / col_df.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
B.plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
B.plt.ylabel("盈利（比例）")
B.plt.show()








