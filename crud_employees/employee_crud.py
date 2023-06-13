import json

# Tasks:
        # adding more robust error handling for other types of errors that could occur,
        # such as invalid user input or file write errors.

# function to add new employee
def create_employee():
    # take employee information 
    employee_first_name = input("Enter employee first name: ")
    employee_last_name = input("Enter employee last name: ")
    employee_salary = 0
    # read existing data from json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    # add new employee data together
    data[employee_first_name] = employee_last_name, employee_salary
    # write the new employee data to json file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)
        print("Employee added successfully")


# function to view all employees first name in the file
def read_employee():
    # read existing data from json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
            print("List of all employees first name: \n")
            # loop on all first names
            for i in data:
                print(i)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")


# function to update exciting employee name
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
    employee_first_name = input("Enter employee first name: ")
    employee_last_name = input("Enter employee last name: ")
    # check if employee first and last name in the json file
    if employee_first_name in data:
        if data[employee_first_name][0] == employee_last_name:
            print("User found in the list")
            # match the target variable
            if target_update.lower() == "first name":
                employee_first_name_update = input("Enter updated employee first name: ")
                # update the employee first name
                data[employee_first_name_update] = data.pop(employee_first_name)
                print("Employee FirstName Updated")

            elif target_update.lower() == "last name":
                employee_last_name_update = input("Enter updated employee last name: ")
                # update the employee last name
                data[employee_first_name][0] = employee_last_name_update
                print("Employee LastName Updated")
        else:
            print("Employee last name didn't match")
    # notify: employee not in file
    else:
        print("Employee not found in the file")
        
    # write updated data to the file
    with open("gui/employee_accounts.json", mode="w") as f:
        json.dump(data, f)


# function to delete employee
def delete_employee():
    # read exciting json file
    try:
        with open("gui/employee_accounts.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        print(f"File Not Found{error}")
    # take employee information
    employee_first_name = input("Enter the employee first name: ")
    employee_last_name = input("Enter the employee last name: ")
    # find if the employee is in our data
    if employee_first_name in data:
        if employee_last_name in data[employee_first_name][0]:
            # delete our target key in the data
            del data[employee_first_name]
            print("Employee information has been deleted")
            with open("gui/employee_accounts.json", mode="w") as f:
                json.dump(data, f)
        else:
            print("Employee last name didn't match check it again")
    # notify: employee not in file
    else:
        print("Employee not found in the file")        
            
