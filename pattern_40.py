"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 40 : 
         A
       A B C
     A B C D E
   A B C D E F G
 A B C D E F G H I
"""
rows = int(input("Enter the total number of rows : "))
k = rows - 1
for i in range(1,2*rows,2):
    print("  " * k,end="")
    k -= 1
    for j in range(1,i+1):
        print(" " + chr(64 + j),end="")
    print()