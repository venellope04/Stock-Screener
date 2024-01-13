import datetime as dt
import pandas as pd
import yfinance as yf
from PyQt5.Qtwidgets import QApplication,QMainWindow,QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QWidget

start =dt.datetime(2017,12,1)
now=dt.datetime.now()

class StockScreenerApp1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stock Screener")
        self.setGeometry(100,100,800,600)

        central_widget=QWidget(self)
        


