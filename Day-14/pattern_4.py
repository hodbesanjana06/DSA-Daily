'''

        * * * * *
        *       *
        *   *   *
        *       *
        * * * * *


'''

n = int(input("enter odd number only : "))
rem = n//2
mid = rem+1
print(mid)

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == mid and i == mid or j ==1 or j == n or i == 1 or i == n :
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print(end="\n")