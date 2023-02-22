"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 18 : 
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
"""
rows = int(input("Enter the rows : "))
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(chr(65+rows-j),end=" ")
    print()