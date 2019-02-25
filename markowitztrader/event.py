from enum import Enum
from abc import ABC, abstractmethod
import abc

class EventType(Enum):
    MARKET = "MARKET"
    SIGNAL = "SIGNAL"
    ORDER = "ORDER"
    FILL = "FILL"


class BaseEvent(ABC):
    ''' Abstract Event to fill in backtest queue
    '''
    __metaclass__ = abc.ABCMeta
    @abc.abstractproperty
    def type(self):
        pass
        

class MarketEvent(BaseEvent):
    ''' Event representing the market has been updated, 
        i.e new data has arrived.
    '''
    def __init__(self):
        self._type: EventType = EventType.MARKET

    @property
    def type(self):
        return self._type
    

class SignalEvent(BaseEvent):
    def __init__(self):
        self._type: EventType = EventType.Signal
    
    @property
    def type(self):
        return self._type

class OrderEvent(BaseEvent):
    def __init__(self):
        self._type: EventType = EventType.ORDER

    @property
    def type(self):
        return self._type

class FillEvent(BaseEvent):
    def __init__(self):
        self._type: EventType = EventType.FIL
    
    @property
    def type(self):
        return self._type

if __name__ == '__main__':
    print(EventType.MARKET)
    event: BaseEvent = MarketEvent()
    print(event.type)