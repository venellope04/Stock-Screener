import datetime as dt
import pandas as pd
import yfinance as yf
from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QWidget

start =dt.datetime(2020,12,1)
now=dt.datetime.now()

class StockScreenerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stock Screener")
        self.setGeometry(100,100,800,600)

        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)

        layout=QVBoxLayout()

        self.table=QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['Stock', '150 Day MA', '200 Day MA', '52 Week Low', '52 Week High'])
        layout.addWidget(self.table)

        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.run_stock_screener)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.refresh_button)

        central_widget.setLayout(layout)

    def run_stock_screener(self):
        symbol_list=["RELIANCE.NS","ADANIGREEN.NS","MSFT","INFY.NS","AAPL","GOOGL"]
        exportList=[]
        
        for stock in symbol_list:
            try:
                df=yf.download(stock, start=start, end=now)

                df['SMA_50']=df['Adj Close'].rolling(window=50).mean()
                df['SMA_150']=df['Adj Close'].rolling(window=150).mean()
                df['SMA_200'] = df['Adj Close'].rolling(window=200).mean()

                currentClose = df["Adj Close"].iloc[-1]
                moving_average_50 = df["SMA_50"].iloc[-1]
                moving_average_150 = df["SMA_150"].iloc[-1]
                moving_average_200 = df["SMA_200"].iloc[-1]
                low_of_52week = df["Adj Close"].iloc[-260:].min()
                high_of_52week = df["Adj Close"].iloc[-260:].max()

                exportList.append({"stock":stock ,"50 Day MA":moving_average_50,
                                   "150 Day Ma": moving_average_150, "200 Day MA": moving_average_200,
                                   "52 Week Low": low_of_52week, "52 Week High": high_of_52week })
            except Exception as e:
                print(f"Error fetching data for {stock}: {e}")

        self.display_result(exportList)

    def display_result(self, result__list):
        self.table.setRowCount(0)
        for i, data in enumerate(result__list):
            self.table.insertRow(i)
            for j, value in enumerate(data.values()):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

if __name__=='__main__':
    app=QApplication([])
    main_window=StockScreenerApp()
    main_window.show()
    app.exec_()



            


