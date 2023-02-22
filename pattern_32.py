"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 32 : 
 E E E E E
   D D D D
     C C C
       B B
         A
"""
rows = int(input("Enter number of rows : "))
for i in range(rows,0,-1):
    print("  "*(rows-i) + (" " + chr(64+i)) * i)
    