# -*- coding: utf-8 -*-
"""
销量异常数据检查

对于店品的销量数据，有很多不明确的场景，系统希望通过找出销量异常值
来找出实际销售过程中特殊场景,方便后续业务规则调整

样本数据突变值检测

https://blog.csdn.net/Jasminexjf/article/details/88527966
"""
import base as B

def sale_err_check(df, goods_list):
    err_sku_list = []
    for sku in good_list:
        item_df = df.query('goods_code=={0}'.format(sku))
        err_sku = iqr_check(item_df, sku)
        if err_sku is not None:
            err_sku_list.append('0' * (6 - len(str(err_sku))) + str(err_sku))
    return err_sku_list


# 识别异常值函数
def iqr_check(data, sku):
    err_sku = None
    series = data['qty']
    max = series.max()
    min = series.min()
    if len(series) > 5:
        iqr = series.quantile(0.75) - series.quantile(0.25)
        low = series.quantile(0.25)
        up = series.quantile(0.75) + 5 * iqr
        if min * 10 < low or max > up:
            err_sku = sku
            print("------------",err_sku)
            plt_draw(data)
            pause_flag=True
    return err_sku


def plt_draw(df):
    df=df[['day','qty']]
    df=df.sort_values(by='day',ascending=True)
    df['day']=df['day'].astype('str')#x轴 时间必须转换为字符串
    df.index=df['day']
    fig = B.plt.figure()
    ax = fig.add_subplot(111)
    df.plot(kind='line', ax=ax)
    B.plt.show()



if __name__ == '__main__':
    input_file = 'sale_data.csv'
    df = B.pd.read_csv(input_file)
    good_list = df['goods_code'].drop_duplicates().values.tolist()
    # print("店品列表:", good_list)
    # print("总共多少个店品:", len(good_list))
    # print(df.query('goods_code==941047'))
    list = sale_err_check(df, good_list)
    print("异常店品=", len(list))
    print("异常店品=", list)

