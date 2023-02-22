"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 47 : 
 * * * * * * * * *
   * * * * * * *
     * * * * *
       * * *
         *
"""
rows = int(input('Enter the number of rows : '))
k = 0
for i in range(1,2*rows,2):
    print("  " * k + (" *" * (2*rows-i)))
    k += 1
