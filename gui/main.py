import tkinter 
# from crud_employees.employee_crud import read_employee, create_employee, delete_employee, update_employee
# from crud_salaries.salary_crud import * 
from tkinter.constants import *
# from app_auth.login import login

    # Example (Hello, World):
    

tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World!")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()