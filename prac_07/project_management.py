"""
Program to load and save a data file using a list of objects to manage projects.
Estimated completion time: 1-2 hours (Start @ 11:30) (Paused @ )
Actual completion time:
"""
import datetime

# ------------------------------------------------------------------- EXAMPLE CODE
# The following code reads a string from user input,
# converts it to a date object (using the strptime method from the datetime type),
# prints the day of the week (%A) and then prints the date as a string:

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
# -------------------------------------------------------------------- EXAMPLE CODE

# Load projects -> prompt for filename to load, then load
# Save projects -> prompt for filename to save, then save
# Display projects -> display 2 groups, incomplete projects, completed projects, Both sorted by priority.
# Filter projects by date -> ask for date, display only projects that start after that date, sorted by date.
# Use the datetime date module.
# Add new project -> ask for the inputs, then add new project to memory.
# Update project -> choose project, modify completion % and/or priority - leave blank to retain existing values.

# MENU remains the same throughout program.
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n"
        "(U)pdate project\n(Q)uit")
# filename which can change based on what the user enters, Maybe move to separate load and save function.
filename = ""


def main():
    print(MENU)
    selection = input(">>> ")
    while selection.upper() != 'Q':
        if selection.upper() == 'L':
            print("Load projects")  # Note to self
            # Call function here

        elif selection.upper() == 'S':
            print("Save projects")  # Note to self
            # Call function here

        elif selection.upper() == 'D':
            print("Display projects")  # Note to self
            # Call function here

        elif selection.upper() == 'F':
            print("Filter projects by date")  # Note to self
            # Call function here

        elif selection.upper() == 'A':
            print("Add new project")  # Note to self
            # Call function here

        elif selection.upper() == 'U':
            print("Update project")  # Note to self
            # Call function here

        else:
            print("Invalid Menu Selection.")
        print(MENU)
        selection = input(">>> ")
    print("Thank you for using custom-built project management software.")


# FOR READING - projects file contains a header, Want to ignore it when reading, Use in_file.readline()


main()
