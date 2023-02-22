"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 84 : 
     *
    * *
   *   *
  *     *
 *       *
"""
rows = int(input("Enter the total rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i),end="")
    print(" *",end="")
    if i>=2:
       print(" " * ((i*2)-4),end="")
       for j in range(i,i+1):
           print(" *",end="")
    print()
       
    