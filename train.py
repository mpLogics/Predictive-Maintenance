from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
from sklearn import datasets,linear_model
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,mean_squared_error, r2_score

from Models import Linear_Regressor,LSTM_Seq_Pred,SV_Regressor

class Train():
    def __init__(self):
        self.train_start_val = 0
        self.train_end_val = 1700
        self.lr_agent = None
        self.svr_agent = None
        self.LSTM_agent = None
        self.LSTM_epochs = 20
        self.val_split = 0.1
        
    def lr_trainer(self,x,y):
        x_train = x[self.train_start_val:self.train_end_val]
        y_train = y[self.train_start_val:self.train_end_val]
        
        x_test = x[self.train_end_val:]
        y_test = y[self.train_end_val:]
        
        h = self.lr_agent.fit(x_train,y_train)
        y_p = self.lr_agent.predict(x_test)

        print(mean_squared_error(y_test, y_p))
        print(r2_score(y_test, y_p))
    
    def svr_trainer(self,x,y):
        x_train = x[self.train_start_val:self.train_end_val]
        y_train = y[self.train_start_val:self.train_end_val]
        
        x_test = x[self.train_end_val:]
        y_test = y[self.train_end_val:]

        self.svr_agent.fit(x_train, y_train)
        y_pred = self.svr_agent.predict(x_test)

    def lstm_train(self,x,y):
        try:
            session.close()
            print("All previous sessions closed.")
        except:
            print("No previous session exists. Commencing a new session.")
        
        x_train = x[self.train_start_val:self.train_end_val]
        y_train = y[self.train_start_val:self.train_end_val]
        
        x_test = x[self.train_end_val:]
        y_test = y[self.train_end_val:]
        

        config = ConfigProto()
        config.gpu_options.allow_growth = True
        session = InteractiveSession(config=config)
        
        history = self.LSTM_agent.fit(x_train,y_train,epochs=20,validation_split=self.val_split)
        self.LSTM_agent.evaluate(x_test,y_test)


        