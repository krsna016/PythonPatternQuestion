"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 6.1 : 
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1

Pattern 6.2 :
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8 8 8
7 7 7 7 7 7 7 7 7 7
6 6 6 6 6 6 6 6 6 6
5 5 5 5 5 5 5 5 5 5
4 4 4 4 4 4 4 4 4 4
3 3 3 3 3 3 3 3 3 3
2 2 2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1
"""
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
for i in range(rows):
    for j in range(columns,0,-1):
        print(j,end=" ")
    print()

print("\n\n")

rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))
for i in range(rows,0,-1):
    for j in range(columns):
        print(i,end=" ")
    print()