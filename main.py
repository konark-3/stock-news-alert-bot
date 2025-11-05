import requests
from twilio.rest import Client
import os
import smtplib
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
api_key = os.environ.get("API_KEY")



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


response1 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=iu")
data1 = response1.json()


response2 = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-06-23&sortBy=publishedAt&apiKey=767X")
data2 = response2.json()

close_price_yesterday = float(data1["Time Series (Daily)"]['2024-07-17']['4. close'])
close_price_day_before = float(data1["Time Series (Daily)"]['2024-07-15']['4. close'])

diff = abs(close_price_yesterday - close_price_day_before)
percent = (diff/close_price_day_before)*100

if percent > 2:
    client = Client(account_sid, auth_token)
    for num in range(0, 3):
        title = data2['articles'][num]['title']
        descrip = data2['articles'][num]['description']

        message = client.messages.create(
            from_='whatsapp:+1676',
            body=f'{STOCK} 🔺2%\n\nHeadline: {title}\n\nBrief: {descrip}',
            to='whatsapp:+11234'
        )
        print(message.sid)

        email_message = EmailMessage()
        email_message['Subject'] = f"🔺2%{STOCK}"
        email_message['From'] = EMAIL
        email_message['To'] = "xyz@yahoo.com"
        email_message.set_content(f"Headline: {title}\n\nBrief: {descrip}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.send_message(email_message)


print(f"Percent difference -> {percent}")
print(f"Close price yesterday -> {close_price_yesterday}")
print(f"Close price day before yesterday-> {close_price_day_before}")





