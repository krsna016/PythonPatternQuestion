"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 65 : 
     *
    * *
   * * *
  * * * *
 * * * * *
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
    print(" " * (rows-i) + " *" * i)