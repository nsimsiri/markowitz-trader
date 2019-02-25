import abc
from abc import ABC
from event import MarketEvent

class BaseDataFeed(ABC):
    ''' Abstract class for broadcasting new market signals.
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def next_bar(self):
        pass
    
    @abc.abstractmethod
    def update(self):
        pass
    
    @value.setter
    def event_queue(self, queue):
        pass


class HistoricOLHCDataFeed(BaseDataFeed):
    ''' a feed for daily OHLC data (open, low, high, close)

    '''
    def __init__(self, event_queue, olhc_data = {}):
        self.event_queue = event_queue
        self.olhc_data = olhc
        self.olhc_symbol = []
        self.latest_data = {}
        pass
    
    
    def next_bar(self):
        pass

    def update(self):
        pass

    @value.setter
    def event_queue(self, queue):
        self.event_queue = queue
    
if __name__ == '__main__':
    pass 