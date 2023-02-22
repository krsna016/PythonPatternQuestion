"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 34 : 
         *
       * * *
     * * * * *
   * * * * * * *
 * * * * * * * * *
"""
rows = int(input("Enter the number of rows : "))
k = rows - 1
for i in range(1,2*rows,2):
    print("  " * k + " *" * i)
    k -= 1