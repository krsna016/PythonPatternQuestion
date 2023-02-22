"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 88 : 
     A
    B B
   C   C
  D     D
 E       E
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    print(" " + chr(64+i),end="")
    if(i>=2):
        print(" " * ((2*i)-4),end="")
        for k in range(i,i+1):
            print(" " + chr(64+k),end="")
    print()