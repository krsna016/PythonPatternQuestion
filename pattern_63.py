"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 63 : 
E
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    for j in range(columns,columns-i,-1):
        print(chr(64+j),end=" ")
    print()
for k in range(1,columns):
    for l in range(columns,k,-1):
        print(chr(64+l),end=" ")
    print()

