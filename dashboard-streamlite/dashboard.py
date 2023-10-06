import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark') 

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")
 

def create_weathersit_df(df):
    weathersit_df =  day_df.groupby(by="weathersit").agg({
    "cnt": "sum"
})
    weathersit_df = weathersit_df.reset_index()
    weathersit_df.rename(columns={
        "cnt": "total",
    }, inplace=True)
    
    return weathersit_df

def create_holiday_df(df):
    holiday_df = day_df.groupby(by="holiday").agg({
        "cnt": "mean",
    }, inplace=True)

    return holiday_df

def create_weekday_df(df):
    weekday_df = day_df.groupby(by="weekday").agg({
        "cnt": "mean",
    }, inplace=True)

    return weekday_df

def create_hours_df(df):
    hours_df = hour_df.groupby(by="hr").agg({
    "cnt":"mean"

    }, inplace=True)

    return hours_df


with st.sidebar:
    st.title('Bike Sharing')
    st.image("image/logo.png")
    st.text('informasi Bike Sharing')


st.title('visualisasi data :sparkles:')


st.title('Visualisasi rata rata peminjam sepeda')

col1, col2 = st.columns(2)
 
with col1:
    holiday_pd = create_holiday_df(day_df)

    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(
        y="cnt", 
        x="holiday",
        data=holiday_pd,
        ax=ax
    )
    
    

    ax.set_title("rata rata penyewa berdasarkan hari libur", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

    wet_pd = create_weathersit_df(day_df)
    

with col2:
    weekday_pd = create_weekday_df(day_df)
    sns.barplot(
        y="cnt", 
        x="weekday",
        data=weekday_pd,
        ax=ax
    )

    ax.set_title("rata rata penyewa berdasarkan hari", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)


st.subheader("rata rata peminjam berdasarkan jam")

hours_df = create_hours_df(hour_df)


fig, ax2 = plt.subplots(figsize=(16, 8))
ax2.plot(
    hours_df["cnt"],
    marker='o', 
    linewidth=5,
    color="#90CAF9"
)
ax2.set_ylabel("rata rata sewa")
ax2.set_xlabel("jam")
ax2.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

