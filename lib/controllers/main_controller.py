import lib.utils.input_handler as ask
import lib.data_processing.bearable_data as bear
# from lib.data_processing.nutrition_data import df as nut

def nutrition_analysis():
    selected_outcomes = ask.about_outcomes()
    outcomes_data = bear.filter_outcomes(selected_outcomes)
    # get clensed bear data
    # get cleansed nutrition data
    # pass to combiner
