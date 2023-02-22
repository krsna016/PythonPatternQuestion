"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 92 : 
 E       E
  D     D
   C   C
    B B
     A
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
     print(" " * (i-1),end="")
     print(" " + chr(64+rows-i+1),end="")
     if i <= (rows - 1):
          print(" " * ((2*(rows-i))-2),end="")
          for k in range(i,i+1):
               print(" " + chr(64+rows-i+1),end="")
     print()