"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 99 : 
 * *
 * *
 * * * *
 * * * * 
 * * * * * *
 * * * * * *
 * * * * * * * *
 * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
"""
rows = int(input("Enter the number of rows : "))
k = 2
str = ""
for i in range(1,rows+1):
    if(i != 1 and i % 2 != 0):
        k += 2
    for j in range(k):
        str += " *"
    print(str)
    str = ""
    
