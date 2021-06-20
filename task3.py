#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
# idonthave1 = True
# while idonthave1:
#     x = input("enter a number ")
#     x = int(x)
#     if x == 1:
#         idonthave1 = False


idonthaveeveninteger = True
while idonthaveeveninteger:
    x = input("write a number")
    x = float(x)
    y = int(x)
    if y == x and (x % 2) == 0:
        print("That is an even integer")
        idonthaveeveninteger = False
    else:
        print("That is not an even integer")