import datetime

prompt_input = input("enter your goal with a deadline separated by colon \n")
input_list = prompt_input.split(":")

goal = input_list[0]
deadline = input_list[1]

time_format = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(time_format)
print(type(time_format))

current_date = datetime.datetime.today()
print(current_date)

remaining_days = time_format - current_date
print(f"Dear user! Time remaining for your goal: {goal} {int(remaining_days.total_seconds())} seconds")
print(f"Dear user! Time remaining for your goal: {goal} {int(remaining_days.total_seconds() / 60)} minutes")
print(f"Dear user! Time remaining for your goal: {goal} {int(remaining_days.total_seconds() / 60 / 60)} hours")
print(f"Dear user! Time remaining for your goal: {goal} {remaining_days.days} days")

