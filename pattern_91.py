"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 91 : 
 5       5
  4     4
   3   3
    2 2
     1
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (i-1),end="")
    print(" " + str(rows+1-i),end="")
    if i <= (rows-1):
        print(" " * ((2*(rows-i))-2),end="")
        for i in range(i,i+1):
            print(" " + str(rows-i+1),end="")
    print()
            
            