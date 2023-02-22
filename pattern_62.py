"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 62 : 
E
D D
C C C
B B B B
A A A A A
B B B B
C C C
D D
E
"""
columns = int(input("Enter the number of columns : "))
for i in range(columns,0,-1):
    print((chr(64+i)+" ") * (columns-i+1))
for j in range(1,columns):
    print((chr(65+j) + " ") * (columns-j))