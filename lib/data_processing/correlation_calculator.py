import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

def outcomes_with_variables(outcomes_data, variables_data):
    outcomes, variables = outcomes_data.copy(), variables_data.copy()
    df = data_process.combine_outcomes_variables(outcomes, variables)
    return df.corr()


# To do: finish separating
def using_threshold(outcomes_data, variables_data, correlation_threshold, outcome_count):
    correlation_matrix = outcomes_with_variables(outcomes_data, variables_data)
    correlation_values = correlation_matrix.iloc[0:outcome_count, outcome_count:]
    ###################
    print('outcomes', outcome_count)
    input('pause')
    ###################

    correlation_values = correlation_matrix.iloc[0, outcome_count]
    input_columns = df.columns[outcome_count:][correlation_values.abs() > correlation_threshold].values

# To do: finish
def using_top_n(correlation_matrix, correlation_filter):
    top_n = correlation_filter[1]

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
