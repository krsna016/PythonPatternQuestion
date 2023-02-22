"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 35 : 
         1
       2 2 2
     3 3 3 3 3
   4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5 5
"""
rows = int(input("Enter the number of rows : "))
k = rows-1
for i in range(1,2*rows,2):
    print("  "*k + (" " + str(rows-k))*i)
    k -= 1