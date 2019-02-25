import requests
import numpy as np
import pickle
import bs4 as soup
import matplotlib as plt
import fix_yahoo_finance as yf
import pandas as pd 
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr
import json

yf.pdr_override()

def get_daily_olhc(symbols=[]):
    pass

