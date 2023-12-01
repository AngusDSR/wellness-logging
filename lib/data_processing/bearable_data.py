import pandas as pd
import lib.utils.input_handler as ask
import lib.data_processing.data as data

df = data.source['bearable']
df['date'] = df['date formatted']
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Only use relevant rows and columns, clean headers
df = df[['category', 'rating/amount']]
df.rename(columns={'rating/amount': 'value'}, inplace=True)
df['category'] = df['category'].replace('Sleep', 'sleeptime')
df['category'] = df['category'].replace('Sleep factors', 'sleepfactors')
df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
data.sets['bearable'] = df

def pausedfornow():
    # select outcomes to include
    selection = ask.about_outcomes()
    df = df[df['category'].isin(selection)]

    # Convert values to numeric, group by date and category, pivot table
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.groupby(['date', 'category']).mean()
    df = df.pivot_table(index='date', columns='category', values='value', aggfunc='sum', fill_value=0)
