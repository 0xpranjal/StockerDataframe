import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def most_traded():

    dfs = pd.read_html('https://money.rediff.com/companies/most-traded',header=0)
    for df in dfs[:-1]:
        return df

    df['% Change'] = df['% Change'].str.replace(' ', "")
    df1 = df[['Company', '% Change', 'Current Price (Rs)', 'Volume']]
    return df1
    df1.to_csv('mosttraded.csv', index=False)
    
    
def plot_most_traded():

    most_traded()
    plt.style.use('fivethirtyeight')
    data_daily_gainers = pd.read_csv('mosttraded.csv')
    data_daily_gainers_final = data_daily_gainers[:15]
    x1 = data_daily_gainers_final.plot.bar(x = 'Company', y = 'Volume', title = 'Top Traded', color='Black')
    plt.savefig('mosttraded.png', bbox_inches='tight')
    plt.show(x1)
