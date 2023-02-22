"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 42 : 
         0
       1 0 1
     2 1 0 1 2
   3 2 1 0 1 2 3
 4 3 2 1 0 1 2 3 4
"""
rows = int(input("Enter the number of rows : ")) # 5
for i in range(1,rows+1):
    print("  " * (rows-i),end="") # Printing spaces
    for j in range(1,i):
        print(" " + str(i-j),end="") # Printing column 1,2,3,4
    for k in range(0,i):
        print(" " + str(k),end="") # Printing column 5,6,7,8,9
    print()