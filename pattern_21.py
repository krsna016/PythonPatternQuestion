"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 21 : 
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A
"""
rows = int(input('Enter number of rows : '))
for i in range(rows):
    print((chr(64+rows-i)+" ") * (rows-i))
