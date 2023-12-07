import pandas as pd
import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

# Load data, cleans, format and pass to data.py
df = data_process.import_from_csv('bearable')
df['date'] = df['date formatted']
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# only use category and rating/amount columns
df = df[['category', 'rating/amount']].copy()

# Exclude notes and water
df = df[~df['category'].isin(['Extra notes', 'Water'])]

# Pause all this
#################################
# Add wake up factor
# df.loc[df['category'].str.contains('Wake-up', case=False, na=False), 'category'] = 'Wake-up'

# trim headers for slicing later
# df['category'] = df['category'].replace('Sleep', 'sleeptime')
# df['category'] = df['category'].replace('Sleep factors', 'sleepfactors')

# Split Nutrition factors into lists
# To do: split into rows (explode)
# df['detail'] = df['detail'].str.replace('. Snacks:', ' |')
# df['detail'] = df['detail'].replace({'Meals: ': '', 'Snacks: ': ''}, regex=True)
# df['detail'] = df['detail'].str.split(' \| ')

# print('BEARABLE DATA')
# input(df.head())
# input(df['category'].unique())
#################################


# rename ratings to value
df.rename(columns={'rating/amount': 'value'}, inplace=True)

df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
data.sets['bearable'] = df

# Only applies to bearable outcomes data - otherwise move to data_processing.py
def filter_outcomes(user_seleced_outcomes):
    df = data.sets['bearable'].copy()
    df = df[df['category'].isin(user_seleced_outcomes)]
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # TO DO: This should be optional/temporary until we can get the data in a better format
    df = data_process.average_rows_by_day(df, 'category')
    ###################################################
    df = data_process.pivot_table_on_day(df, 'category')
    return df
