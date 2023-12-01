import pandas as pd
import lib.utils.input_handler as ask
from .nutrition_data import df as nut
from .bearable_data import df as bear

# Set up data
outcome_count = bear.shape[1]
start_row_index = outcome_count if outcome_count == 1 else None
df = pd.merge(bear, nut, on='date', how='inner')
exclude_average_col = None
correlation_matrix = df.corr()

if outcome_count > 1:
    df['average'] = df.iloc[:, :outcome_count].mean(axis=1)
    exclude_average_col = -1

def rename_negative_correlations_headers(correlations, columns_to_change, table):
    for column in columns_to_change:
        if correlations[column] < 0:
            columns_to_change = [col + ' (neg)' if col == column else col for col in columns_to_change]
            table.rename(columns={column: column + ' (neg)'}, inplace=True)
    return columns_to_change

correlation_filter = ask.about_correlation()

# By threshold
if correlation_filter[0] == 0:
    correlation_threshold = correlation_filter[1]
    if 'average' in df.columns:
        correlation_values = correlation_matrix.iloc[0:outcome_count, outcome_count:exclude_average_col].abs().mean()
        input_columns = df.columns[outcome_count:exclude_average_col][correlation_values > correlation_threshold].values
    else:
        correlation_values = correlation_matrix.iloc[0, outcome_count:exclude_average_col]
        input_columns = df.columns[outcome_count:][correlation_values.abs() > correlation_threshold].values

# By top_n
else:
    top_n = correlation_filter[1]
    if 'average' in df.columns:
        correlation_values = correlation_matrix.iloc[0:outcome_count, outcome_count:exclude_average_col].abs().mean()
        input_columns = correlation_values.nlargest(top_n).index
    else:
        correlation_values = correlation_matrix.iloc[0, outcome_count:].abs()
        input_columns = correlation_values.nlargest(top_n).index

input_columns = rename_negative_correlations_headers(correlation_values, input_columns, df)
df = df.iloc[:, :outcome_count].join(df[input_columns])
