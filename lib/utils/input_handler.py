import os, sys, re
import numpy as np
import inflect
import lib.data_processing.data_utils as data

p = inflect.engine()

def clear():
    os.system('clear')

def stop():
    sys.exit()

def invalid_input(message="Invalid input. Try again."):
    clear()
    lines =  '~' * ( len(message) + 3)
    return f"{lines}\n⚠️ {message}\n{lines}\n"

# TO DO: Add option to return to previous menu
def for_menu_selection(prompt='\nEnter the corresponding number: ', preceeding_message=''):
    return input(f"\n{preceeding_message}{prompt}") if len(preceeding_message) > 0 else input(prompt)

def for_number_in_range(min_value, max_value, value_type='number'):
    clear()
    while True:
        user_input = input(f'Enter {p.a(value_type)} between {min_value} and {max_value}: ')
        if not re.search(r'\d', user_input):
            print(invalid_input())
            continue

        numeric_value = float(user_input) if isinstance(min_value + max_value, float) else int(user_input)

        if min_value <= numeric_value <= max_value:
            return numeric_value
        else:
            print(invalid_input())

def for_single_input(options, prompt="Select an option:\n" ):
    error = ''
    clear()
    while True:
        print(prompt)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        user_input = for_menu_selection(preceeding_message=error)
        if not user_input.isdigit():
            error = invalid_input()
            continue

        user_input = int(user_input) - 1
        if 0 <= user_input < len(options):
            return user_input
        else:
            clear()
            error = invalid_input()

# TO DO: make this dynamic and applicable to different data sets
# TO DO: Refactor these are menus
# Check for existence of key factors
def about_variable_factors(df, key_factors_list, data_set_name='factors'):
    clear()
    df = df.copy()
    highly_variable_factors = df.std().sort_values(ascending=False).head(10).index.tolist()
    while True:
        user_input = for_single_input([f'Analyse key {data_set_name}', f'Analyse {data_set_name} with a high degree of variation (top 10)', f'See the list of highly variable {data_set_name}', f'See the list of key {data_set_name}'])
        clear()
        if user_input == 0:
            return df[key_factors_list]
        elif user_input == 1:
            return df[highly_variable_factors]
        elif user_input == 2:
            print(f"\nHighly variable {data_set_name} (top 10):")
            for index, item in enumerate(highly_variable_factors, start=1):
                print(f"{index}. {item}")
        elif user_input == 3:
            print(f"\nKey {data_set_name}:")
            for index, item in enumerate(key_factors_list, start=1):
                print(f"{index}. {item}")
        else:
            invalid_input()
            continue

# TO DO: What prompt text/customised text would be needed: explanation?
def for_multiple_inputs(options, choice_limit, item_name='option', min_selections=1):
    options = options.copy()
    selection_list = []
    error = ''
    clear()
    while len(selection_list) < choice_limit:
        print(f"Select up to {choice_limit} {p.plural(item_name, choice_limit)} from the list. When you are finished, enter '0'.\n")
        for i, value in enumerate(options):
            print(f"{i+1}. {value} {' ' * (18 - len(value) + (1 if i+1 < 10 else 0))} [{'x' if value in selection_list else ' '}]")
        # SHOULD be lines for the match length of value #DEBUG
        print(f"{(27) * '—'}\n0. Done{' ' * 17} ✓") if selection_list != [] else None
        user_input = for_menu_selection(preceeding_message=error)
        if not user_input.isdigit():
            error = invalid_input()
            continue

        user_input = int(user_input) - 1
        if user_input == -1 and selection_list:
            break
        elif user_input == -1 and not selection_list:
            error = invalid_input(f"Select at least {p.number_to_words(min_selections)} {item_name}.")
            continue

        if 0 <= user_input < len(options):
            selection_list.append(options[user_input])
            error = ''
            clear()
        else:
            error = invalid_input()
            continue

    selection_array = np.array(selection_list)
    return selection_array

# To do: replace with range input
def about_averaging():
    while True:
        user_input = input("Would you like to average the intake values over a series of days?\n\n1. Average the data\n2. Do not average the data\n3. Exit\n\nEnter the corresponding number: ")
        clear()
        if user_input == "3":
            stop()

        if user_input == "2":
            return 1
        elif user_input == "1":
            while True:
                user_input = input("Enter a number of days greater than 1: ")
                if not user_input.isdigit():
                    invalid_input()
                    continue

                user_input = int(user_input)
                if user_input < 2:
                    invalid_input()
                    continue
                clear()
                return user_input
        else:
            invalid_input()
            continue
