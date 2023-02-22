"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 73 : 
 E E E E E
  D D D D
   C C C
    B B 
     A
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows + 1):
    print(" " * (i-1) + (" " + chr(64 + rows-i+1))*(rows-i+1))