"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 78 : 
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
  2 3 4 5
   3 4 5
    4 5
     5
"""
columns = int(input("Enter the columns : "))
for i in range(1,columns+1):
    print(" " * (columns-i),end="")
    for j in range(0,i):
        print(" " + str(j+1),end="")
    print()
for i in range(columns-1,0,-1):
    print(" " * (columns-i),end="")
    for j in range(i,0,-1):
        print(" " + str(columns-j+1),end="")
    print()