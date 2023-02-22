"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 45 : 
         A
       A B A
     A B C A B
   A B C D A B C
 A B C D E A B C D
"""
rows = int(input("enter the number of rows : "))
for i in range(1,rows+1):
    print("  " * (rows-i),end="")
    for j in range(0,i):
        print(" " + chr(65 + j),end="")
    for k in range(1,i):
        print(" " + chr(64 + k),end="")
    print()