# Tasks:

    # adding to it execption handling 

    # adding to it error descriptive statments

    # Search for any improvments i can add to the function


import json

# define function that takes username and password 
def login():
    user_name = input("Put Your User Name: ")
    password = input("Put Your Password: ")

# read the existing json file
    with open("credentials_file.json", mode="r") as f:
        data = json.load(f)
        
# verify credentials
    if user_name in data:
        if data[user_name] == password:
            print("Authentication successful!")
        # if Password incorrect
        else:
            print("Incorrect password.")
        # if username incorrect
    else:
        print("Username not found.")        

login()