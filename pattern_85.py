"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 85 : 
     1
    2 2
   3   3
  4     4
 5       5
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    print((" " + str(i)),end="")
    if i >= 2:
        print(" " * ((2*i)-4),end="")
        for k in range(i,i+1):
            print((" " + str(k)),end="")
    print()