"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Sets is_finished to True when a valid integer is entered
    except ValueError:  # Catches the ValueError if a non-integer is entered
        print("Please enter a valid integer.")
print("Valid result is:", result)
