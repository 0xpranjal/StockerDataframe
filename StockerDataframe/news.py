#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:04:45 2021

@author: pranjal27bhardwaj
"""


import requests
from bs4 import BeautifulSoup
from csv import writer
from GoogleNews import GoogleNews

 
       
    
    
def stock_news_headlines():
        response = requests.get('https://pulse.zerodha.com/')
        # print(response)
        soup = BeautifulSoup(response.text,'html.parser')
        companys = soup.find_all(class_='box item') 
        
        with open('news.csv', 'w', encoding="utf-8") as csv_file:
            csv_writer = writer(csv_file)
            headers = ['Title', 'News', 'Link', 'FeedType']
            csv_writer.writerow(headers)
        
            for company in companys:
                title = company.find(class_='title').get_text().split('\n')
                link = company.find('a')['href']
                desc = company.find(class_='desc').get_text()
                Feedtype = company.find(class_='feed').get_text()
                csv_writer.writerow([title, desc, link, Feedtype])
                print(title)
                print(link)
                print(desc)
                print(Feedtype + '\n')
                
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
            print("Selection Menu")
            print("Enter 1 to Find News\n"
                  "Enter 2 to Exit program\n")
        
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
        
print("Select either of the two options")
print("Enter 1 to find financial news\n")
print("Enter 2 to search for a type of news\n")
choice = int(input())
        
if choice == 1:
    stock_news_headlines()
else:
    Google_news()    
        