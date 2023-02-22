"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 27 : 
        A
       B B
      C C C
     D D D D
    E E E E E
   F F F F F F
  G G G G G G G
 H H H H H H H H
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    print((" " + chr(64+i)) * i)
