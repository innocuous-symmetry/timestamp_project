from database import *

user_prompt = """
Welcome to the personal time stamp program.
This program is intended to help you keep track of your work hours on personal projects.

Please choose from the following options:
1) Select all timestamps (option: limit number of results)
2) Find a timestamp by date range
3) Calculate total hours for the week
4) Calculate complete sum of hours
"""

def handle_first_option():
    limit_results = input("Returning all timestamps. Limit results? y/n \n")
    if limit_results == 'n':
        output = get_all_stamps()
        for row in output:
            print(row)

    elif limit_results == 'y':
        def find_row_limit():
            user_limit = input("How many rows? \n")
            table_length = get_table_length()

            try:
                user_limit = int(user_limit)
            except ValueError:
                print("Please provide an integer.")
                find_row_limit()
            except:
                print("An unknown error occurred. Please try again.")
                find_row_limit()
            
            if (user_limit > table_length):
                print("Provided input is larger than available rows in table.")
                print("Printing all rows...")
                output = get_all_stamps()
                for row in output:
                    print(row)
            else:
                table_rows = get_number_of_stamps(user_limit)
                for row in table_rows:
                    print(row)
            
            another_selection = input("Make another selection? y/n \n")

            if another_selection == 'y':
                parse_input()
            elif another_selection == 'n':
                pass
            else:
                print("Make another selection:")
                parse_input()

        find_row_limit()
    
    elif limit_results != 'y' or limit_results != 'n':
        print("Please provide a valid selection.")
        handle_first_option()


def handle_second_option():
    pass

def handle_third_option():
    pass

def handle_fourth_option():
    pass


def parse_input():
    print(user_prompt)
    response = input("Enter your selection: ")

    try:
        response = int(response)
    except ValueError:
        print("Please provide an integer.")
        parse_input()
    except:
        print("Please provide a valid input.")
        parse_input()



    if type(response) == int:
        print(f'You selected {response}. Working...')



    if response == 1:
        handle_first_option()
    elif response == 2:
        pass
    elif response == 3:
        pass
    elif response == 4:
        pass
    else:
        print("Please provide a valid selection.")
        parse_input()