#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
name = ""
password= ""

while True:
    name !="admin" and password !="12345"
    name=input("Enter username")
    password=input("Enter password")

    if name =="admin" and password =="12345":
        print("Access granted")
        break 
    else:
        print("Access denied") 
