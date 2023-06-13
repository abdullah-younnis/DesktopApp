import json


# function to add new salary
def create_salary():
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")
    # read existing data from json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(error)
    # match employee information
    if employee_fname in data:
        if data[employee_fname][0] == employee_lname:
            # add new employee data to the json file
            data[employee_fname][1] = int(input("Enter employee salary: "))
        else:
            print("last name didn't match")
    else:
        print("Employee not in file")
    # write updated data to json file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)
        print("Salary added successfully")


# to view salary table
def read_salary():
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
            print("List of all employees salaries: \n")
            # loop to get salaries
            for i in data:
                print(data[i][1])
    except FileNotFoundError as error:
        print(f"File Not Found{error}")


# to update salary
def update_salary():
    # read exciting json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")
    # take employee first and last name
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")
    # check if employee in the json file
    if employee_fname in data:
        if data[employee_fname][0] == employee_lname:
            print("User found in the list")
            # update the salary
            employee_salary_update = int(input("Enter updated employee salary: "))
            data[employee_fname][1] = employee_salary_update
            print("Employee Salary Updated")
        else:
            # notify: employee last name miss-match
            print("Employee last name didn't match")
    # notify: employee not in file
    else:
        print("Employee not found in the file")

    # write updated data to the file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)


# to delete salary
def delete_salary():
    # read exciting json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")
    # Take employee information
    employee_fnmae = input("Enter the employee first name: ")
    employee_lnmae = input("Enter the employee last name: ")

    if employee_fnmae in data:
        if employee_lnmae in data[employee_fnmae][0]:
            # print(f"Employee data: {target}")
            del data[employee_fnmae][1]
            print("Employee salary information has been deleted")
            with open("gui/employee_accounts.json", mode="w") as f:
                json.dump(data, f)
        else:
            print("Employee last name didn't match check it again")
    # notify: employee not in file
    else:
        print("Employee not found in the file")
