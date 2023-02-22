"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 55 : 
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
    print(" " * (columns-i),end="")
    for j in range(1,i+1):
        print(" *",end="")
    print()
for k in range(1,columns):
    print(" " * k,end="")
    for l in range(1,columns+1-k):
        print(" *",end="") 
    print()
