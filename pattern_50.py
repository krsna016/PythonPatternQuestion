"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 50 : 
 1 2 3 4 5 6 7
   1 2 3 4 5
     1 2 3
       1
"""
rows = int(input("Enter the number of rows : "))
k = 0
for i in range(rows*2-1,0,-2):
    print("  " * k,end="")
    for j in range(1,i+1):
        print(" "+str(j),end="")
    k += 1
    print()
    
    