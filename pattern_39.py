"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 39 : 
         1
       3 2 1
     5 4 3 2 1
   7 6 5 4 3 2 1
 9 8 7 6 5 4 3 2 1
"""
rows = int(input("Enter the number of rows : "))
k = rows - 1
for i in range(1,2*rows,2):
    print("  " * k,end="")
    k -= 1
    for j in range(i,0,-1):
        print(" " + str(j),end="")
    print()