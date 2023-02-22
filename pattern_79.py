"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 79 :
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
  1 2 3 4
   1 2 3
    1 2
     1
"""
columns = int(input("Enter the number of columns : "))
for i in range(1, columns+1):
    print(" " * (columns-i), end="")
    for j in range(1, i+1):
        print(" " + str(j), end="")
    print()
for i in range(columns-1,0,-1):
    print(" " * (columns-i), end="")
    for j in range(i,0,-1):
        print(" " + str(i - j + 1 ), end="")
    print()