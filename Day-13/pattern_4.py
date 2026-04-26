'''
only odd num enterd

        * * * * * * *
        *           *
        *           *
        * * * * * * *
        *
        *
        *


'''

n = int(input("enter number"))
rem= n // 2
mid = rem+1
# print(mid)

for i in range(1 , n+1):
    for j in range(1 , n+1):
        if i == 1 or j == 1 or i == mid or j == n and i < mid :
            print("*", end=" ")
    
        else:
            print(" ", end=" ")
    print(end="\n")