"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 41 : 
         A
       C B A
     E D C B A
   G F E D C B A
 I H G F E D C B A
"""
rows = int(input("Enter the number of rows : "))
k = rows - 1
for i in range(1,2*rows,2):
    print("  " * k,end="")
    k -= 1
    for j in range(i,0,-1):
        print(" "  + chr(64 + j),end="")
    print()