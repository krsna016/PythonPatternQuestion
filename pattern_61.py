"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 61 : 
4
3 4
2 3 4
1 2 3 4
0 1 2 3 4
1 2 3 4
2 3 4
3 4
4
"""
columns = int(input("Enter the number of columns : "))
for i in range(1,columns+1):
    for j in range(columns-i,columns):
        print(str(j) + " ",end="")
    print()
for k in range(1,columns):
    for l in range(k,columns):
        print(str(l) + " ",end="")
    print()