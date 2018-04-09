import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import os
import csv

#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------

# to pull stocklist from csv file on drive:

os.chdir('/Users/durantem/desktop/Stock_Analysis')
#topstocks = pd.read_csv('top-25-stocks.csv')
#stocklist = topstocks['Symbol'].tolist()

        
#Stock data structure from https://pythonprogramming.net/

style.use('ggplot')

#declare starting and ending dates for data pull
start = dt.datetime(2017, 1, 1)
end = dt.datetime.now()

#initialize array of stocks for analysis
stocklist = ["AAPL", "TSLA", "MSFT", "SPX","AMZN","GOOGL","ADSK"]

#create empty dictionary to import morningstar historical data to 
s = {}

#for each stock in stocklist, pull data from morningstar
for symbol in stocklist:
    try:
        s[str(symbol)] = web.DataReader(symbol, 'morningstar', start, end)
        s[str(symbol)].reset_index(inplace=True)
        s[str(symbol)].set_index("Date", inplace=True)
        s[str(symbol)] = s[str(symbol)].drop("Symbol", axis=1)
        continue
    except:
        print('Error reading stock data for ' + str(symbol))
    
    
# add standard deviation, moving average and exponential weighted moving average columns to each stock's dataframe
for df in s:
    df = s[df]
    df['stdev'] = df['Close'].rolling(window=20,min_periods=10).std()
    df['20ma'] = df['Close'].rolling(window=20,min_periods=0).mean()
    df['20ewm'] = df['Close'].ewm(span=20,adjust=True).mean()

#initialize empty array to store key value (stock symbol) of each dataframe for plot titles
plottitles = []
for key in s:
    plottitles.append(key)

benchmark = s['SPX']

    
#create counter at 0 to iterate through keys
i = 0

for df in s: 
    df = s[df]
    df[['Close','20ma','20ewm']].plot()
    plt.title(plottitles[i], fontsize=20)
    plt.tight_layout()
    plt.savefig(str(plottitles[i])+' 2017-To-Date.png', dpi = 300)
    plt.close()
    i += 1
