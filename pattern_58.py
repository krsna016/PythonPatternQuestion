"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 58 : 
     E
    D E
   C D E
  B C D E
 A B C D E
  B C D E
   C D E
    D E
     E
"""
coloums = int(input("Enter the number of rows : "))
for i in range(1,coloums+1):
    print(" " * (coloums-i),end="")
    for j in range(coloums+1-i,coloums+1):
       print(" " + chr(64+j),end="")
    print()
for k in range(1,coloums):
    print(" " * k,end="")
    for l in range(k,coloums):
        print(" " + chr(65+l),end="")
    print()


        
    
