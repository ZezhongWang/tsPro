import tushare as ts
import pandas as pd
from matplotlib.pylab import date2num
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import datetime

def draw_line_chart():
    tick_data = pd.read_pickle('code_k_data_part.pkl')
    tick_data.axes[0]
    def draw_k_line(code):
        hist_data = tick_data[code]
        data_list = []
        for dates, row in hist_data.iterrows():
            date_time = datetime.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
            t = date2num(date_time)
            _open, high, low, close = row[:4]
            datas = (t, _open, high, low, close)
            data_list.append(datas)
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis_date()
        plt.xticks(rotation=45)
        plt.yticks()
        plt.title(code)
        plt.xlabel("Time")
        plt.ylabel("Price(RMB)")
        mpf.candlestick_ohlc(ax, data_list, width=0.005, colorup='r', colordown='green', alpha=0.7)
        plt.grid()
        plt.savefig('/home/wangzezhong/PycharmProjects/tsPro/klinePicture/' + str(code) + '.png')
    [draw_k_line(code) for code in tick_data]
