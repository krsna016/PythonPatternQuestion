"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 4 : 
A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J
"""
size = int(input("Enter the total columns : "))
# Limit of rows should be 26 as there's 26 alphabets.
height = int(input("Enter the total rows : ")) 
for i in range(height):
    print((chr(65+i) + " ")*size)


