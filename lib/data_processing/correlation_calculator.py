import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

# join - find correlations - rename colls

def outcomes_with_variable(outcomes_data, variables_data):
    outcomes, variables = outcomes_data.copy(), variables_data.copy()
    df = data_process.combine_outcomes_variables(outcomes, variables)
    return df.corr()

# To do: finish separating
def using_threshold(correlation_matrix, correlation_threshold):
    outcome_count = data.outcomes_count
    # DEBUG: PRINT OUT TO TEST HOW MANY COLUMNS IS WORKING BASEED ON AVERAGED DAYS
    print('1')
    input(correlation_matrix[0:outcome_count, outcome_count:1])
    print('2')
    input(correlation_matrix[0:outcome_count, outcome_count:2])
    ###################
    input('pause')
    ###################

    if data.averaged_periods:
        correlation_values = correlation_matrix.iloc[0:outcome_count, outcome_count:exclude_average_col].abs().mean()
        input_columns = df.columns[outcome_count:exclude_average_col][correlation_values > correlation_threshold].values
    else:
        correlation_values = correlation_matrix.iloc[0, outcome_count:exclude_average_col]
        input_columns = df.columns[outcome_count:][correlation_values.abs() > correlation_threshold].values

# To do: finish
def using_top_n(correlation_matrix, correlation_filter):
    top_n = correlation_filter[1]
    if 'average' in df.columns:
        correlation_values = correlation_matrix.iloc[0:outcome_count, outcome_count:exclude_average_col].abs().mean()
        input_columns = correlation_values.nlargest(top_n).index
    else:
        correlation_values = correlation_matrix.iloc[0, outcome_count:].abs()
        input_columns = correlation_values.nlargest(top_n).index

    input_columns = rename_negative_correlations_headers(correlation_values, input_columns, df)
    df = df.iloc[:, :outcome_count].join(df[input_columns])
    return df, input_columns


def rename_negative_correlations_headers(correlations, columns_to_change, table):
    for column in columns_to_change:
        if correlations[column] < 0:
            columns_to_change = [col + ' (neg)' if col == column else col for col in columns_to_change]
            table.rename(columns={column: column + ' (neg)'}, inplace=True)
    return columns_to_change
