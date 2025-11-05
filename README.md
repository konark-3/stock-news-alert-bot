# Stock Price Alert & News Notifier

This Python project monitors **stock price changes** and automatically fetches the latest news for a company.  
It sends alerts via **WhatsApp (Twilio)** and **Email** when the stock price changes significantly.

---

## Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `requests`, `twilio`, `smtplib`, `email`, `os`  
- **APIs:**  
  - [Alpha Vantage API](https://www.alphavantage.co/) – for stock prices  
  - [NewsAPI](https://newsapi.org/) – for fetching company news  
  - [Twilio API](https://www.twilio.com/) – for WhatsApp notifications  

---

## Features

- Monitors daily stock price changes.  
- Calculates percentage change between yesterday and the day before.  
- Fetches top 3 news articles when stock price changes exceed a threshold (e.g., 2%).  
- Sends alerts via WhatsApp with stock info, headline, and brief.  
- Sends the same news via Email.  

---

## Setup

1. Set environment variables or directly update credentials:

`
EMAIL = "your_email@example.com"
PASSWORD = "your_email_password"
ACCOUNT_SID = "your_twilio_account_sid"
AUTH_TOKEN = "your_twilio_auth_token"`

1.  Install dependencies:

`pip install requests twilio`

1.  Obtain API keys:

    -   Alpha Vantage for stock data

    -   NewsAPI for news articles

    -   Twilio account for WhatsApp notifications

2.  Update stock symbol and company name if needed:

`STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"`

* * * * *

How It Works
------------

1.  Fetch daily stock prices using **Alpha Vantage API**.

2.  Calculate the percentage difference between yesterday and the day before yesterday.

3.  If the change exceeds the threshold (e.g., 2%):

    -   Fetch the top 3 news articles about the company using **NewsAPI**.

    -   Send alerts via **WhatsApp** through Twilio API.

    -   Send the same news via **Email**.

* * * * *

Example Usage
-------------

Run the script:

`python stock_alert_notifier.py`

Sample WhatsApp message:

`TSLA: 🔺2%
Headline: Tesla News Headline
Brief: Tesla news description...`

Sample Email message:

`Subject: 🔺2% TSLA
Headline: Tesla News Headline
Brief: Tesla news description...`

* * * * *

Notes
-----

-   Keep API keys and credentials secure (use environment variables in production).

-   Adjust the percentage threshold for stock alerts if needed.

-   Ensure email provider allows SMTP access (Gmail may require App Passwords).
