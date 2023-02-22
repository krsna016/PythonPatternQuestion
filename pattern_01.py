"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 1 : 
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
"""
size = int(input("Enter the size of the square pattern : ")) # Total columns
height = int(input("Enter the height of the square pattern : ")) # Total rows
for i in range(height):
    print("* "*size)
