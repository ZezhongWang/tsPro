#encoding:utf-8
import pandas as pd


def calc_corr(stock_dict):
    # data = pd.read_pickle('code_k_data_part.pkl').to_frame()
    stock_dict = pd.Panel(stock_dict).to_frame()
    for index in stock_dict.index[0]:
        index = str(index)
        print(index)
        stock_dict[index] = stock_dict[index].drop(['ma5'], axis=0)
    # df = pd.Panel(stock_dict).to_frame()
    corr = stock_dict.corr()
    # corr = df.corr()  # ¼ÆËãÏà¹ØÏµÊý
    corr_strong = corr[corr >= 0.8]
    print(corr)
    print(corr[corr >= 0.8])
    corr.to_csv('/home/lijiaheng/corr.csv')
    stock_dict.axes
    corr_strong.to_csv('/home/lijiaheng/corr_string.csv')