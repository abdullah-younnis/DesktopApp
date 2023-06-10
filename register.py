# Tasks:

    # adding to it password verification not less than 8 char
    
    # adding to it execption handling for value errors

    # adding to it error statments



import json
import re

# Define a function named register that takes username and password as input 
def register():
    user_name = input() 
    password = input("Enter password: ") 
    account_type = ""
    # Choosing the account type mangerial or empolyee and save it
    while account_type not in ("manager", "employee"):
        account_type = input("Enter account type (manager/employee): ") 

    # read existing data from json file if it exists
    try:
        with open("credentials_file.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # add new user credentials to data
    data[user_name] = password, account_type

    # write updated data to json file
    with open("credentials_file.json", mode="w") as f:
        json.dump(data, f)

register()   