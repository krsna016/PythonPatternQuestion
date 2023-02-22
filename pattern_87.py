"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 87 : 
     E
    D D
   C   C
  B     B
 A       A
"""
rows = int(input("Enter the rows : "))
for i in range(1,rows+1):
     print(" " * (rows-i),end="")
     print(" " + chr(64+rows-i+1),end="")
     if i >= 2:
          print(" " * ((2*i)-4),end="")
          for i in range(i,i+1):
               print(" " + chr(64 + rows - i + 1),end="")
     print()