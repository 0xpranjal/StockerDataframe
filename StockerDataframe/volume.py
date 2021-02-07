import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from GoogleNews import GoogleNews

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

def Google_news():

    news = GoogleNews(period='7d')
    file = open("tracker_data.txt", 'w')
    
    def main():
        procced = 'y'
        while procced == 'y':
            menu()
            choice = selection()
            search_to_file(choice)
            procced = str(input("Enter 'y' to make another menu selection, enter anything else if finished: "))
    
    def menu():
        print("[Selection Menu]")
        print("(1) Find News\n"
              "(2) Exit program\n")
    
    def selection():
        choice = int(input("Enter number corresponding to choice: "))
        while not (choice == 1 or choice == 2):
            choice = int(input("Invalid input, Enter number corresponding to the choices: "))
            
        if choice == 1:
            ticker = str(input("Enter ticker symbol or company name to find news: "))
    
        elif choice == 2:
            print("Exiting program...")
            exit()
                
        return ticker
    
    def search_to_file(ticker):
        news.search(ticker)
        #news.getpage(1)#starts on page two, if u call this it will give duplicate values
        news.getpage(2)
        news.getpage(3)# carfull this method creates duplicate links
        links = news.result()
        for link in links:
            if link["title"] == '':
                None
            else:
                writing = str(link["title"])+": "+str(link["link"])+" "+str(link["date"])+"\n" + "\n"
                file.write(writing)
                print(link["title"]+"\n",link["link"]+"\n",link["date"])
        file.close()
        
    main()