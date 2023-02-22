"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 72 : 
 5 4 3 2 1
  4 3 2 1
   3 2 1
    2 1
     1
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (i-1),end="")
    for j in range(rows-i+1,0,-1):
        print(" " + str(j),end="")
    print()
          