import pandas as pd
import numpy as np

class PreProcess():
    def __init__(self):
        self.d_init = None
        self.base_path = 'data/'
        self.data_ext = '.csv'
        self.Column_Names = {'Unnamed: 1': 'band-y',
                             'Unnamed: 4': 'damage-y',
                             'Unnamed: 7': 'peak_acc-y',
                             'Unnamed: 10': 'peak_vel-y',
                             'Unnamed: 13': 'rms-x',
                             'Unnamed: 16': 'tempx-y',
                             'Unnamed: 19': 'peak_acc-x',
                             'Unnamed: 22': 'peak_vel-x',
                             'Unnamed: 25': 'rms-y',
                             'Unnamed: 28': 'temp-y',
                             'Unnamed: 31': 'band-x',
                             'Unnamed: 34': 'damage-x',
                             'Unnamed: 37':'battery'}
        self.Metrics=[]
    
    
    def check_for_null_value(self,df):
        return df.isnull().values.any(),df.isnull().values.sum()
    
    def get_date_time(self,df,Columns):
        df_ = pd.DataFrame()
        df_ = df_.astype(float)

        df_['datetime'] = pd.to_datetime(df[Columns[0]][1:])
        df_ = df_.resample('10T',on='datetime')

        for i in range(len(Columns)-1):
            df_[self.Column_Names[Columns[i+1]]] = df[Columns[i+1]].values[1:]

        df_.index = [i for i in range(len(df_.values))]
        self.Metrics.append((Columns[0],self.check_for_null_value(df_)))
        return df_
    
    def clean_and_process(self,df):
        Metrics=[]
        Cols = df.columns
        i=0
        self.d_init = self.get_date_time(df[Cols[i:i+2]],Cols[i:i+2])
        for i in range(2,len(Cols)-1,2):
            d1 = self.get_date_time(df[Cols[i:i+2]],Cols[i:i+2])
            self.d_init = pd.merge(self.d_init,d1)

        self.d_init.fillna(method='pad')
    
    def prep_data(self,path):
        df_set = pd.read_csv(self.base_path + path + self.data_ext)
        df_set = df_set.dropna(how='all',axis=1)
        df_set = self.clean_and_process(df_set)
        return df_set    
    