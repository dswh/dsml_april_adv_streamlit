import datetime
import pandas as pd
import streamlit as st
import yfinance as yf


st.write(
    """
    # Stock Price Analyser
    
    Shown are the stock prices of Apple Company
    """
)

ticker_symbol = st.text_input(
                                "Enter Stock Symbol",
                                "AAPL",
                                key="placeholder"
)

col1, col2 = st.columns(2)

## start date
with col1:
    start_date = st.date_input("Input the starting date", 
                                datetime.date(2019,1,1))

## end date
with col2:
    end_date = st.date_input("Input the ending date", 
                                datetime.date(2022,12,31))                            

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",
                                start= f"{start_date}",
                                end=f"{end_date}")


st.write(f"""
    ### {ticker_symbol}'s stock price info:
""")

st.dataframe(ticker_df)

## showcassing line charts

col1, col2 = st.columns(2)

with col1:
   st.header("Daily Closing Prices")
   st.line_chart(ticker_df.Close)

with col2:
   st.header("Daily Volume:")
   st.line_chart(ticker_df.Volume)




