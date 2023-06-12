# Tasks:

    # adding to it password verification not less than 8 char and contain numbers and @#$% special char
    
    # adding to it execption handling 

    # adding to it error descriptive statments

import json
import re

# define a function takes username, password and account_type as input 
def register():
    user_name = input("Enter Your User Name: ") 
    password = input("Enter Your Password: ") 
    account_type = ""
    # choosing the account type mangerial or empolyee and save it
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