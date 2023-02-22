"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 12 : 
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J
"""
rows = int(input("Enter number of rows : ")) # Limited to 26
for i in range(1,rows+1):
    print((chr(64+i) + " ") * i)