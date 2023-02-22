"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 74 : 
 E D C B A
  D C B A
   C B A
    B A
     A
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (i-1),end="")
    for j in range(rows-i+1,0,-1):
        print(" " + chr(64 + j),end="")
    print()