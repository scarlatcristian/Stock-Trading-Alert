# Stock-Trading-Alert

This Python script tracks the stock price of a specified company and sends notifications if there is a significant change in the stock price or if there are relevant news articles about the company.

## Setup

1. Install required packages using pip:


2. Obtain API keys

   - **Stock API Key**: Obtain an API key from [Alpha Vantage](https://www.alphavantage.co/) by signing up for an account. Set the obtained API key as an environment variable named `STOCK_API_KEY`.
   - **News API Key**: Obtain an API key from [News API](https://newsapi.org/) by signing up for an account. Set the obtained API key as an environment variable named `NEWS_API_KEY`.
   - **Twilio Account SID and Auth Token**: Sign up for a Twilio account at [Twilio](https://www.twilio.com/). Obtain the Account SID and Auth Token from the Twilio dashboard. Set these values as environment variables named `TWILIO_SID` and `TWILIO_TOKEN` respectively.
   - **Twilio Phone Number and Recipient Phone Number**: Set your Twilio phone number (from which messages will be sent) and the recipient phone number (where messages will be sent) as environment variables named `PHONE_NUMBER` and `RECIPIENT_NUMBER` respectively.

## Usage

Run the script `main.py` using Python:


The script will fetch the stock price data and news articles, and send notifications via SMS using Twilio if the stock price change exceeds 5%.

## Dependencies

- `requests`: Used for making HTTP requests to the Alpha Vantage and News API.
- `twilio`: Used for sending SMS notifications.

## Environment Variables

- `STOCK_API_KEY`: API key for Alpha Vantage.
- `NEWS_API_KEY`: API key for News API.
- `TWILIO_SID`: Twilio Account SID.
- `TWILIO_TOKEN`: Twilio Auth Token.
- `PHONE_NUMBER`: Twilio phone number.
- `RECIPIENT_NUMBER`: Recipient phone number.
