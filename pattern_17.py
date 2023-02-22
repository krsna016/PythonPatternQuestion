"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 17 : 
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
"""
rows = int(input("Enter the number of rows : "))
for i in range(rows,-1,-1):
    print((chr(65 + rows - i) + " ") * i)