"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 9 : 
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
"""
rows_or_height = int(input("Enter the height for the pattern : "))
for i in range(1,rows_or_height + 1):
    print("* " * i)