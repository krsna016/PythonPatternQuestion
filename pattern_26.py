"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 26 : 
          1
         1 2
        1 2 3
       1 2 3 4
      1 2 3 4 5
     1 2 3 4 5 6
    1 2 3 4 5 6 7
   1 2 3 4 5 6 7 8
  1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9 10
"""
rows = int(input("Enter number of rows : "))
for i in range(1,rows+1):
    print((" " * (rows-i)),end="")
    for j in range(1,i+1):
        print(" " + str(j),end="")
    print()