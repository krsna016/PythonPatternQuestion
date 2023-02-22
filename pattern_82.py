"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 82 :  
         5
       4 5 4
     3 4 5 4 3
   2 3 4 5 4 3 2
 1 2 3 4 5 4 3 2 1
   2 3 4 5 4 3 2
     3 4 5 4 3
       4 5 4
         5
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1): # For, Upper portion
    print("  " * (rows-i),end="") # Upper spaces
    for j in range(1,i+1):
        print(" " + str(rows - i + j),end="") # Second quadrant
    for k in range(1,i):
        print(" " + str(rows - k),end="") # Firsts quadrant
    print()
        
for i in range(rows-1,0,-1): # For, Lower portion
    print("  " * (rows-i),end="") # Lower spaces
    for j in range(i,0,-1): 
        print(" " + str(rows - j + 1),end="") # Third quadrant
    for k in range(0,i-1): 
        print(" " + str(rows-k-1),end="") # Forth quadrant
    print()
        
  