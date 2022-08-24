from datetime import datetime
from twilio.rest import Client 
import requests
from random import choice
from decouple import config
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY=config('STOCK_API_KEY')
NEWS_API_KEY = config('NEWS_API_KEY')
account_sid = config('account_sid')
auth_token = config('auth_token')
stock_url = "http://api.marketstack.com/v1/eod"
news_url = "https://newsapi.org/v2/everything"
stock_parameters = {
    "access_key": STOCK_API_KEY,
    "symbols": STOCK
}

response = requests.get(url=stock_url, params=stock_parameters)
data = response.json()
last_two_days = data['data'][:2]
yesterday = last_two_days[0]
day_before_yesterday = last_two_days[1]
growth = yesterday['close']-day_before_yesterday['close']
percentage = (growth/yesterday['close'])*100

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "from": day_before_yesterday['date'].split('T')[0],
}

res = requests.get(url=news_url, params=news_parameters)
res_data = res.json()
articles = res_data["articles"][:3]

symbol = ""
if percentage >=0:
    symbol+= "🔺"+str(round(percentage)) +"%"
else:
    symbol+= "🔻"+str(round(percentage*-1)) +"%"
    
def tesla_news():
    for news in articles:
        if 'Tesla'in news['title']:
            return news
       
    return choice(articles)
   
if percentage >=5:
    tesla = tesla_news()
    content = tesla['description']
    client = Client(account_sid, auth_token) 
    message = client.messages.create(   
                                    from_= "+13862309305",  
                                to='+61401915591',
                                body=f"TSLA: {symbol}\nHeadline: {tesla['title']}\nBrief: {content}"
                            ) 
