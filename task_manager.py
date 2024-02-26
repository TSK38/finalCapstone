''' 
This programme is a task manager which allows the user to do various
things such as, e.g. register a user, add/allocate a task, view tasks
generate reports and display some specific statistics  
'''

# Importing libraries
import os
from datetime import datetime, date

# Date format
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to register a user including some validation
def reg_user():
    new_username = input("New Username: ")

    # Check if the username already exists
    while new_username in username_password:
        print("Username already exists. Please choose a different username.\n")
        new_username = input("New Username: ")

    # Asking the user to enter and confirm password
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    # Checking if the passwords entered match
    if new_password == confirm_password:
        print("New user added\n")
        username_password[new_username] = new_password

        # Writing the user login info to user.txt file
        with open("user.txt", "w") as out_file:
            user_data = [f"{k};{username_password[k]}" for k in username_password]
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match.\n")

# Function to add a new task including some validation
def add_task():

    # Asking the user who the task needs to be assigned to
    task_username = input("Name of person assigned to task: ")

    # Checking if the user exists
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username\n")
        return

    # Obtaining further information about the task
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    # Requesting the due date with the above stated format validation
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified\n")

    # Obtaining currrent date
    curr_date = date.today()

    # Creating a task dictionary
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Adding the new task to the task list
    task_list.append(new_task)

    # Storing the updated task list to tasks.txt file
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = [
            ";".join([
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]) for t in task_list
        ]
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.\n")

# Function to view all tasks
def view_all():
    for t in task_list:
        disp_str = f"--------------------------------------------------\n"
        disp_str += f"Task: \t\t\t {t['title']}\n"
        disp_str += f"Assigned to: \t\t {t['username']}\n"
        disp_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \t {t['description']}\n"
        disp_str += f"--------------------------------------------------\n"
        print(disp_str)

# Function to view tasks assigned to the current user
def view_mine(curr_user):
    user_tasks = [t for t in task_list if t['username'] == curr_user]

    # This information will loop until a valid option is chosen
    while True:
        print("Your Tasks:")
        for i, t in enumerate(user_tasks, 1):
            disp_str = f"{i}. Task: \t\t {t['title']}\n"
            disp_str += f"   Assigned to: \t {t['username']}\n"
            disp_str += f"   Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"   Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"   Task Description: \n   {t['description']}\n"
            disp_str += f"   Completed: \t {t['completed']}\n"
            print(disp_str)

        # Asking the user to select accordingly with some validation
        task_selection = input("Enter the number of the task to view details, or enter '-1' to return to the main menu: ")

        try:
            task_selection = int(task_selection)

            if task_selection == -1:
                return
            elif 1 <= task_selection <= len(user_tasks):
                selected_task = user_tasks[task_selection - 1]

                if not selected_task['completed']:
                    action = input(f"Do you want to mark task '{selected_task['title']}' as complete (enter 'C') or edit it (enter 'E')? ").lower()

                    # Only incomplete tasks can be marked as complete
                    if action == 'c':
                        selected_task['completed'] = True

                        # Storing the updated task in tasks.txt file
                        with open("tasks.txt", "w") as task_file:
                            task_list_to_write = [
                                ";".join([
                                    t['username'],
                                    t['title'],
                                    t['description'],
                                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                    "Yes" if t['completed'] else "No"
                                ]) for t in task_list
                            ]
                            task_file.write("\n".join(task_list_to_write))
                        print(f"Task '{selected_task['title']}' marked as complete.\n")

                    # Only incomplete tasks can be edited
                    elif action == 'e':
                        if not selected_task['completed']:
                            new_username = input("Enter the new username (leave blank to keep the current username): ")

                            if not new_username:
                                print("Username cannot be empty. Task not updated.\n")
                            elif new_username not in username_password:
                                print("User does not exist. Task not updated.\n")
                            else:
                                selected_task['username'] = new_username

                                # Storing the updated task in tasks.txt file
                                with open("tasks.txt", "w") as task_file:
                                    task_list_to_write = [
                                        ";".join([
                                            t['username'],
                                            t['title'],
                                            t['description'],
                                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                            "Yes" if t['completed'] else "No"
                                        ]) for t in task_list
                                    ]
                                    task_file.write("\n".join(task_list_to_write))
                                print(f"Task '{selected_task['title']}' updated.")
                        else:
                            print("Completed tasks cannot be edited.\n")
                else:
                    print("Completed tasks cannot be edited.\n")
            else:
                print("Invalid task number. Please enter a valid task number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
        except IndexError:
            print("Invalid task number. Please enter a valid task number.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

# Function to generate reports, only if current user is Admin
def generate_reports():
    if curr_user == 'admin':
        total_tasks = len(task_list)
        completed_tasks = sum(1 for task in task_list if task['completed'])
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())

        # Calculate percentages
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

        # Storing the generated report in task_overview.txt file
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write("Task Overview\n")
            task_overview_file.write("-----------------\n")
            task_overview_file.write(f"Total Tasks: {total_tasks}\n")
            task_overview_file.write(f"Completed Tasks: {completed_tasks}\n")
            task_overview_file.write(f"Uncompleted Tasks: {uncompleted_tasks}\n")
            task_overview_file.write(f"Overdue Tasks: {overdue_tasks}\n")
            task_overview_file.write(f"Percentage of Incomplete Tasks: {incomplete_percentage:.2f}%\n")
            task_overview_file.write(f"Percentage of Overdue Tasks: {overdue_percentage:.2f}%\n")

        total_users = len(username_password.keys())

        # Storring the generated report in user_overview.txt. file
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write("User Overview\n")
            user_overview_file.write("-----------------\n")
            user_overview_file.write(f"Total Users: {total_users}\n")
            user_overview_file.write(f"Total Tasks: {total_tasks}\n")

            for user, password in username_password.items():
                user_tasks = [task for task in task_list if task['username'] == user]
                total_user_tasks = len(user_tasks)
                completed_user_tasks = sum(1 for task in user_tasks if task['completed'])

                user_percentage_total_tasks = (total_user_tasks / total_tasks) * 100 if total_tasks > 0 else 0
                user_percentage_completed_tasks = (completed_user_tasks / total_user_tasks) * 100 if total_user_tasks > 0 else 0

                user_overview_file.write(f"\nUser: {user}\n")
                user_overview_file.write(f"Total Tasks Assigned: {total_user_tasks}\n")
                user_overview_file.write(f"Percentage of Total Tasks Assigned: {user_percentage_total_tasks:.2f}%\n")
                user_overview_file.write(f"Percentage of Completed Tasks: {user_percentage_completed_tasks:.2f}%\n")

        print("Reports generated successfully!")
    else:
        print("Access denied. Only Admin can generate reports.")

# If tasks.txt file doesn't exist it'll get created
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Once created the code will read the data within tasks.txt file
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Creating an empty list to fill it with data from tasks.txt file
task_list = []
for t_str in task_data:
    curr_t = {}
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)

# If user.txt file doesn't exist it'll get created
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Once created the code will read the data within user.txt file
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Creating a dictionary to store the data from user.txt file
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False

# This loop will continue until the user enters a valid username and
# password
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist, please try again.\n")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password, please try again.\n")
    else:
        print("Login Successful!\n")
        logged_in = True

# This loop is to ensure the main menu keeps appearing until the user
# enters 'e' for exiting the programme
while True:
    print()
    menu = input('''Please select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics 
e - exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(curr_user)

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds':
        if curr_user == 'admin':
            num_users = len(username_password.keys())
            num_tasks = len(task_list)

            print("-----------------------------------")
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("-----------------------------------")
        else:
            print("Access denied. Only Admin can display statistics.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice. Please Try again")
