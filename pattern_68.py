"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 68 : 
     A
    B B
   C C C
  D D D D
 E E E E E
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i) + (" " + chr(64+i)) * i)
