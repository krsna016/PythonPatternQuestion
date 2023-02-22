"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 96 : 
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
1 0 1 0 1 0 1
"""
import pprint

list = []

rows = int(input("Number of rows : "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if ((i%2 != 0 and j%2 != 0) or (i%2 == 0 and j%2 ==0)):
            print("1 ",end="")
        else:
            print("0 ",end="")
    print()
            

    