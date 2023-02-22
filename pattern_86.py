"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 86 : 
     5
    4 4
   3   3
  2     2
 1       1
"""
rows = int(input("Enter the rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    print(" " + str(rows-i+1),end="")
    if i >= 2:
        print(" " * ((2*i)-4),end="")
        for k in range(i,i+1):
            print(" " + str(rows-k+1),end="")
    print()