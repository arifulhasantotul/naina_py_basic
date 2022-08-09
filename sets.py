"""
    => Data type: Sets
    => Encapsulate with curly braces {}
    => Doesn't contain deplicate items
    => Items in a set do not have a defined order
    => Items cannot be referred to by index
    => Items cannot be changed, only added/removed
"""
my_set = {"January", "February", "March"}
for item in my_set:
    print(item)


my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)

to_hours = 24
name_of_units = "hours"


# conversion function of days to hours
def days_to_units(days):
    return f"{days} days are {days * to_hours} {name_of_units}"


# error handling of user input
def validate_and_execute(user_input):
    try:
        user_num = float(user_input)
        if user_num > 0:
            calculated_value = days_to_units(user_num)
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
    prompt_input = input("Enter a number or number of days as a comma separated list and I'll convert it to hours! \n")
    list_of_days = prompt_input.split(", ")

    print(list_of_days)
    print(type(list_of_days))

    print(set(list_of_days))
    print(type(set(list_of_days)))

    for element in set(list_of_days):
        validate_and_execute(element)

