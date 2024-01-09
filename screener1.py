from pandas_datareader import data as pdr
import pandas as pd 
import yfinance as yf
import datetime as dt 
from tkinter import Tk 
from Tkinter.filedialog import askopenfilename

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
