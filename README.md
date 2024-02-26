
# Task Manager

This programme is a task manager which allows the user to do various things such as, e.g. register a user, add/allocate a task, view tasks generate reports and display some specific statistics.


## Table of Content

    1. Title/Description
    2. Installation
    3. Usage/Examples
    4. Authors
    5. License 
## Installation

Confirmed operation with the following environment:
    
    > Windows operating system Windows 10 or higher
    > Download and install Python 3.10 or higher to run the application
    
## Deployment

### via Command Line

    > Download file (task_manager.py) as well as all the accompanying text file
    > Ensure all files are in one directory 
    > Using the command line prompt, navigate to the folder containing the (task_manager.py) file
    > Finally type the following command (task_manager.py)

### via IDLE

    > Using the windows start menu start the IDLE.
    > Navigate from File and the Open, you can then run the task_manager.py file

## Usage/Examples

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


## Authors

[@TSK38](https://www.github.com/TSK38)


## License

[MIT](https://choosealicense.com/licenses/mit/)

