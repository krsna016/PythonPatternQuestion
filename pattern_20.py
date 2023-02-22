"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 20 : 
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10
"""
rows = int(input("Enter number of rows : "))
temp = 0
for i in range(rows,0,-1): # i = 10,9,8..1
    for j in range(i+temp,temp,-1): # j = 10->1,10->2,..10
        print(j,end = " ")
    temp += 1
    print()