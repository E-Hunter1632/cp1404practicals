"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        # add the exception you want to catch after except - DONE
        print("Please enter a valid integer.")
print("Valid result is:", result) # This is safe to ignore.
is_finished = True

