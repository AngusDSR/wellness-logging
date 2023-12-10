import lib.utils.input_handler as ask
import lib.data_processing.bearable_data as bear
import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process
from lib.data_processing.data_utils import correlation_threshold as def_corr_threshold
import lib.data_processing.correlation_calculator as correlate
import lib.visualization.plotter as plotter

def nutrition_analysis():
    data_process.prepare_nutrition_data()
    selected_outcomes = ask.for_multiple_inputs(data.wellbeing_outcomes, 3, 'wellbeing outcome')
    outcomes_data = bear.filter_outcomes(selected_outcomes)
    # To do: Make a 'choose between' input function for this
    selected_intakes = ask.about_variable_factors(data.sets['nutrition'], data.key_nutrition_intakes, 'nutritional intakes')
    average_over_days = ask.about_averaging()
    selected_intakes = data_process.average_over_days(selected_intakes, average_over_days)
    intakes_data = data_process.normalise_values(selected_intakes)
    correlation_method = ask.for_single_input([f'Use the default correlation threshold ({def_corr_threshold})', 'Choose a custom correlation threshold', 'See the top x correlated inputs'])
    if correlation_method == 2:
        top_n = ask.for_number_in_range(1, 15, "number of top correlated inputs to select")
        print("Top", top_n, "correlations selected")
        filtered_correlations_table = correlate.process_correlations(outcomes_data, intakes_data, top_n)
    elif correlation_method == 0:
        threshold = def_corr_threshold
        # could this not be repeated?
        filtered_correlations_table = correlate.using_threshold(outcomes_data, intakes_data, threshold)
    elif correlation_method == 1:
        threshold = ask.for_number_in_range(0.2, 1, "threshold")
        print("Threshold set to:", threshold, ".")
        filtered_correlations_table = correlate.using_threshold(outcomes_data, intakes_data, threshold)

    chart_type = ask.for_single_input(['columns', 'lines'], 'Put outcomes as columns or as lines?:')
    plotter.line_column_chart(filtered_correlations_table, len(selected_outcomes), chart_type)
    plotter.visualise()
    ask.stop()

def test():
    data_process.prepare_nutrition_data()
    outcomes_data = bear.filter_outcomes(['Energy', 'Mood'])
    intakes = data_process.average_over_days(data.sets['nutrition'], 2)
    intakes_data = data_process.normalise_values(intakes)
    deff_crr = correlate.process_correlations(outcomes_data, intakes_data, threshold=0.5)

    chart_type = ask.for_single_input(['columns', 'lines'], 'Plot outcomes as columns or as lines?:')
    plotter.line_column_chart(deff_crr, 2, chart_type)
    plotter.visualise()
    ask.stop()
