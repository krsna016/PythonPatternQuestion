"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 36 : 
         A
       B B B
     C C C C C
   D D D D D D D
 E E E E E E E E E
"""
rows = int(input("Enter the number of rows : "))
k = rows-1
for i in range(1,2*rows,2):
    print("  "*k + (" " + chr(64+rows-k))*i)
    k -= 1