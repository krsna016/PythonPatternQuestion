"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 81 : 
     A
    A B
   A B C
  A B C D
 A B C D E
  B C D E
   C D E
    D E
     E
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    print(" " * (columns-i),end="")
    for j in range(1,i+1):
        print(" " + chr(64+j),end="")
    print()
for i in range(columns-1,0,-1):
    print(" " * (columns-i),end="")
    for j in range(i,0,-1):
        print(" " + chr(65+columns-j),end="")
    print()