import requests
import datetime
import smtplib

MY_EMAIL= "youremailID"
MY_PASSWORD= "password"

ACCESS_KEY= "apikey"
COMPANY_NAME="Tesla"
STOCK_SYM= "TSLA"

NEWS_API= "newsapikey"

parameters={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYM,
    "outputsize":"compact",
    "apikey": ACCESS_KEY
}

response= requests.get(url="https://www.alphavantage.co/query",params=parameters)
webpage= response.json()


date= datetime.datetime.now().date()
print(date)

yesterday = date - datetime.timedelta(days = 1)
day_before_yes= str(yesterday- datetime.timedelta(days=1))
yesterday=str(yesterday)

print(webpage['Time Series (Daily)'][str(yesterday)]['4. close'])
print(webpage['Time Series (Daily)'][str(day_before_yes)]['4. close'])


# For percentage rise

yes_close_price= float(webpage['Time Series (Daily)'][str(yesterday)]['4. close'])
day_before_close_price= float(webpage['Time Series (Daily)'][str(day_before_yes)]['4. close'])

price_diff= yes_close_price-day_before_close_price


if(price_diff>0):
    dir="up"
else:
    dir= "down"

percent_diff= (abs(price_diff)/yes_close_price)*100
print(percent_diff)


if(percent_diff>=1):
    par= {
        "q":COMPANY_NAME,
        "from":yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_API,
        "language":"en"

    }

    news= requests.get(url="https://newsapi.org/v2/everything", params=par)

    newsWebpage= news.json()

    first_3_news= newsWebpage['articles'][:3]

    headlines=[]
    description=[]

    for x in first_3_news:
        headlines.append(x['title'])
        description.append(x['description'])
    
    for i in range(3):
        msg= headlines[i]+" : "+description[i]
        print(msg)
        msg.encode("ascii", errors="ignore")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            msg= msg.replace('\u2026',' ')
            msg= msg.replace('\u2019',' ')
            msg= msg.replace('\u2013',' ')
            msg= msg.replace('\xef',' ')
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Tesla Stocks went "+dir+ "!!\n\n"+"Recent news related to Tesla\n"+msg)
            




