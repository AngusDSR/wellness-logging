import os
import sys
import numpy as np
import lib.data_processing.data as data

def clear():
    os.system('clear')

def stop():
    sys.exit()

def invalid_input():
    clear()
    print("Invalid input. Try again.\n")

# DEBUG
# Add option to return to previous menu
# Add shrinking/selection functionality
# Add option (via arguement) to return number or value
def asker(prompt, options, shrinking=False):
    clear()
    while True:
        print(prompt)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        user_input = input("\nEnter the corresponding number: ")

        if not user_input.isdigit():
            invalid_input()
            continue

        user_input = int(user_input) - 1

        if 0 <= user_input < len(options):
            return options[user_input]
        else:
            clear()
            invalid_input()

def about_inputs(df, high_variance_intakes):
    while True:
        user_input = input("Select an option:\n\n1. Analyse key nutritional intakes\n2. Analyse intakes with a high degree of variation\n3. See the list of highly variable intakes\n4. See the list of key inputs\n5. Exit\n\nEnter the corresponding number: ")
        clear()
        if user_input == "5":
            break

        if user_input == "3":
            print("\nHighly variable intakes (top 10):")
            for index, item in enumerate(high_variance_intakes, start=1):
                print(f"{index}. {item}")

        elif user_input == "4":
            print("\nKey inputs:")
            for index, item in enumerate(data.key_intakes, start=1):
                print(f"{index}. {item}")

        elif user_input == "2":
            return df[high_variance_intakes]

        elif user_input == "1":
            return df[data.key_intakes]

        else:
            invalid_input()
            continue

def about_outcomes():
    selected_outcomes = []
    while len(selected_outcomes) < 3:
        if len(selected_outcomes) > 0:
            clear()
            None

        print("Select up to 3 outcomes from the 'category' column. When you are finished, enter '0'.\n")
        unique_values = data.wellbeing_outcomes
        for i, value in enumerate(unique_values):
            print(f"{i+1}. {value}")

        print("\n0. STOP\n\nSelected outcomes:", ", ".join(map(str, np.array(selected_outcomes)))) if selected_outcomes != [] else None

        user_input = input("\nEnter the corresponding number: ")

        if not user_input.isdigit():
            invalid_input()
            continue

        user_input = int(user_input) - 1

        if user_input == -1 and selected_outcomes:
            break
        elif user_input == -1 and not selected_outcomes:
            clear()
            print("*** Select at least one outcome ***")
            continue

        if 0 <= user_input < len(unique_values):
            selected_value = unique_values.pop(user_input)
            selected_outcomes.append(selected_value)
        else:
            clear()
            invalid_input()

    selected_outcomes_array = np.array(selected_outcomes)
    clear()
    print("Selected outcomes:", ", ".join(map(str, np.array(selected_outcomes))))
    return selected_outcomes_array

def about_averaging():
    while True:
        user_input = input("Would you like to average the intake values over a series of days?\n\n1. Average the data\n2. Do not average the data\n3. Exit\n\nEnter the corresponding number: ")
        clear()
        if user_input == "3":
            stop()

        if user_input == "2":
            return False
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

def get_numeric_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)

        try:
            numeric_value = float(user_input)

            if min_value <= numeric_value <= max_value:
                return numeric_value
            else:
                invalid_input()
        except ValueError:
            invalid_input()

def about_correlation():
    while True:
        user_input = input("Select an option:\n\n1. Use the default correlation threshold (0.4)\n2. Choose a custom correlation threshold\n3. Select the top x correlated inputs\n4. Exit\n\nEnter the corresponding number: ")
        clear()

        if user_input == "4":
            stop()

        if user_input == "1":
            return [0, data.correlation_threshold]
        elif user_input == "2":
            correlation_threshold = get_numeric_input("Enter a threshold between 0.2 and 1: ", 0.2, 1)
            clear()
            print("Threshold set to:", correlation_threshold)
            return [0, correlation_threshold]
        elif user_input == "3":
            top_n = get_numeric_input("Enter a top n between 1 and 10: ", 1, 10)
            clear()
            print("Filtering to top ", top_n)
            return [2, int(top_n)]
        else:
            invalid_input()

clear()
