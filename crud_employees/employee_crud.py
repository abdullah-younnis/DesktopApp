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
    data[employee_fname] = employee_lname,employee_salary

    # write updated data to json file
    with open("gui\employee_accounts.json", mode="w") as f:
        json.dump(data, f)
        print("Employee added successfully")


# to view employee table
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
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")

    try:
        with open("gui\employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")

    if employee_fname in data:
        if employee_lname in data:
            print("User found")
        else:
            print("User last name didn't match")
    else:
       print("Employee not found")

update_employee()

# to delete employee
def delete_employee():
    pass
