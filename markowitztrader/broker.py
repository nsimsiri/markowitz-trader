class Broker(object):
    
    def __init__(self):
        self.history = []

    def addHistory(self, history):
        self.history += history