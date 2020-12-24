import pandas as pd
import pandas_datareader as dr
from datetime import datetime, timedelta

class financeData:
    """
      -------------
      input:
        keyword
        start_date
      -------------
      output:
         Difference in the stock price over the time
      -------------

    """
    def getYahooData(self, keyword, start_date):
        end_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        #print(start_date)
        #print(end_date)
        df = dr.data.get_data_yahoo(keyword, start= start_date, end=end_date)

        #return df.head()
        #df = df.rename(columns = {'Adj Close':'Close'})
        #print(df)
        for i in list(df):
            close_prices = df['Close'].values.tolist()

        a = close_prices[-1] #price of stock today
        b = close_prices[0] # Price of stock on the day user wants to know
        #print(a)
        #print(b)
        diff = close_prices[-1] - close_prices[0]
        print(diff)
        #print(df)
        #historical_data = yahoo.get_historical(start_date, end_date)
        #return historical_data
        #getYahooData('', 'tsla', '2020-03-18')
