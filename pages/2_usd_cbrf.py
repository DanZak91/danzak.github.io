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


def dynamics_USD_CBRF():
    date_1 = datetime(1998, 1, 1)
    date_2 = datetime(2023, 1, 1)

    BASE = {'dates': [], 'values': []}

    id_code = 'R01235'
    dynamic_rates = DynamicCurrenciesRates(date_1, date_2, id_code)
    for i in range(1998, 2023):
        for j in range(1, 13):
            try:
                dates = dynamic_rates.get_by_date(datetime(i, j, 1)).date
                values = float(dynamic_rates.get_by_date(datetime(i, j, 1)).value)
                BASE['dates'].append(dates)
                BASE['values'].append(values)
            except AttributeError:
                pass

    df = pd.DataFrame(BASE)
    col1, col3 = st.columns(2)
    with col1:
        st.line_chart(BASE, x='dates', y='values', height=700, width=650, use_container_width=False)
    # with col2:
    #     pass
    with col3:
        st.dataframe(df, height=700, width=600, use_container_width=False)


if __name__ == '__main__':
    st.set_page_config(
        page_title="Dynamics USD_CBRF",
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

    dynamics_USD_CBRF()
