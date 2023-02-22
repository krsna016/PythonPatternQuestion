"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 98 :  
         *
        * *
       * * *
      * * * *
     * * * * *
    *         *
   * *       * *
  * * *     * * *
 * * * *   * * * *
* * * * * * * * * *
""" 
rows = int(input("Enter the number of rows : "))
for i in range(1,((rows//2)+1)):
    print(" " * ((rows)-i) + " *" * i)
for i in range(1,(rows//2)+1):
    print((" " * ((rows//2)-i)) + (" *" * (i)) + ("  " * ((rows//2)-i)) + (" *" * (i)))
