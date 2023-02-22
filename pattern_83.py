"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 83 : 
		 5
	   5 4 5
	 5 4 3 4 5
   5 4 3 2 3 4 5
 5 4 3 2 1 2 3 4 5
   5 4 3 2 3 4 5
	 5 4 3 4 5
	   5 4 5
		 5
"""
rows = int(input("Enter the number of rows : "))
for i in range(1,rows+1):
	print("  " * (rows-i),end="")
	for j in range(1,i+1):
		print(" " + str(rows-j+1),end="")
	for k in range(2,i+1):
		print(" " + str(rows-i+k),end="")
	print()

for i in range(rows-1,0,-1): # i = 4,3,2,1
	print("  " * (rows-i),end="")
	for j in range(i,0,-1): # j = 4->0,3->0,2->1,1->0
		print(" " + str(rows-(i-j)),end="")
	for k in range(2,i+1): # k = 2->5,2->4,2->3
		print(" " + str(rows-(i-k)),end="")
	print()