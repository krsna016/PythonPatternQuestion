"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 60 : 
4
4 3
4 3 2
4 3 2 1
4 3 2 1 0
4 3 2 1
4 3 2
4 3
4
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    for j in range(1,i+1):
        print(str(columns-j) + " ",end="")
    print()
for k in range(1,columns):
    for l in range(columns-1,k,-1):
        print(str(l) + " ",end="")
    print()
