import lib.utils.input_handler as ask
import lib.data_processing.bearable_data as bear
import lib.data_processing.data_utils as data
import lib.data_processing.data_processing as data_process
from lib.data_processing.data_utils import correlation_threshold as def_corr_threshold
import lib.data_processing.correlation_calculator as correlate

def nutrition_analysis():
    data_process.prepare_nutrition_data()
    selected_outcomes = ask.for_multiple_inputs(data.wellbeing_outcomes, 3, 'wellbeing outcome')
    outcomes_data = bear.filter_outcomes(selected_outcomes)
    # To do: Make a 'choose between' function for this
    selected_intakes = ask.about_variable_factors(data.sets['nutrition'], data.key_nutrition_intakes, 'nutritional intakes')
    average_over_days = ask.about_averaging()
    selected_intakes = data_process.average_over_days(selected_intakes, average_over_days)
    intakes_data = data_process.normalise_values(selected_intakes)
    correlation_method = ask.for_single_input([f'Use the default correlation threshold ({def_corr_threshold})', 'Choose a custom correlation threshold', 'See the top x correlated inputs'])
    if correlation_method == 0:
        correlation_threshold = def_corr_threshold
    elif correlation_method == 1:
        correlation_threshold = ask.for_number_in_range(0.2, 1, "threshold")
        print("Threshold set to:", correlation_threshold, ".")
    elif correlation_method == 2:
        correlation_threshold = ask.for_number_in_range(1, 15, "number of top correlated inputs to select")
        print("Top", correlation_threshold, "correlations selected")

def test():
    data_process.prepare_nutrition_data()
    outcomes_data = bear.filter_outcomes(['Mood', 'Energy'])
    intakes_data = data_process.normalise_values(data.sets['nutrition'])

    # Test from here:
    # need to check that we can skip columns after averaging: which leaves first x cols blank
    ######################
    correlation_matrix = correlate.using_threshold(outcomes_data, intakes_data, def_corr_threshold, 2)

    # To do: return correlation method based on response
    ask.stop()
