import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

def rename_negative_correlations_headers(correlations, table):
    headers = correlations.index
    neg_columns = correlations[correlations < 0].index
    headers = [col + ' (neg)' if col in neg_columns else col for col in headers]
    table.rename(columns={col: col + ' (neg)' for col in neg_columns}, inplace=True)
    return table

def using_threshold(outcomes_data, variables_data, correlation_threshold):
    outcomes, variables = outcomes_data.copy(), variables_data.copy()
    outcome_count = len(outcomes.columns)
    df = data_process.combine_outcomes_variables(outcomes, variables)
    correlation_values = df.corr().iloc[0:outcome_count, outcome_count:].mean()
    correlation_values = correlation_values[correlation_values.abs() > correlation_threshold]
    df = df[correlation_values.index]
    df = rename_negative_correlations_headers(correlation_values, df)
    return df

def using_top_n(outcomes_data, variables_data, top_n):
    outcomes, variables = outcomes_data.copy(), variables_data.copy()
    outcome_count = len(outcomes.columns)
    df = data_process.combine_outcomes_variables(outcomes, variables)
    correlation_values = df.corr().iloc[0:outcome_count, outcome_count:].mean()
    correlation_values = correlation_values.nlargest(top_n)
    df = df[correlation_values.index]
    df = rename_negative_correlations_headers(correlation_values, df)
    return df
