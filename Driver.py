from Preprocessing import PreProcess
from Models import Linear_Regressor,SV_Regressor,LSTM_Seq_Pred
from Scheduler import scheduler
from train import Train

class Driver():
    def __init__(self):
        self.modality = 'LSTM'
        self.data_preparer = PreProcess()
        self.data_preparer.base_path = 'data/'
        self.data_preparer.data_ext = '.csv'
        self.file_name = 'drill press X'
        self.data=None
            
    def read_data(self):
        self.data = self.data_preparer.prep_data(self.file_name)
    
    def setup_training_data(self):
        y =self.data["damage X"]
        x = self.data.loc[:,self.data.columns!="damage X"]
        return y,x  
    
    def setup_training(self):
        if self.modality=='LSTM':
            lstm_based_1 = LSTM_Seq_Pred()
            lstm_based_1.LSTM_layers = 1
            lstm_based_1.list_units = [32]
            lstm_based_1.build_model()
            agent = lstm_based_1.model
            
        elif self.modality == 'LR':
            lr_1 = Linear_Regressor()
            lr_1.build_model()
            agent = lr_1.lr_model

        elif self.modality == 'SVR':
            svr_1 = SV_Regressor()
            svr_1.build_model()
            agent = svr_1.grid
        
        return agent


if __name__ == '__main__':
    d1 = Driver()
    d1.modality='LSTM'
    d1.read_data()
    y,x = d1.setup_training_data()
    agent = d1.setup_training()

    trainer = Train()
    trainer.train_start_val = 0
    trainer.train_end_val = 1700
    trainer.LSTM_agent = agent
    trainer.LSTM_epochs = 20
    trainer.val_split = 0.1
    trainer.lstm_train(x,y)







