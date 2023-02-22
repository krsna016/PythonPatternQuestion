"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 37 : 
         A
       C C C
     E E E E E
   G G G G G G G
 I I I I I I I I I
"""
rows = int(input("Enter the number of rows : "))
k = rows-1
for i in range(1,2*rows,2):
    print("  "*k + (" " + chr(64+i)) * i)
    k -= 1