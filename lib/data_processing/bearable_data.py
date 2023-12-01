import pandas as pd
import lib.utils.input_handler as ask
import lib.data_processing.data as data

# Load data, cleans, format and pass to data.py
df = data.source['bearable']
df['date'] = df['date formatted']
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Only use relevant rows and columns, clean headers
df = df[['category', 'rating/amount']].copy()
df.rename(columns={'rating/amount': 'value'}, inplace=True)
df['category'] = df['category'].replace('Sleep', 'sleeptime')
df['category'] = df['category'].replace('Sleep factors', 'sleepfactors')
df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
data.sets['bearable'] = df

def filter_outcomes(selection):
    df = data.sets['bearable'].copy()
    df = df[df['category'].isin(selection)]
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.groupby(['date', 'category']).mean()
    df = df.pivot_table(index='date', columns='category', values='value', aggfunc='sum', fill_value=0)
    return df
