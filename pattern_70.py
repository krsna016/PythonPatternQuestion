"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 70 : 
 * * * * *
  * * * *
   * * *
    * *
     *
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * i,end="")
    for j in range(rows+1-i,0,-1):
        print(" *",end="")
    print()
