import lib.utils.input_handler as ask
import lib.controllers.main_controller as controller

menu_selection = ask.asker('What do you want to do?:\n', ['Nutrition analysis', 'Factor analysis', 'Reports', 'Settings', 'View data', 'Exit'])

# Change to case statement
if menu_selection == 'Nutrition analysis':
    controller.nutrition_analysis()
# elif menu_selection == 'Factor analysis':
#     controller.factor_analysis()
# elif menu_selection == 'Reports':
#     controller.reports()
# elif menu_selection == 'Settings':
#     controller.settings()
# elif menu_selection == 'View data':
#     controller.view_data()
elif menu_selection == 'Exit':
    ask.clear()
    ask.stop()
else:
    None
