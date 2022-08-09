"""
    video duration: 3:40:31
"""
from helper import validate_and_execute, prompt_message

prompt_input = ""
while prompt_input != "exit":
    prompt_input = input(prompt_message)
    days_and_unit = prompt_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)
