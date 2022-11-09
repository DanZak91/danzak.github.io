import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from cbrf.models import DynamicCurrenciesRates
from datetime import date, datetime
import time
import altair as alt
from vega_datasets import data
import numpy as np
import codecs


def dynamics_stocks():
    trickerSymbol = 'GOOGL'
    trickerData = yf.Ticker(trickerSymbol)
    trickerDF = trickerData.history(period='1m', start='2010-5-31', end='2020-5-31')
    st.line_chart(trickerDF.Close)
    st.line_chart(trickerDF.Volume)


if __name__ == '__main__':
    st.set_page_config(
        page_title="Dynamics Stocks",
        page_icon="🥰",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    hide_menu_style = """
            <style>
            .css-79elbk  {display: none;}
            .css-1ck8f3p {visibility: hidden;}
            .css-hzzzp9  {display: none;}
            .css-1tipzh0  {display: none;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    dynamics_stocks()
