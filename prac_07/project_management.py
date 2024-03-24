"""
Project Management Program
Estimated time: 5 hours
"""
import csv
from datetime import date, datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.percent_complete}%"

    def __lt__(self, other):
        """Compare projects based on priority (lower value is higher priority)."""
        return self.priority < other.priority

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip header row
            for row in reader:
                name, start_date, priority, cost_estimate, percent_complete = row
                start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
                priority = int(priority)
                cost_estimate = float(cost_estimate)
                percent_complete = int(percent_complete)
                project = Project(name, start_date, priority, cost_estimate, percent_complete)
                projects.append(project)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return projects

def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate, project.percent_complete])

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if project.percent_complete < 100]
    incomplete_projects.sort()
    completed_projects = [project for project in projects if project.percent_complete == 100]
    completed_projects.sort()

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Display projects that start after a given date, sorted by date."""
    start_date_str = input("Show projects that start after date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y').date()
    filtered_projects = [project for project in projects if project.start_date > start_date]
    filtered_projects.sort(key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Let's add a new project\nName: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y').date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)

def update_project(projects):
    """Update the percentage and priority of an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percent_complete = input("New Percentage: ")
    if new_percent_complete:
        project.percent_complete = int(new_percent_complete)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

def main():
    """Run the project management program."""
    projects = load_projects('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print("\n- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").upper()

        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice in ['yes', 'y']:
                save_projects(projects, 'projects.txt')
            print("Thank you for using custom-built project management software.")
            break

if __name__ == '__main__':
    main()