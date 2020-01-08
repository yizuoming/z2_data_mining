import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号


#获取excel
def in_excel(path,col):
    df=pd.read_excel(path,index_col=col)
    return df

def in_excel_header(path,header):
    if header=="":
       header=None
    df=pd.read_excel(path,header=header)
    return df

