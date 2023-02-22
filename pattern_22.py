"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 22 : 
J I H G F E D C B A
J I H G F E D C B
J I H G F E D C
J I H G F E D
J I H G F E
J I H G F
J I H G
J I H
J I
J
"""
rows = int(input("Enter number of rows : "))
for i in range(rows): # i = 0->9
    for j in range(rows-i): # j = 0->9,0->8,0->7,..0  
        print(chr(64+rows-j),end=" ")
    print()