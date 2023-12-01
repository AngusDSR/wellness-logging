import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import lib.utils.input_handler as ask
import data
import re

df = data.source['nutrition']
df = df.rename(columns={'Date': 'date'})
df = df.rename(columns={'Energy (kcal)': 'Calories'})
df = df.drop(columns=['Carbs (g)'])

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.columns = [re.sub(r'\(.*\)', '', col).strip() for col in df.columns]

high_variance_intakes = df.std().sort_values(ascending=False).head(10).index.tolist()
selected_intakes = ask.about_inputs(df, high_variance_intakes)

# Ask user if they want to average the data
average_over_days = ask.about_averaging()
if average_over_days != False:
    selected_intakes = selected_intakes.rolling(window=average_over_days).mean()

df = df.dropna()

# Normalize the selected_intakes with scaler
scaler = MinMaxScaler()
df = pd.DataFrame(
    scaler.fit_transform(selected_intakes),
    columns=selected_intakes.columns,
    index=df.index
)
