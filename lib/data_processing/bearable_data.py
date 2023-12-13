import pandas as pd
import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

def filter_outcomes(user_seleced_outcomes):
    df = data.sets['bearable'].copy()
    df = df[df['category'].isin(user_seleced_outcomes)]
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = data_process.average_rows_by_day(df, 'category')
    df = data_process.pivot_table_on_day(df, 'category')
    return df

def simple_import():
    df = data_process.import_from_csv('bearable')
    df['date'] = df['date formatted']
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['category', 'rating/amount']].copy()
    df = df[~df['category'].isin(['Extra notes', 'Water'])]
    df.rename(columns={'rating/amount': 'value'}, inplace=True)
    df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
    data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
    data.sets['bearable'] = df

def better_import():
    df = data_process.import_from_csv('bearable')
    df = df.drop(columns=['date'], errors='ignore')
    df.rename(columns={'rating/amount': 'value', 'date formatted': 'date'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[~df['category'].isin(['Extra notes', 'Water'])]
    # Convert sleep to hours
    df = df[~((df['category'] == 'Sleep') & (df['value'].isnull()))]
    df.loc[df['category'] == 'Sleep', 'value'] = df.loc[df['category'] == 'Sleep', 'value'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)

    # Turn foods into rows
    df['detail'] = df['detail'].str.replace('. Snacks:', ' |')
    df['detail'] = df['detail'].replace({'Meals: ': '', 'Snacks: ': ''}, regex=True)
    df['detail'] = df['detail'].str.split(' \| ')
    df = df.explode('detail')
    df.loc[df['category'] == 'Nutrition', 'value'] = 1
    # to do: rename 'Nutrition' to 'Food'
    df.loc[df['category'] == 'Nutrition', 'category'] = 'Food'


    # for rows where category is 'Sleep' convert the HH:MM string to a number of hours

    # for rows where category is 'Sleep' convert the string to an integer


    #################################
    # remove rows where category is 'Sleep' and value is NaN
    input(df[df['value'].isnull()]['category'].unique())
    input(df[df['category'] == 'Food'])
    input(df[df['category'] == 'Sleep']['value'].unique())


    #################################
    # To do: Make graditudes a count of the number of gratitudes
    # input(df[df['category'] == 'Gratitudes'])
    # To do: make values numeric
    # df['value'] = pd.to_numeric(df['value'], errors='coerce')
    #################################
    # Add wake up factor
    df.loc[df['category'].str.contains('Wake-up', case=False, na=False), 'category'] = 'Wake-up'
    input(df.columns)
    # trim headers for slicing later
    # df['category'] = df['category'].replace('Sleep', 'sleeptime')
    # df['category'] = df['category'].replace('Sleep factors', 'sleepfactors')



    # print('BEARABLE DATA')
    # input(df.head())
    # input(df['category'].unique())
    #################################
    df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
    data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
    data.sets['bearable'] = df
