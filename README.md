# StockerDataframe
<p  align="center"><img height="300" src = "https://github.com/Bhard27/StockerDataframe/blob/master/docs/img1.png"></p>
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
To extract the Top performers of a particular day in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.daily_gainers()
```
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
Radhika Jeweltech	+11.29
Alufluoride Ltd.	+11.19
IIFL Finance	+10.43
Chembond Chemica	+10.12
```

<p  align="center"><img height="600" src = "https://raw.githubusercontent.com/Bhard27/StockerDataframe/master/examples/daily_top_gainers.png?token=AMFAV3527AXOOU73Y5P6ANS7K7RKO"></p>

### Weekly Gainers
To extract the Top performers of a particular week in BSE and save them locally in a CSV file format. We can get the % change and Company name in the CSV file which can be used for further advanced Data Analysis.

```python
import StockerDataframe

StockerDataframe.weekly_gainers()
```
