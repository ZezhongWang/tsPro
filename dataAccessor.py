import tushare as ts
import pandas as pd
import pickle


class DataAccessor(object):

    # hist_data = ts.get_hist_data(ktype='5')
    def run(self, size='all'):
        code_list = ts.get_area_classified()
        sh_code_prefix = ['600', '601', '603']
        sh_code_list = []

        # get shang hai code list
        for index, row in code_list.iterrows():
            code = row[0]
            if code[:3] in sh_code_prefix:
                sh_code_list.append(code)

        # get shang hai code deata
        code_k_data = {}
        if size == 'all':
            for sh_code in sh_code_list:
                code_k_data[sh_code] = ts.get_k_data(sh_code, ktype='5', start='2018-01-15', end='2018-01-19')
                code_k_data_panel = pd.Panel(code_k_data)
                code_k_data_panel.to_pickle('code_k_data_all.pkl')
        elif size == 'part':
            for sh_code in sh_code_list[:5]:
                code_k_data[sh_code] = ts.get_k_data(sh_code, ktype='5', start='2018-01-15', end='2018-01-19')
                code_k_data_panel = pd.Panel(code_k_data)
                code_k_data_panel.to_pickle('code_k_data_part.pkl')


