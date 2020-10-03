##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""
name = ""
password= ""
count = 0 
while True:
    name !="admin" and password !="12345"
    name=(input("Enter username")).strip()
    password=input("Enter password")

    if name =="admin" and password =="12345":
        print("Access granted")
        break 
    else:
        print("Access denied") 
        count = count +1 
        if count ==3:
            break 
