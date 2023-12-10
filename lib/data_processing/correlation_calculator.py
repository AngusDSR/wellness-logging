import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process

def rename_negative_correlations_headers(correlations, table):
    headers = correlations.index
    neg_columns = correlations[correlations < 0].index
    headers = [col + ' (neg)' if col in neg_columns else col for col in headers]
    table.rename(columns={col: col + ' (neg)' for col in neg_columns}, inplace=True)
    return table

def process_correlations(outcomes_data, variables_data, top_n=None, threshold=None):
    outcomes, variables = outcomes_data.copy(), variables_data.copy()
    outcome_count = len(outcomes.columns)
    df = data_process.combine_outcomes_variables(outcomes, variables)
    correlation_values = df.corr().iloc[0:outcome_count, outcome_count:].mean()
    if top_n is not None:
        correlation_values = correlation_values.nlargest(top_n)
    elif threshold is not None:
        correlation_values = correlation_values[correlation_values.abs() > threshold]
    variables = variables[correlation_values.index]
    variables = rename_negative_correlations_headers(correlation_values, variables)
    df = data_process.combine_outcomes_variables(outcomes, variables)
    return df
