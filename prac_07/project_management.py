"""
Program to load and save a data file using a list of objects to manage projects.
Estimated completion time: 1-3 hours (Start @ 11:30am) (Paused @ 12:50pm)
Actual completion time:
"""
import datetime
from prac_07.project import Project

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


def main():
    print(MENU)
    selection = input(">>> ")
    while selection.upper() != 'Q':
        if selection.upper() == 'L':
            print("Load projects")  # Note to self
            load_filename = input("Enter filename of file to load projects from. ")
            projects = load_projects(load_filename)
            print(projects)  # DEBUGGING

        elif selection.upper() == 'S':
            print("Save projects")  # Note to self
            save_filename = input("Enter filename of file to save projects to. ")
            save_projects(save_filename, projects)

        elif selection.upper() == 'D':
            print("Display projects")  # Note to self
            display_projects(projects)

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
def load_projects(filename):
    projects = []
    filename = filename
    try:
        in_file = open(filename, 'r')
    except FileNotFoundError:
        print("File Not Found / Does Not Exist.")
        filename = input("Enter filename to load projects from. ")
    in_file = open(filename, 'r')
    # File format is: Name, Start Date, Priority, Cost Estimate, Completion Percentage.
    in_file.readline()  # Use readline to skip the file header.
    for line in in_file:
        parts = line.strip().split('\t')
        print(parts)  # DEBUGGING

        project_name = parts[0]
        project_start_date = parts[1]
        project_priority = parts[2]
        project_cost_estimate = parts[3]
        project_completion_percentage = parts[4]
        project = Project(project_name, project_start_date, project_priority, project_cost_estimate,
                          project_completion_percentage)

        # project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
        # projects.sort() - THIS WILL BE IN DISPLAY, WHERE IT IS ALSO SORTED BY PRIORITY
        # projects.sort() - THIS WILL BE IN FILTER BY DATE, WHERE IT IS ALSO SORTED BY DATE.
    in_file.close()
    return projects


def save_projects(filename, projects):
    print("Save to file -> open file write to filename file, print projects to file, close")


def display_projects(projects):
    # number_of_projects = 0
    for project in projects:
        # number_of_projects += 1
        name = project[0]
        start_date = project[1]
        priority = project[2]
        cost_estimate = project[3]
        completion_percentage = project[4]
        print(f"{name}, start: {start_date}, priority {priority}, estimate: ${cost_estimate:,.2f}, "
              f"completion: {completion_percentage}")


# UPDATE PROJECTS FUNCTION WILL USE THE NUMBER_OF_PROJECTS FIELD.

main()
