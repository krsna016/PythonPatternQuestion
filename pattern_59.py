"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 59 : 
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    print("* " * i)
for k in range(columns-1,0,-1):
    print("* " * k)
