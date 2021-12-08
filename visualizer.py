import matplotlib.pyplot as plt

class Visualizer():
    def __init__(self):
        pass

    def makePlot(xVal,yVal = None, caption = "Data",l = 15, b = 10,sloc=None,xlab=None,ylab=None):
            plt.figure(figsize=(l,b))        
            plt.title(caption) 
            
            if yVal==None:
                plt.plot(xVal)
            else:
                plt.plot(xVal,yVal)

            if xlab==None and ylab==None:
                pass
            else:
                plt.xlabel(xlab)
                plt.ylabel(ylab)    

            if sloc==None:
                plt.show()
            else:
                plt.savefig(sloc)