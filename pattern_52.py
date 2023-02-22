"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 52 : 
 I I I I I I I I I
   G G G G G G G
     E E E E E
       C C C
         A
"""
rows = int(input("Enter the number of rows : "))
k = 0
for i in range(2*rows-1,0,-2):
    print("  " * k + (" " + chr(64+i)) * i)
    k += 1
