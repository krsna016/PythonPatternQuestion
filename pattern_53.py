"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 53 : 
 A B C D E F G
   A B C D E
     A B C 
       A
"""
rows = int(input("Enter the number of rows : "))
k  = 0
for i in range(2 * rows - 1,0,-2):
    print("  " * k,end="")
    k += 1
    for j in range(1,i+1):
        print(" " + chr(64+j),end="")
    print()
