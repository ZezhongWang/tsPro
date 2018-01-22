#encoding:utf-8
import pandas as pd


def calc_corr():
    stock_panel= pd.read_pickle('code_k_data_part.pkl')

    for key, data in stock_panel.iteritems():
        stock_panel[key] = stock_panel[key].drop(['turnover'], axis=1)

    df = pd.Panel(stock_panel).to_frame()
    corr = stock_panel.corr()
    # corr = df.corr()  # ¼ÆËãÏà¹ØÏµÊý
    corr_strong = corr[corr >= 0.8]
    print(corr)
    print(corr[corr >= 0.8])
    corr.to_csv('/home/lijiaheng/corr.csv')
    stock_panel.axes
    corr_strong.to_csv('/home/lijiaheng/corr_string.csv')