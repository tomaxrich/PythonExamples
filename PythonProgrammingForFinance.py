import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
'''
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

#parameters are Stock ticker, website data extracted from, start, and end dates
df = web.DataReader('TSLA', 'yahoo', start, end)

#converts stock information to a csv file
df.to_csv('tsla.csv')

print(df.head())
print(df.tail())
'''
df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0)
#print(df.head())

#df['Adj Close'].plot()
df['Open'].plot()
df['Close'].plot()

plt.show()
