from processor.drawLineChart import draw_line_chart
from processor.calcCorr import calc_corr

class DataProcessor(object):

    def run(self):
        calc_corr()
        draw_line_chart()


    