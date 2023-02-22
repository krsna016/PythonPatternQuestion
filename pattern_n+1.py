"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 2:
            1
            22
            333
            4444
            55555
"""
size = int(input("Enter the size : "))
for i in range(1,size+1):
    print(((10**i)//9)*i)