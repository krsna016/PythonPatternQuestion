"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 5 : 
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
"""
coloum = int(input("Enter the total columns : ")) # Limited to 26
rows = int(input("Enter the total rows : "))
for i in range(rows):
    for j in range(1,coloum+1):
        print(chr(64+j),end=" ")
    print()
