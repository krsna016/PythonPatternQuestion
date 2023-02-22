"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 77 :
	 1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
	 1
"""
columns = int(input("Enter the columns : "))
for i in range(1,columns+1):
    print(" " * (columns-i) + (" " + str(i)) * i)
for i in range(columns-1,0,-1):
    print(" " * (columns-i) + (" " + str(i)) * i)
