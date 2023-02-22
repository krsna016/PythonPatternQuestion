"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 43 : 
         A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print("  " * (rows-i),end="")
    for j in range(1,i):
        print(" " + chr(65+(i-j)),end="")
    for k in range(0,i):
        print(" " + chr(65+k),end="")
    print()
