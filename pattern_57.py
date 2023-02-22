"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 57 : 
    3
   2 3
  1 2 3
 0 1 2 3
  1 2 3
   2 3
    3
"""
columns = int(input("Enter the number of rows : "))
for i in range(1,columns+1):
    print(" " * (columns-i),end="")
    for j in range(columns-i,columns):
        print(" " + str(j),end="")
    print()
for k in range(1,columns):
    print(" " * k,end="")
    for l in range(k,columns):
        print(" " + str(l),end="")
    print()