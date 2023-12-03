import re
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import lib.data_processing.data_utils as data

def import_from_csv(data_set_name):
    data.sets[data_set_name] = pd.read_csv(data.source[data_set_name])
    return data.sets[data_set_name]

def combine_outcomes_variables(outcome_data, variables_data):
    data.outcomes_count = outcome_data.shape[1]
    return pd.merge(outcome_data, variables_data, on='date', how='inner')

def average_over_days(values, period_to_average):
    df = values.copy()
    df = values.rolling(window=period_to_average).mean()
    df = df.dropna()
    data.averaged_periods = period_to_average
    return df

def normalise_values(values):
    df = values.copy()
    df = pd.DataFrame(
        MinMaxScaler().fit_transform(values),
        columns=values.columns,
        index=df.index
    )
    return df

def average_rows_by_day(df, column_to_average):
    df = df.copy()
    df = df.groupby(['date', column_to_average]).mean()
    return df

# TO DO: average rows by part of day: all, morning, afternoon, evening, night
# def average_rows_by_intervals(df, column_to_average):

def pivot_table_on_day(df, columns_to_pivot):
    df = df.copy()
    df = df.pivot_table(index='date', columns=columns_to_pivot, values='value', aggfunc='sum', fill_value=0)
    return df

# To do: Should this be here/data utils?
def prepare_nutrition_data():
    df = import_from_csv('nutrition')
    df = df.rename(columns={'Date': 'date'})
    df = df.rename(columns={'Energy (kcal)': 'Calories'})
    df = df.drop(columns=['Carbs (g)'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    # To do: should this be in data_processing?
    df.columns = [re.sub(r'\(.*\)', '', col).strip() for col in df.columns]
    data.sets['nutrition'] = df
