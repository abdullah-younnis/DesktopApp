import json


# function to add new employee
def create_employee():
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")
    employee_salary = 0

    # read existing data from json file
    try:
        with open("gui\employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # add new employee data to the json file
    data[employee_fname] = employee_lname, employee_salary

    # write updated data to json file
    with open("gui\employee_accounts.json", mode="w") as f:
        json.dump(data, f)
        print("Employee added successfully")


# to view employees first name in the file 
def read_employee():
    # read existing data from json file
    try:
        with open("gui\employee_accounts.json", mode="r") as f:
            data = json.load(f)
            print("List of all employees first name: \n")
            for i in data:
                print(i)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")


# to update employee name
def update_employee():
    target_update = ""
    # take target variable to be updated
    while target_update not in ("first name", "last name"):
        target_update = input("Enter target to update (first name/last name): ")
    # read exciting json file
    try:
        with open("gui\employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")
    # take employee first and last name
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")

    # check if employee in the json file
    if employee_fname in data:
        if employee_lname in data[employee_fname][0]:
            print("User found in the list")
            # match the target variable
            if target_update == "First_name":
                employee_fname_update = input("Enter updated employee first name: ")
                employee_fname = employee_fname_update
                print("Employee FirstName Updated")
            else:
                employee_lname_update = input("Enter updated employee last name: ")
                employee_lname = employee_lname_update
                print("Employee LastName Updated")
        # notify miss-match employee last name
        else:
            print("Employee last name didn't match check it again")
    # notify wrong employee first name 
    else:
        print("Employee not found in the file")

# update_employee function Task:
#                               Append the new employee updated variable to the json file


# to delete employee
def delete_employee():
    pass
