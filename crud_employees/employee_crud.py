import json

# Tasks:
        # adding more robust error handling for other types of errors that could occur,
        # such as invalid user input or file write errors.

# function to add new employee
def create_employee():
    employee_fname = input("Enter employee first name: ")
    employee_lname = input("Enter employee last name: ")
    employee_salary = 0
    # read existing data from json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    # add new employee data to the json file
    data[employee_fname] = employee_lname, employee_salary
    # write updated data to json file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)
        print("Employee added successfully")


# to view all employees first name in the file
def read_employee():
    # read existing data from json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
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
            # match the target variable
            if target_update.lower() == "first name":
                employee_fname_update = input("Enter updated employee first name: ")
                data[employee_fname_update] = data.pop(employee_fname)
                print("Employee FirstName Updated")

            elif target_update.lower() == "last name":
                employee_lname_update = input("Enter updated employee last name: ")
                data[employee_fname][0] = employee_lname_update
                print("Employee LastName Updated")
        else:
            print("Employee last name didn't match")
    # notify: employee not in file
    else:
        print("Employee not found in the file")
        
    # write updated data to the file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)


# to delete employee
def delete_employee():
    # read exciting json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")

    employee_fnmae = input("Enter the employee first name: ")
    employee_lnmae = input("Enter the employee last name: ")
    
    if employee_fnmae in data:
        if employee_lnmae in data[employee_fnmae][0]:
            # print(f"Employee data: {target}")
            del data[employee_fnmae]
            print("Employee information has been deleted")
            with open("gui/employee_accounts.json", mode="w") as f:
                json.dump(data, f)
        else:
            print("Employee last name didn't match check it again")
    # notify: employee not in file
    else:
        print("Employee not found in the file")        
            
