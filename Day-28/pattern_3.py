'''


*       *       *
*       *       *
* * * * * * * * *
*       *       *
*       *       *



'''

n = int(input("Enter Number : "))
r = n // 2
mid = r + 1



for i in range(1, n+1):
    for j in range(1, 2 * n):

        if j == 1 or j == n  or j ==(2 * n - 1) or i == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")



