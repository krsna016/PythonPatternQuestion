"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 64 : 
E
D E
C D E
B C D E
A B C D E
B C D E
C D E
D E
E
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    for j in range(columns+1-i,columns+1):
        print(chr(64+j),end=" ")
    print()
for k in range(1,columns):
    for l in range(k+1,columns+1):
        print(chr(64+l),end=" ")
    print()