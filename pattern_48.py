"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 48 : 
 5 5 5 5 5 5 5 5 5
   4 4 4 4 4 4 4
     3 3 3 3 3
       2 2 2
         1
"""
rows = int(input("Enter the number of rows : "))
k = 0
for i in range(rows,0,-1):
    print("  "*(k) + (" " + str(i))*((i*2)-1))
    k += 1