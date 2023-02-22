"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 76 : 
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    print(" " * (columns-i) + " *" * i)
for i in range(columns-1,0,-1):
	print(" " * (columns-i) + " *" * i)