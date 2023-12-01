import pandas as pd
from datetime import datetime
import glob

start_date = '2023-06-01'
end_date = datetime.today().strftime('%Y-%m-%d')

source = {
    'bearable': pd.read_csv(glob.glob('data/bearable-export-*.csv')[0]),
    'nutrition': pd.read_csv('data/dailysummary.csv'),
    'weather': None,
    # 'trello': None,
    # 'spotify': None,
    # fitbit: None,
    # etc.
}

sets = {}

correlation_threshold = 0.4

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

key_intakes = [
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

date_table = pd.date_range(start=start_date, end=end_date, freq='D')
date_table = pd.DataFrame(date_table, columns=['date'])
date_table['day'] = date_table['date'].dt.strftime('%a')
