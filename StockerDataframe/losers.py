import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def daily_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/bse/daily',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)
    df1.to_csv('daily_top_losers.csv', index=False)


def weekly_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/bse/weekly',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)
    df1.to_csv('weekly_top_losers.csv', index=False)

def monthly_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/bse/monthly',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)
    df1.to_csv('monthly_top_losers.csv', index=False)

def plot_daily_losers():
    plt.style.use('fivethirtyeight')
    data_daily_losers = pd.read_csv('daily_top_losers.csv')
    data_daily_losers_final = data_daily_losers[:16]
    x4 = data_daily_losers_final.plot.bar(x = 'Company', y = '% Change', title = 'Daily Top Losers', color='Black')
    plt.savefig('daily_top_losers.png', bbox_inches='tight')
    plt.show(x4)
    
def plot_weekly_losers():
    plt.style.use('fivethirtyeight')
    data_weekly_losers = pd.read_csv('weekly_top_losers.csv')
    data_weekly_losers_final = data_weekly_losers[:16]
    x5 = data_weekly_losers_final.plot.bar(x = 'Company', y = '% Change', title = 'Weekly Top Losers', color='Black')
    plt.savefig('weekly_top_losers.png', bbox_inches='tight')
    plt.show(x5)

def plot_monthly_losers():
    plt.style.use('fivethirtyeight')
    data_monthly_losers = pd.read_csv('monthly_top_losers.csv')
    data_monthly_losers_final = data_monthly_losers[:16]
    x6 = data_monthly_losers_final.plot.bar(x = 'Company', y = '% Change', title = 'Monthly Top Losers', color='Black')
    plt.savefig('monthly_top_losers.png', bbox_inches='tight')
    plt.show(x6)


