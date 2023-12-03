import lib.utils.input_handler as ask
import lib.controllers.main_controller as controller

def nut_analysis_menu():
    nut_analysis_selection = ask.for_single_input(['Intakes vs outcomes', 'Exit'])
    if nut_analysis_selection == 0:
        controller.nutrition_analysis()
    else:
        ask.stop()
    None

menu_selection = ask.for_single_input(['Nutrition analysis', 'Factor analysis', 'Reports', 'Settings', 'View data', 'Exit'])
if menu_selection == 0:
    nut_analysis_menu()
# elif menu_selection == 1:
#     controller.factor_analysis()
# elif menu_selection == 2:
#     controller.reports()
# elif menu_selection == 3:
#     controller.settings()
# elif menu_selection == 4:
#     controller.view_data()
elif menu_selection == 5:
    ask.clear()
    ask.stop()
else:
    None
