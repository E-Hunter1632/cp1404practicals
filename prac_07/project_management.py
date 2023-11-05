"""
Program to load and save a data file using a list of objects to manage projects.
Estimated completion time: 1-3 hours (Start @ 11:30am) (Paused @ 12:50pm) : (12->12:47) : (+30mins) : (10:15 -> )
Actual completion time:
"""
import datetime
from prac_07.project import Project
from operator import itemgetter

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


def main():
    """Custom-built project manager menu interface. """
    print(MENU)
    selection = input(">>> ")
    while selection.upper() != 'Q':
        if selection.upper() == 'L':
            load_filename = input("Enter filename of file to load projects from: ")
            projects = load_projects(load_filename)

        elif selection.upper() == 'S':
            print("Save projects")  # Note to self
            save_filename = input("Enter filename of file to save projects to: ")
            save_projects(save_filename, projects)

        elif selection.upper() == 'D':
            print("Display projects")  # Note to self
            display_projects(projects)

        elif selection.upper() == 'F':
            print("Filter projects by date")  # Note to self
            filter_projects(projects)

            # date_string = input("Date (d/m/yyyy): ")
            # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            # print(date)  # DEBUGGING

        elif selection.upper() == 'A':
            projects = add_project(projects)

        elif selection.upper() == 'U':
            print("Update project")  # Note to self
            # Call function here
            update_project(projects)
            print(projects)  # DEBUGGING

        else:
            print("Invalid Menu Selection.")
        print(MENU)
        selection = input(">>> ")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from chosen filename and store to list of objects. """
    projects = []
    filename = filename
    try:
        in_file = open(filename, 'r')
    except FileNotFoundError:
        print("File Not Found / Does Not Exist.")
        filename = input("Enter filename to load projects from: ")
    in_file = open(filename, 'r')
    # File format is: Name, Start Date, Priority, Cost Estimate, Completion Percentage.
    in_file.readline()  # Use readline to skip the file header.
    for line in in_file:
        parts = line.strip().split('\t')

        project_name = parts[0]
        project_start_date = parts[1]
        project_priority = int(parts[2])
        project_cost_estimate = float(parts[3])
        project_completion_percentage = float(parts[4])
        project = Project(project_name, project_start_date, project_priority, project_cost_estimate,
                          project_completion_percentage)

        projects.append(project)
        # projects.sort() - THIS WILL BE IN DISPLAY, WHERE IT IS ALSO SORTED BY PRIORITY
        # projects.sort() - THIS WILL BE IN FILTER BY DATE, WHERE IT IS ALSO SORTED BY DATE.
    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save list of project objects to chosen file. """
    print("Save to file -> open file write to filename file, print projects to file, close")


def display_projects(projects):
    """Display projects listed in completed and incomplete projects. """
    print("Completed Projects: SELF-NOTE: ADD THIS")
    print("Incomplete Projects: SELF-NOTE: ADD THIS")
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
        # completed_projects.sort()
        # incomplete_projects.sort()

    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def filter_projects(projects):
    """Filter projects by date, and display sorted by date. """
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(date)  # DEBUGGING
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
        print("SELF-NOTE: THIS NEEDS TO BE SORTED BY DATE")


def add_project(projects):
    """Add new project with details"""
    # new_project = []
    print("Let's add a new project")
    new_name = input("Name: ")
    new_start_date_string = input("Start date (d/m/yyyy): ")
    new_start_date = datetime.datetime.strptime(new_start_date_string, "%d/%m/%Y").date()
    new_priority = int(input("Priority: "))
    new_cost_estimate = float(input("Cost estimate: "))
    new_percent_complete = int(input("Percent complete: "))
    print(f"Project: {new_name}, start: {new_start_date}, priority {new_priority}, "
          f"estimate: ${new_cost_estimate:,.2f}, completion: {new_percent_complete}%, Added to project list. ")
    # new_project.append(Project(new_name, new_start_date, new_priority, new_cost_estimate, new_percent_complete))
    projects.append(Project(new_name, new_start_date, new_priority, new_cost_estimate, new_percent_complete))
    return projects


def update_project(projects):
    """Update project percentage and/or priority, leave blank to retain info. """
    number_of_projects = 0
    for project in projects:
        number_of_projects += 1
        print(f"{number_of_projects} {project}")
        # name = project[0]
        # start_date = project[1]
        # priority = project[2]
        # cost_estimate = project[3]
        # completion_percentage = project[4]
        # print(
        #     f"{number_of_projects} {name}, start: {start_date}, priority {priority}, estimate: ${cost_estimate:,.2f}, "
        #     f"completion: {completion_percentage}")
    project_choice = int(input("Project choice: "))
    project_index = project_choice - 1
    print(project_index)  # DEBUGGING
    print("SELF-NOTE: PRINT PROJECT USING CHOICE AS INDEX - 1, LIKE ASSIGNMENT")
    updated_percentage = int(input("New Percentage: "))
    # if updated_percentage == "":
    #     updated_percentage = completion_percentage
    # else:
    #     updated_percentage = updated_percentage
    print(updated_percentage)  # DEBUGGING
    updated_priority = int(input("New Priority: "))
    # if updated_priority == "":
    #     updated_priority = priority
    # else:
    #     updated_priority = updated_priority
    print(updated_priority)  # DEBUGGING


# UPDATE PROJECTS FUNCTION WILL USE THE NUMBER_OF_PROJECTS FIELD.

main()
