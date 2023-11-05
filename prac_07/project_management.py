"""
Program to load and save a data file using a list of objects to manage projects.
Estimated completion time: 1-3 hours (Start @ 11:30am) (Paused @ 12:50pm) : (12->12:47) : (+30mins) : (10:15 -> )
Actual completion time:
"""
import datetime
from prac_07.project import Project

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
            save_filename = input("Enter filename of file to save projects to: ")
            save_projects(save_filename, projects)

        elif selection.upper() == 'D':
            display_projects(projects)

        elif selection.upper() == 'F':
            filter_projects(projects)

        elif selection.upper() == 'A':
            projects = add_project(projects)

        elif selection.upper() == 'U':
            projects = update_project(projects)

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
        project_completion_percentage = int(parts[4])
        project = Project(project_name, project_start_date, project_priority, project_cost_estimate,
                          project_completion_percentage)
        projects.append(project)
    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save list of project objects to chosen file. """
    out_file = open(filename, 'w')
    out_file.writelines("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        print(project.name, project.start_date, project.priority, project.cost_estimate, project.completion_percentage,
              sep="\t", file=out_file)
    out_file.close()
    print("Save to file -> open file write to filename file, print projects to file, close")


def display_projects(projects):
    """Display projects listed in completed and incomplete projects. """
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    completed_projects.sort()
    incomplete_projects.sort()

    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def filter_projects(projects):
    """Filter projects by date, and display sorted by date. """
    # date_string = input("Date (d/m/yyyy): ")
    # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filter_date = input("Date (d/m/yyyy): ")
    for project in projects:
        projects.sort()
        if project.start_date > filter_date:
            print(project)


def add_project(projects):
    """Add new project with details"""
    # new_project = []
    print("Let's add a new project")
    new_name = input("Name: ")
    # new_start_date_string = input("Start date (d/m/yyyy): ")
    # new_start_date = datetime.datetime.strptime(new_start_date_string, "%d/%m/%Y").date()
    new_start_date = input("Start date (d/m/yyyy): ")
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

    project_choice = int(input("Project choice: "))
    project_index = project_choice - 1
    print(projects[project_index])
    try:
        updated_percentage = int(input("New Percentage: "))
    except ValueError:
        print("Invalid Percentage.")
        updated_percentage = int(input("New Percentage: "))
    if updated_percentage != "":
        projects[project_index].completion_percentage = updated_percentage
    try:
        updated_priority = int(input("New Priority: "))
    except ValueError:
        print("Invalid Priority.")
        updated_priority = int(input("New Priority: "))
    if updated_priority != "":
        projects[project_index].priority = updated_priority
    return projects


main()
