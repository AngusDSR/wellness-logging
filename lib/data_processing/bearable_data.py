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

def determine_value(detail, current_value):
    if pd.isnull(current_value) or current_value == '' or pd.isna(current_value):
        for item in detail:
            if '(low)' in item or '(None)' in item or 'Poor' in item or '< 2' in item or '0-3' in item or '< 1 l' in item or 'Negative net' in item:
                return 0
            elif 'medium' in item or 'Moderate' in item or '(Little)' in item or 'Ok' in item or '4-6' in item or '1-2 l' in item or 'Low net' in item:
                return 2
            elif 'High' in item or 'high' in item or '(A lot)' in item or 'Good' in item or '> 6' in item or '7+' in item or '2-3 l' in item or 'High net' in item:
                return 3
            else:
                return 1
    return current_value

def simple_import():
    df = data_process.import_from_csv('bearable')
    df['date'] = df['date formatted']
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['category', 'rating/amount']].copy()
    df.rename(columns={'rating/amount': 'value'}, inplace=True)
    df['category'] = df['category'].apply(lambda value: value.split()[0].strip())
    data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
    data.sets['bearable'] = df

def better_import():
    df = data_process.import_from_csv('bearable')
    # Remove unwanted cols and rows, set index
    df = df.drop(columns=['date', 'notes'], errors='ignore')
    df.rename(columns={'date formatted': 'date', 'time of day': 'period', 'rating/amount': 'value'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Remove unwanted rows
    df = df[~df['category'].isin(['Extra notes', 'Gratitudes', 'Water'])]
    df = df[~((df['category'] == 'Sleep') & (df['value'].isnull()))]

    # Set period into groups
    input(df['period'].unique())
    df['period'] = df['period'].apply(data.get_time_period)
    input(df['period'].dtypes.unique())

    # Clean categories
    df.loc[df['category'] == 'Nutrition', 'category'] = 'Foods'
    df.loc[df['category'] == 'Meds/Supplements', 'category'] = 'Intakes'
    df.loc[df['category'] == 'Health measurements', 'category'] = 'Health'
    df.loc[df['category'] == 'Other Factors', 'category'] = 'Main factors'
    df.loc[df['category'].str.contains('Wake-up', case=False, na=False), 'category'] = 'Wake-up'
    df.loc[df['category'].str.contains('Snoring', case=False, na=False), 'category'] = 'Snoring'
    df['category'] = df['category'].str.replace('[^a-zA-Z0-9- ]', '', regex=True)
    df['category'] = df['category'].str.strip()

    # Split factors into rows
    df['detail'] = df['detail'].str.replace('. Snacks:', ' |')
    df['detail'] = df['detail'].replace({'Meals: ': '', 'Snacks: ': ''}, regex=True)
    df['detail'] = df['detail'].str.split(' \| ')
    df = df.explode('detail')

    # Get values from details
    df.loc[df['category'] == 'Sleep', 'value'] = df.loc[df['category'] == 'Sleep', 'value'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
    df['value'] = df.apply(lambda record: determine_value([record['detail']], record['value']), axis=1)

    # Clean details values
    df.loc[df['detail'].str.contains('activ', case=False, na=False), 'detail'] = 'Activity'
    df.loc[df['detail'].str.contains('sociab', case=False, na=False), 'detail'] = 'Sociable'
    df.loc[df['detail'].str.contains('Social', case=False, na=False), 'detail'] = 'Social (qual)'
    df.loc[df['detail'].str.contains('calories', case=False, na=False), 'detail'] = 'Calories'
    df['detail'] = df['detail'].str.replace('Vitamin', 'Vit')
    df['detail'] = df['detail'].str.replace('Distractibility/inattentive', 'Distractibility')
    df['detail'] = df['detail'].str.replace('Difficulty task switching', 'Task switching')
    df['detail'] = df['detail'].str.replace('Difficulty concentrating', 'Focus issue')
    df['detail'] = df['detail'].str.replace('Get sunlight in the morning', 'Morning sun')
    df['detail'] = df['detail'].str.replace('Carbohydrates', 'Carbs')
    df['detail'] = df['detail'].str.replace(r'Heart rate \(bpm\) - (Min|Average|Max)', r'\1 heart rate', regex=True)
    df['detail'] = df['detail'].str.replace('1:1', '1 to 1')
    df['detail'] = df['detail'].str.replace('🖐️', 'Hand')
    df['detail'] = df['detail'].str.replace(r'[<(>:].*', '', regex=True)
    df['detail'] = df['detail'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
    df['detail'] = df['detail'].str.replace(r'\s+', ' ', regex=True)
    df['detail'] = df['detail'].str.strip()
    #################################
    # To do: work on times of day -> period
    input(df[df['category'] == 'Intakes']['detail'].unique())
    for detail in sorted(df[df['category'].str.contains('actor')]['detail'].unique()):
        print(detail)
    input('')

    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # data.wellbeing_outcomes = [value.split()[0].strip() for value in data.wellbeing_outcomes]
    #################################
    data.sets['bearable'] = df
