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
a = input("write username ")
b = input("write password ")
if a ==("admin"):
    input(b)
else:
    print("access denied")
if b == ("12345"):
    print("access granted")
else:
    print("access denied")