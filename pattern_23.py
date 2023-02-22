"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 23 : 
          *
         * *
        * * *
       * * * *
      * * * * *
     * * * * * *
    * * * * * * *
   * * * * * * * *
  * * * * * * * * *
 * * * * * * * * * *
"""
# This pattern is have (total_row-i) spaces for '*' in (i th) row: 
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(((" ") * (rows-i)) + ((" *") * (i)))