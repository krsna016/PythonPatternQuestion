"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 33 : 
 A B C D E
   A B C D
     A B C
       A B
         A
"""
rows = int(input("Enter number of rows : "))
for i in range(rows,0,-1):
    print("  "*(rows-i),end="")
    for j in range(0,i):
        print(" " + chr(65+j),end="")
    print()