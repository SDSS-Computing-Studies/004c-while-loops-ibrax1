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
Access denied
"""
a = input("write username ")
b = input("write password ")
count = 0
while count>3:
    if a ==("admin"):
        input(b)
    else:
        print(a)
    if b == ("12345"):
        print("access granted")
    else:
        print(b)
    count= count+1