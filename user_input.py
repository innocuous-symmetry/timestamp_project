from database import *

user_prompt = """
Welcome to the personal time stamp program.
This program is intended to help you keep track of your work hours on personal projects.

Please choose from the following options:
1) Insert a new timestamp
2) Select all timestamps (option: limit number of results)
3) Find a timestamp by date range
4) Calculate total hours for the week
5) Calculate complete sum of hours

"""

# Inner functions detailed below:
def handle_first_option():
    time_of_stamp = datetime.now()
    in_out = input("Punching in or out? i/o \n")

    if in_out == 'i':
        print("Creating new timestamp and punching in!")
        print("Please enter the following details:")
        name = input("Your name: ")
        purpose = input("Current task: ")

        print("\nPlease confirm your details:")
        confirmation = input(f'{name} clocking in at {time_of_stamp} for {purpose}. Confirm? y/n ')

        if confirmation == 'n':
            handle_first_option()
        elif confirmation == 'y':
            create_new_stamp(time_of_stamp, name, purpose)
            new_selection = input("Data entered. Make another selection? y/n ")
            if new_selection == 'y':
                parse_input()
            elif new_selection == 'n':
                pass
            else:
                print("Invalid input. Exiting...")
                pass
        else:
            print("Invalid input.")
            handle_first_option()
    elif in_out == 'o':
        print("Punching out.")
    else:
        print("Invalid input. Please try again:")
        handle_first_option()


def handle_second_option():
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
        handle_second_option()


def handle_third_option():
    pass

def __admin__():
    print("ADMIN PORTAL")
    print("Choose from additional actions below:")
    print("""
    1) Delete all rows from table (table and schema will persist)
    2) Drop table (database will reinitialize on next render)
    3) Backup data from SQLite file.

    Take care, some actions will permanently delete all data.\n
    """)
    admin_prompt = input("Your response: ")

    if int(admin_prompt) == 1:
        print("Deleting all rows...")
        delete_all_rows()
        print("All rows deleted. Returning...")
        parse_input()
    elif int(admin_prompt) == 2:
        print("Drop table. Confirm?")
    elif int(admin_prompt) == 3:
        print("Back up all SQLite data.")
    else:
        print("Invalid input.")



# Dialogue tree for top-level path handling

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
        handle_second_option()
    elif response == 3:
        pass
    elif response == 3:
        pass
    elif response == 4:
        pass
    elif response == 871:
        __admin__()
    else:
        print("Please provide a valid selection.")
        parse_input()