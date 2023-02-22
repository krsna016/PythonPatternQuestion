"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 80 : 
     A
    B B
   C C C
  D D D D
 E E E E E
  D D D D
   C C C
    B B
     A
"""
columns = int(input("Enter number of columns : "))
for i in range(1,columns+1):
    print(" " * (columns - i) + (" " + chr(64+i)) * i)
for i in range(columns-1,0,-1):
    print(" " * (columns - i) + (" " + chr(64+i)) * i)