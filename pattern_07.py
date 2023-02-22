"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 7 : 
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A
"""
rows = int(input("Enter total number of rows : ")) # Limited to 26
columns = int(input("Enter total number of columns : "))
for i in range(rows,0,-1):
    for j in range(columns):
        print(chr(64 + i),end=" ")
    print()