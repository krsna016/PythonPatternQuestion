"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 51 : 
 E E E E E E E E E
   D D D D D D D
     C C C C C 
       B B B
         A
"""
rows = int(input("Enter the number of rows : "))
k = 0
for i in range(2*rows-1,0,-2):
    print("  " * k + (" " + chr(64+rows-k))*i)
    k += 1