from pandas.io.formats.format import Datetime64TZFormatter
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import os

st.title('Open-Powerlifitng Data')

#DATA_PATH = '/Users/pjheddrich/Downloads/openipf-2022-01-09/openipf-2022-01-09-3336416a.csv'

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

"""
DATA_PATH = os.path.join(__location__, 'openipf-2022-01-09/openipf-2022-01-09-3336416a.csv')

@st.cache
def load_data(nrows=None) -> pd.DataFrame:
    if nrows:
        data = pd.read_csv(DATA_PATH, nrows=nrows)
    else:
        data = pd.read_csv(DATA_PATH)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def plot_data(dataFrame,title="",Xtitle="",Ytitle=""):
    
    chart = alt.Chart(dataFrame).mark_line().encode(
        alt.X('year',title=Xtitle),
        alt.Y('TotalKg:Q',title=Ytitle),
        alt.Color('WeightClassKg:N')).properties(title=title)
    
    return st.altair_chart(chart, use_container_width=True)

def filter_data(df) -> pd.DataFrame:
    df = df[(df['Equipment'] == 'Raw') & (df['Event'] == 'SBD')]
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df['YearOfBirth'] = (df['year'] - np.floor(df['Age'])).fillna(0).astype(np.int64)

    return df

def get_max_mean_count(df,weightClasses) -> tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    df_max = pd.DataFrame(df[df['Sex']=='M'].groupby(['WeightClassKg','year'])['TotalKg'].max()).reset_index()
    df_mean = pd.DataFrame(df[df['Sex']=='M'].groupby(['WeightClassKg','year'])['TotalKg'].mean()).reset_index()
    df_count = pd.DataFrame(df[df['Sex']=='M'].groupby(['WeightClassKg','year'])['TotalKg'].count()).reset_index()

    df_max_cleaned = df_max[df_max['WeightClassKg'].isin(weightClasses)]
    df_mean_cleaned = df_mean[df_mean['WeightClassKg'].isin(weightClasses)]
    df_count_cleaned = df_count[df_count['WeightClassKg'].isin(weightClasses)]

    return df_max_cleaned,df_mean_cleaned,df_count_cleaned

df = load_data()

df = filter_data(df)

male_wc = ['59','66','74','83','93','105','120','120+']

df_max_cleaned,df_mean_cleaned,df_count_cleaned = get_max_mean_count(df,male_wc)
"""

df_max_cleaned = pd.read_csv(os.path.join(__location__, 'df_max_cleaned.csv'))
df_mean_cleaned = pd.read_csv(os.path.join(__location__, 'df_mean_cleaned.csv'))
df_count_cleaned = pd.read_csv(os.path.join(__location__, 'df_count_cleaned.csv')

p1 = plot_data(df_max_cleaned,"Growth mens highest total over the years","year","TotalKg")
p2 = plot_data(df_mean_cleaned,"Growth mens mean total over the years","year","TotalKg")
p3 = plot_data(df_count_cleaned,"Growth mens participation in comp over the years","year","NumberOfTotals")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)