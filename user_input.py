user_prompt = """
Welcome to the personal time stamp program.
This program is intended to help you keep track of your work hours on personal projects.

Please choose from the following options:
1) Select all timestamps
2) Find a timestamp by date range
3) Calculate total hours for the week
4) Calculate complete sum of hours
"""

def parse_input():
    print(user_prompt)
    response = input("Enter your selection: ")

    print()