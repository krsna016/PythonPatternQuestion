"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 38 : 
         1
       1 2 3
     1 2 3 4 5
   1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9
"""
rows = int(input("Enter the number of rows : "))
k = rows-1
for i in range(1,2*rows,2):
    print("  "*k,end="")
    k -= 1
    for j in range(1,i+1):
        print(" " + str(j),end="")
    print()
