"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 24 : 
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
rows = int(input("Enter number of rows : "))
for i in range(1,rows + 1): # For spaces
    print(" " * (rows-i),end="")
    for j in range(i): # For stars
        print(" *",end="")
    print()