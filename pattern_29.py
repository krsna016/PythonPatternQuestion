"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 29 : 
 * * * * *
   * * * *
     * * *
       * * 
         *
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print("  "* (i-1),end="")
    print(" *" * (rows + 1 - i))