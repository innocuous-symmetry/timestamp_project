from database import *
from datetime import *

# String format for datetime string
# "%Y-%m-%d %H:%M:%S.%f"

user_prompt = """
Please choose from the following options:
1) New time punch
2) Select all timestamps (option: limit number of results)
3) Find a timestamp by session id
4) Calculate total hours for the week
5) Calculate complete sum of hours
"""

# New time punch:
def handle_first_option():
    in_out = input("Punching in or out? i/o \n")

    if in_out == 'i':
        time_of_stamp = datetime.now()
        print("Creating new timestamp and punching in!")
        print("Please enter the following details:")
        name = input("Your name: ")
        purpose = input("Current task: ")
        print("Please confirm your details:")
        confirmation = input(f'{name} clocking in at {time_of_stamp} for {purpose}. Confirm? y/n ')

        if confirmation == 'n':
            handle_first_option()
        elif confirmation == 'y':
            create_new_stamp(time_of_stamp, name, purpose)
            session_id = get_created_id(time_of_stamp)
            for data in session_id:
                print(f'Session id: {data[0]}')
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
        time_of_stamp = datetime.now()
        print("Preparing to punch out.")
        session = input("Please provide your session ID: ")
        punch_out(time_of_stamp, session)
        print("Punch out successful. Returning...")
        parse_input()
    else:
        print("Invalid input. Please try again:")
        handle_first_option()

# Select time stamps:
def handle_second_option():
    limit_results = input("Returning all timestamps. Limit results? y/n \n")
    if limit_results == 'n':
        output = get_all_stamps()
        for row in output:
            print(row)

        another_selection = input("Make another selection? y/n \n")

        if another_selection == 'y':
            parse_input()
        elif another_selection == 'n':
            pass
        else:
            print("Make another selection:")
            parse_input()
        

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

# Find stamp by session id
def handle_third_option():
    user_id = input("Provide your session id: ")
    response = get_created_id(user_id)

    print("Data fetched successfully:")
    for data in response:
        print(data)
    
    new_selection = input("Make another selection? y/n ")
    if new_selection == 'y':
        parse_input()
    elif new_selection == 'n':
        pass
    else:
        print("Invalid input.")
        parse_input()

# Calculate weekly hours
def handle_fourth_option():
    print("Find weekly hours.")
    # target = input("Enter a target user name: ")
    # print(f'Find weekly hours for {target}')
    result = get_weekly_hours()

    total_hours = []
    for data in result:
        inner_comparison = []
        for each in data:
            inner_comparison.append(datetime.strptime(each, "%Y-%m-%d %H:%M:%S.%f"))
        total_hours.append(inner_comparison[1] - inner_comparison[0])
    
    print(total_hours)

    hours = 0
    minutes = 0
    total = 0
    for item in total_hours:
        total += item.seconds + (item.microseconds / 10 ** 6)

    hours = total / (60 * 60)
    minutes = total / 60
    print(f'Weekly hours: {round(hours, 3)}')
    print(f'In minutes: {round(minutes, 3)}')


def __admin__():
    print("ADMIN PORTAL")
    print("Choose from additional actions below:")
    print("""
    1) Delete all rows from table (table and schema will persist)
    2) Drop table (database will reinitialize on next render)
    3) Backup data from SQLite file.
    4) Populate with hard coded values

    Take care, some actions will permanently delete all data.\n
    """)
    admin_prompt = input("Your response: ")

    if int(admin_prompt) == 1:
        print("Deleting all rows...")
        delete_all_rows()
        print("All rows deleted. Terminating program:")
    elif int(admin_prompt) == 2:
        print("Drop table. Confirm?")
    elif int(admin_prompt) == 3:
        print("Back up all SQLite data.")
    elif int(admin_prompt) == 4:
        print("Populate hard coded data.")
    else:
        print("Invalid input.")



# Dialogue tree for top-level path handling

def parse_input():
    print(user_prompt)
    response = input("Enter your selection: ")

    # Error handling
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

    # Directing to secondary functions
    if response == 1:
        handle_first_option()
    elif response == 2:
        handle_second_option()
    elif response == 3:
        handle_third_option()
    elif response == 4:
        handle_fourth_option()
    elif response == 5:
        pass
    elif response == 90909:
        __admin__()
    else:
        print("Please provide a valid selection.")
        parse_input()