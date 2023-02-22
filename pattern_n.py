"""
Name                : Anurag Pareek
University Roll no. : 2215000322
Contact             : anurag020416@gmail.com

Pattern 1:
            1
            121
            12321
            1234321
            123454321
"""
size = int(input("Enter the size : "))
for i in range(1,size+1):
    print(((10**i)//9)**2)