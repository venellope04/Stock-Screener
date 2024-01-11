from pandas_datareader import data as pdr
import pandas as pd 
import yfinance as yf
import datetime as dt 
from tkinter import Tk 
from Tkinter.filedialog import askopenfilename
import os
from pandas import ExcelWriter

yf.pdr_override()
start =dt.datetime(2018,12,1)
now=dt.datetime.now()

root= Tk()
ftypes=[(".xlsm",".xlsx","xls")]
ttl="Title"
dir1='c:\\'
filePath=

stocklist=pd.read_excel(filePath)
stocklist=stocklist.head()

exportList=pd.DataFrame(colums=['stock',"RS_rating","50 Day MA","200 day Ma","52 week high"])

for i in stocklist.index:
    stock=str(stocklist["symbol"][i])
    RS_rating=stocklist["RS Rating"[i]]

    try:
        df = pdr.get_data_yahoo(stock, start, now)

        smaUSed= [50,150,200]
        for x in smaUSed:
            df["SMA_"+str(sma)]=round(df.iloc[:,4].rolling(window=sma).mean(),2)

            currentClose=df["Adj Close"][-1]
            moving_average_50=df["SMA_50"][-1]
            moving_average_150=df["SMA_150"][-1]
            moving_average_150=df["SMA_150"][-1]
            moving_average_200=df["SMA_200"][-1]
            low_of_52week=min(df["Adj Close"][-260:])
            high_of_52week=max(df["Adj Close"][-260:])

            try:
                moving_average_200_20=df["SMA_200"][-20]

            except Exception:
                moving_average_200_20=0
                

    except Exception:

