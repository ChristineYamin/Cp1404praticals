
"""
Word Occurrences
Estimate: 30 minutes
Actual:   90 minutes
"""

import datetime
import json

FILENAME = "projects.json"
menu = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"

def main():
    "Displaying Menu"
    print("Welcome to Pythonic Project Management")
    print(menu)
    choice = input(">>> ").upper()
    projects = []  # Initialize projects list outside the loop
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
            print("Projects loaded successfully!")
        elif choice == "S":
            save_projects(projects)
            print("Projects saved successfully!")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    saved_data = input("Would you like to save changes to projects.txt? (Y/N): ").upper()
    if saved_data == 'Y':
        save_projects(projects)
        print("Changes saved to projects.txt")
    print("Thank you for using custom-built project management software.")

def load_projects():
    """ loading the projects"""
    try:
        with open(FILENAME, 'r') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []
    return projects

def save_projects(projects):
    """ Saving the projects"""
    with open(FILENAME, 'w') as file:
        json.dump(projects, file, indent=4)

def display_projects(projects):
    for project in projects:
        print(project)

def filter_projects_by_date(projects):
    """filtering projects by date"""
    date_string = input("Enter a date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project['deadline'] > date.strftime("%Y-%m-%d")]
    for project in sorted(filtered_projects, key=lambda x: x['deadline']):
        print(project)

def add_project(projects):
    """ Adding new project to the projects"""

    name = input("Enter project name: ")
    description = input("Enter project description: ")
    deadline = input("Enter project deadline (YYYY-MM-DD): ")
    priority = input("Enter project priority: ")
    completed = input("Is the project completed? (y/n): ").lower() == 'y'
    project = {'name': name, 'description': description, 'deadline': deadline, 'priority': priority, 'completed': completed}
    projects.append(project)
    print("Project added successfully!")

def update_project(projects):
    """ Updating the projects"""
    name = input("Enter project name to update: ")
    for project in projects:
        if project['name'] == name:
            completion_percentage = input("Enter project completion percentage (leave blank to retain existing): ")
            priority = input("Enter project priority (leave blank to retain existing): ")
            if completion_percentage:
                project['completed'] = int(completion_percentage) >= 100
            if priority:
                project['priority'] = priority
            print("Project updated successfully!")
            return
    print("Project not found.")

main()


