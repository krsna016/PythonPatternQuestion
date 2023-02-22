"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 44 : 
         1
       1 2 1
     1 2 3 2 1
   1 2 3 4 3 2 1
 1 2 3 4 5 4 3 2 1
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows + 1):
    print("  " * (rows-i),end="")
    for j in range(1,i):
        print(" " + str(j),end="")
    for k in range(i,0,-1):
        print(" " + str(k),end="")
    print()