"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 67 : 
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
"""
rows = int(input("Enter the total number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(" " + str(j),end="")
    print()
