import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Futurs Petroli Brent - Gràfic d'Espelmes")
st.markdown("Dades diàries OHLC (obertura, màxim, mínim i tancament) dels futurs del petroli Brent.")

# Càrrega de dades
@st.cache_data
def load_data():
    df = pd.read_csv("data/Brent Oil Futures Historical Data.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df = df.rename(columns={"Price": "Close"})
    df = df.sort_values("Date")
    return df

df = load_data()

# Filtres de la barra lateral
st.sidebar.header("Filtres")
min_date, max_date = df["Date"].min(), df["Date"].max()
date_range = st.sidebar.date_input(
    "Rang de dates",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

# Filtrat per dates
if len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
    mask = (df["Date"] >= start) & (df["Date"] <= end)
    filtered = df[mask].copy()
else:
    filtered = df.copy()

# Construcció del gràfic
fig = go.Figure(
    go.Candlestick(
        x=filtered["Date"],
        open=filtered["Open"],
        high=filtered["High"],
        low=filtered["Low"],
        close=filtered["Close"],
        name="OHLC",
        increasing_line_color="#26a69a",
        decreasing_line_color="#ef5350",
    )
)

fig.update_layout(
    title="Futurs Petroli Brent – OHLC Diari",
    xaxis_rangeslider_visible=False,
    yaxis_title="Preu (USD)",
    template="plotly_dark",
    height=600,
    margin=dict(l=50, r=50, t=80, b=50),
)

st.plotly_chart(fig, use_container_width=True)
