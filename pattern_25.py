"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 25 : 
          1
         2 2
        3 3 3
       4 4 4 4
      5 5 5 5 5
     6 6 6 6 6 6
    7 7 7 7 7 7 7
   8 8 8 8 8 8 8 8
  9 9 9 9 9 9 9 9 9
 10 10 10 10 10 10 10 10 10 10
"""
rows = int(input("Enter number of rows : "))
for i in range(rows):
    print(" " * (rows-i-1) + (str(i+1) + " ") * (i+1))