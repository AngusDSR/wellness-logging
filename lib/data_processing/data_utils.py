from datetime import datetime
import glob, re

# start_date = '2023-06-01'
# end_date = datetime.today().strftime('%Y-%m-%d')
correlation_threshold = 0.4
sets = {}

source = {
    'bearable': glob.glob('data/bearable-export-*.csv')[0],
    'nutrition': 'data/dailysummary.csv',
    'weather': 'data/weather.csv',
    'codetime': glob.glob('data/records-*.csv')[0],
    # 'trello': None,
    # 'spotify': None,
    # 'fitbit': None,
    # etc.
}

# TO DO: Add more categories
# This needs to be updated to reflect the categories in the bearable data
wellbeing_outcomes = [
    'Productivity',
    'Calmness 😌',
    'Motivation 💪',
    'Wake-up time 🌅 (5=7, 4=7.30...)',
    'Snoring (up to) 😴 5=40m   4=1hr   3=1:45m   2=2.45...',
    'Mood',
    'Symptom',
    'Energy',
    'Planning',
    'Focus',
    'Sleep quality'
]

key_nutrition_intakes = [
    'Protein',
    'Net Carbs',
    'Fiber',
    'Fat',
    'B6',
    'Folate',
    'B12',
    'Vitamin A',
    'Vitamin C',
    'Vitamin D',
    'Vitamin E',
    'Iron',
    'Magnesium',
    'Zinc',
    'Potassium',
    'Selenium',
    'Omega-3',
    'Phenylalanine',
]

time_periods = {
    'early': '06:00',
    'morning': '12:00',
    'afternoon': '18:00',
    'evening': '23:59',
    # 'All day':
}

# To do: remove
# date_table = pd.date_range(start=start_date, end=end_date, freq='D')
# date_table = pd.DataFrame(date_table, columns=['date'])
# date_table['day'] = date_table['date'].dt.strftime('%a')

def strip_emoji(string):
    return string.str.replace(r'[<(>:].*', '', regex=True)

def remove_paranthesised_column_text(columns):
    return [re.sub(r'\(.*\)', '', col).strip() for col in columns.copy()]

def convert_time_string_to_hours(timestring):
    print(timestring)
    print(type(timestring))
    # To do: add error handling for split - should only take 'hh:mm' format
    # time_split = timestring.split(':')
    # return int(time_split[0]) + (int(time_split[1]) / 60)

def get_time_period(time):
    # options:
    # - NaN -> check for floats -> return as all day
    # - a string 'am' 'pm' -> if in ... -> map to new ones
    # - a string in hh:mm 8:49 -> apply the logic below

    input(type(time))
    input(time)
    return

    if time.isna:
        input('na')
        return
    elif type(time) == Str:
        input(time)
        return
    else:
        for period, hours in time_periods.items():
            if time <= hours:
                input(period)
                return period
