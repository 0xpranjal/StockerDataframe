import requests
from bs4 import BeautifulSoup
import pandas as pd

def monthly_gainers():

    dfs = pd.read_html('https://money.rediff.com/gainers/nse/monthly',header=0)
    for df in dfs[:-1]:
        print(df)

    df['% Change'] = df['% Change'].str.replace(' ', "")
    print(df)
    df.to_csv('monthly_top_gainers.csv', index=False)


def daily_gainers():
    dfs = pd.read_html('https://money.rediff.com/gainers/nse/daily',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)
    df1.to_csv('daily_top_gainers.csv', index=False)


    
def weekly_gainers():    
    dfs = pd.read_html('https://money.rediff.com/gainers/nse/weekly',header=0)
    for df in dfs[:1]:
        print(df)


    df['% Change'] = df['% Change'].str.replace(' ', "")
    print(df)
    df.to_csv('weekly_top_gainers.csv',index=False)


def daily_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/nse/daily',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)  
    df1.to_csv('daily_top_losers.csv', index=False)


def weekly_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/nse/weekly',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)  
    df1.to_csv('weekly_top_losers.csv', index=False)

def monthly_losers():
    dfs = pd.read_html('https://money.rediff.com/losers/nse/monthly',header=0)
    for df in dfs[:-1]:
        print(df)

    df1 = df[['Company', '% Change']]
    print(df1)  
    df.to_csv('monthly_top_losers.csv', index=False)