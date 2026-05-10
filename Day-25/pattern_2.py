'''
Arrow Pattern


    *
    * *
* * * * * *
    * *
    *


'''


n = int(input("Enter Number : "))
rem = n//2
mid = rem + 1
for i in range(1 , n+1):
    for j in range(1, n+1):
        if i == mid or j == mid or (i == mid-1 and j == mid+1) or (i == mid+1 and j == mid+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")