"""
    => Data type: str, int, float, boolean (True, False)
    video duration: 3:01:35
"""


# conversion function of days to hours
def days_to_units(days, units):
    return f"{days} days are {days * 24} {units}"


# error handling of user input
def validate_and_execute(data):
    try:
        user_num = float(data["days"])
        if user_num > 0:
            calculated_value = days_to_units(user_num, data["unit"])
            print(calculated_value)
        else:
            print(f"{user_num} is not a positive number!")
    except ValueError:
        user_input = data["days"]
        if user_input == 'exit':
            print("Application closed!")
        else:
            print(f"{user_input} is not a positive number!\n")


prompt_message = "Enter a number or number of days as a comma separated list and I'll convert it to hours! \n"
