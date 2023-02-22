"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 8 : 
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
"""
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : ")) # Limited  to 26
for i in range(rows):
    for j in range(columns,0,-1):
        print(chr(64 + j),end=" ")
    print()