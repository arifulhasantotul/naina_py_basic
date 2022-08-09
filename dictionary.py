
# conversion function of days to hours
def days_to_units(days, unit):
    if unit == "hours" or unit == "hour" or unit == "hr" or unit == "hrs":
        return f"{days} days are {days * 24} {unit}"
    elif unit == "minutes" or unit == "minute" or unit == "min":
        return f"{days} days are {days * 24 * 60} {unit}"
    elif unit == "seconds" or unit == "second" or unit == "sec":
        return f"{days} days are {days * 24 * 60 * 60} {unit}"
    else:
        return "unsupported unit"


# error handling of user input
def validate_and_execute(user_input):
    try:
        user_num = float(user_input["days"])
        if user_num > 0:
            calculated_value = days_to_units(user_num, user_input["unit"])
            print(calculated_value)
        else:
            print(f"{user_num} is not a positive number!")
    except ValueError:
        if user_input == 'exit':
            print("Application closed!")
        else:
            print(f"{user_input} is not a positive number!\n")


prompt_input = ""
while prompt_input != "exit":
    prompt_input = input("Enter total_days and conversion_unit as total_days:conversion_unit e.g. 20:hours \n")
    days_and_unit = prompt_input.split(":")
    print(days_and_unit)
    my_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(my_dictionary)
    validate_and_execute(my_dictionary)
