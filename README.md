# StockerDataframe
<p  align="center"><img height="300" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/docs/img1.png?token=AMFAV3YUAJJNUNJTCCDQNPS7LAD3S"></p>

A unique tool for better analysis of Stock Market. This library can scrape the web for a lot of stock related data which can help you with detailed analysis of the market.

## Installation
Install with:  
```pip install StockerDataframe```

For [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb):  
```!pip install StockerDataframe```

## Stock Market Analysis
Stock market analysis enables investors to identify the intrinsic worth of a security even before investing in it. All stock market tips are formulated after thorough research by experts. Stock analysts try to find out activity of an instrument/sector/market in future.

By using stock analysis, investors and traders arrive at equity buying and selling decisions. Studying and evaluating past and current data helps investors and traders to gain an edge in the markets to make informed decisions. Fundamental Research and Technical Research are two types of research used to first analyze and then value a security.

## Importance
Performing a research before making an investment is a must. It is only after a thorough research that you can make some assumptions into the value and future performance of an investment. Even if you are following stock trading tips, it ideal to do some research, just to ensure that you are making an investment that’s expected to get you maximum returns.

When you invest in equity, you purchase some portions of a business expecting to make money upon increase in the value of the business. Before buying anything, be it a car or phone, you do some degree of research about its performance and quality. An investment is no different. It is your hard earned money that you are about to invest, so you must have a fair knowledge of what you are investing in.

## What Parameters can help you with the Analysis
One of the key factors for traders is tracking the best and worst performing stocks over a period of time. With StockerDataframe, you can easily 
scrape the web for a lot of stock related data which can help you with detailed analysis of the market.

## Getting Started
### Daily Gainers
To extract the performers of a particular day in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.daily_gainers()
```
OUTPUT:
```
Company	              % Change
Indian Acrylics	+20.00
Pasupati Acrylon	+19.91
Vidli Restaurants Lt	+19.12
Responsive Industrie	+16.60
Victoria Mills	+14.60
HB Portfolio	+14.41
Gensol Engineering	+14.38
Technocraft Industri	+14.28
Radhe Developers	+14.11
Pondy Oxides & C	+11.39
```
### Plotting the Daily top performers
```python
import StockerDataframe

StockerDataframe.plot_daily_gainers()
```
OUTPUT:

<p  align="center"><img height="600" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/daily_top_gainers.png?token=AMFAV3527AXOOU73Y5P6ANS7K7RKO"></p>

### Weekly Gainers
To extract the Top performers of a particular week in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.weekly_gainers()
```
OUTPUT:
```
Company	              % Change
Dhanvarsha Finvest	+36.84
Polyspin Exports	+33.19
Vitesse Agro L	+28.89
Rainbow Foundati	+27.44
Anubhav Infrastructu	+27.38
Real Strips	+27.35
Global Offshore Ser	+27.27
Kellton Tech Solutio	+27.18
Simran Farms Lim	+26.98
```
### Plotting the Weekly top performers
```python
import StockerDataframe

StockerDataframe.plot_weekly_gainers()
```
OUTPUT:
<p  align="center"><img height="600" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/weekly_top_gainers.png?token=AMFAV34JMSWL4BJNXG6A2QK7LAAVW"></p>


### Monthly Gainers
To extract the Top performers of a particular week in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.monthly_gainers()
```
OUTPUT:
```
Company	              % Change
Kaushalya Infrastruc	+173.40
Optiemus Infracom	+162.00
Source Natural Foods	+160.36
Axtel Industries	+142.98
Regency Investments	+137.73
CG Power and Indust	+130.73
Mangalam Drugs	+116.51
Amaze Entertech	+115.63
Tirupati Tyres	+110.75
```
### Plotting the Monthly top performers
```python
import StockerDataframe

StockerDataframe.plot_monthly_gainers()
```
OUTPUT:
<p  align="center"><img height="500" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/monthly_top_gainers.png?token=AMFAV34TL56K2S4Q2BOUGTC7LAAXW"></p>

### Daily Losers
To extract the worst performers of a particular day in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.daily_losers()
```
OUTPUT:
```
Company	              % Change
Benara Bearings	-20.0
Bothra Metals & Allo	-14.0
Dhruv Consultancy	-13.33
Vodafone Idea L	-12.76
Yug Decor	-12.5
Caprihans India	-11.19
La Tim Metal & Ind	-10.0
Future Retail L	-9.98
Odyssey Technolo	-9.95
```
### Plotting the Daily worst performers
```python
import StockerDataframe

StockerDataframe.plot_daily_losers()
```
OUTPUT:
<p  align="center"><img height="500" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/daily_top_losers.png?token=AMFAV3YLRONQXY2SW3XYEM27LABGY"></p>

### Weekly Losers
To extract the worst performers of a particular week in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.weekly_losers()
```
OUTPUT:
```
Company	              % Change
Morganite Crucible (	-52.38
Benara Bearings	-33.13
Somi Conveyor Beltin	-30.64
GlobalSpace Techno	-25.59
Patel Integrated Log	-23.94
Hindustan Aeronautic	-23.91
Dynamic Industri	-23.33
NDR Auto Components	-22.57
Goldstone Tech	-22.44
```
### Plotting the Weekly worst performers
```python
import StockerDataframe

StockerDataframe.plot_weekly_gainers()
```
OUTPUT:
<p  align="center"><img height="500" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/weekly_top_losers.png?token=AMFAV34SEC7JIIWYEK32KMS7LABLS"></p>


### Monthly Losers
To extract the worst performers of a particular week in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.monthly_losers()
```
OUTPUT:
```
Company	              % Change
Eicher Motors	-89.68
Madhav Infra Project	-79.26
Trident Texofab	-63.33
Leading Leasing Fin	-52.62
Netripples Software	-48.68
UTL Industries	-47.12
Morganite Crucible (	-41.91
Caprolactam Chemical	-37.37
Panth Infinity	-35.2
```
### Plotting the Monthly worst performers
```python
import StockerDataframe

StockerDataframe.plot_monthly_losers()
```
OUTPUT:
<p  align="center"><img height="500" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/monthly_top_losers.png?token=AMFAV36TLZUESOBCPZ747VK7LABNI"></p>

