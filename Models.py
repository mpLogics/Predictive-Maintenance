from sklearn import datasets,linear_model
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,mean_squared_error, r2_score

from keras.models import Sequential
from keras.layers import CuDNNLSTM,Dense,Dropout,LSTM,Flatten,Conv2D,GlobalAveragePooling2D,TimeDistributed,Input

class Linear_Regressor():
    def __init__(self):
        self.lr_model = None
    
    def build_model(self):
        self.lr_model = linear_model.LinearRegression()

class SV_Regressor():
    def __init__(self):
        self.C = [0.001, 0.1, 1, 10, 100, 1000]
        self.gamma = [10, 1, 0.1, 0.01, 0.001, 0.0001]
        self.kernel = ['rbf']
        self.param_grid = {'C':self.C,
                          'gamma':self.gamma,
                          'kernel':self.kernel}
        self.grid = None
        
    def build_model(self):
        self.grid = GridSearchCV(SVR(), self.param_grid, refit = True, verbose = 3)

        
class LSTM_Seq_Pred():
    def __init__(self):
        self.LSTM_layers = 1
        self.list_units = [32]
        self.input_shape = None
        self.add_dropout = True
        self.loss = 'mse'
        self.optimizer = 'rmsprop'
        self.model=None
        
        
    def build_model(self):
        self.model = Sequential()
        self.model.add(CuDNNLSTM(self.list_units[0],return_sequences=True, input_shape=self.input_shape))
        for i in range(1,self.LSTM_layers):
            if i==self.LSTM_layers-1:
                self.model.add(CuDNNLSTM(self.list_units[i],return_sequences=False))
            else:
                self.model.add(CuDNNLSTM(self.list_units[i],return_sequences=True))
        if self.add_dropout:
            self.model.add(Dropout(0.5))
        self.model.add(Dense(1))
        self.model.summary()
        self.model.compile(loss='mse', optimizer='rmsprop')