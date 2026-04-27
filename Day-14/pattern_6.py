'''


        * * * * *
        *       *
        *   *   *
        *     * *
        *       *


'''


n = int(input("enter odd number only : "))
rem = n//2
mid = rem+1


for i in range(1, n+1):
    for j in range(1 , n+1):
        if (i == 1) or (j == 1) or (j == n) or (j==mid and i==mid) or (j == i and j>=mid+1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")

