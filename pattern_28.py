"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 28 : 
          A
         A B
        A B C
       A B C D
      A B C D E
     A B C D E F
    A B C D E F G
   A B C D E F G H
  A B C D E F G H I
 A B C D E F G H I J
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    for j in range(1,i+1):
        print(" " + chr(64+j),end="")
    print()