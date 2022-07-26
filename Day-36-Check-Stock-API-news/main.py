import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY ="BOEOEQ49CN5ICFQ2"
NEWS_API_KEY = "bc16af46d8a64f53b4d3b39af3d6353a"
account_sid = ""
auth_token = ""
Twilio_phone = ""
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decrease by 5% between yesterday and the day before yesterday then

#TODO 1. - Get yesterday is closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 =-20, but the positive difference is 20.
# Hint: https://www.w3schools/python/ref_func_abs.asp
difference = round(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference < 0:
    up_down = "🔻"

else:
    up_down = "✅"

print(difference)

#TODO 4. - Work out the percentage diffrence in price between closing price yesterday  and closing the day before yesterday .
diff_percent = (difference/float(yesterday_closing_price))*100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News")
if abs(diff_percent) > 0:
    print("Get News")

    news_prams = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get("https://newsapi.org/v2/everything", params=news_prams)
    response.raise_for_status()



## STEP 2: Insted of printing ("Get News"), actually get the first 3 news pieces for the Company

    #TODO 6. - Use python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211
    data_news_slice_3_articles = response.json()["articles"][0:3]

## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone

    #TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension

    formatted_articles = [f"{STOCK_NAME}: {up_down}{difference}%\nHeadline: {article['title']}." \
                          f"\nBrief: {article['description']}"
                          for article in data_news_slice_3_articles]



    #TODO 8. - Send each article as a seperate message via Twilio.


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=Twilio_phone,
            to='+84389675880'
        )
        print(message.status)

