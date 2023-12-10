import lib.utils.input_handler as ask
import lib.controllers.main_controller as controller

def run():
    while True:
        main_menu()
        break

def nut_analysis_menu():
    selection = ask.for_single_input(['Intakes vs outcomes', 'Return\n', 'Exit'])
    if selection == 0:
        controller.nutrition_analysis()
    elif selection == 1:
        main_menu()
    else:
        return None
    None

def main_menu():
    menu_selection = ask.for_single_input(['Test', 'Nutrition analysis', 'Factor analysis', 'Reports', 'Settings', 'View data', 'Exit'])
    if menu_selection == 0:
        controller.test()
    elif menu_selection == 1:
        nut_analysis_menu()
    #     controller.factor_analysis()
    # elif menu_selection == 2:
    #     controller.reports()
    # elif menu_selection == 3:
    #     controller.settings()
    # elif menu_selection == 4:
    #     controller.view_data()
    elif menu_selection == 5:
        ask.clear()
    else:
        None
