"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 49 : 
 9 9 9 9 9 9 9 9 9
   7 7 7 7 7 7 7
     5 5 5 5 5
       3 3 3 
         1
"""
rows = int(input("Enter the number of rows : "))
k = 0
for i in range(2*rows-1,0,-2):
    print(("  " * k) + ((" " + str(i))*i))
    k += 1