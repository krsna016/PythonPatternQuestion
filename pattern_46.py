"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 46 : 
     5
    5 4
   5 4 3
  5 4 3 2
 5 4 3 2 1
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(" " + str(rows-j+1),end="")
    print()