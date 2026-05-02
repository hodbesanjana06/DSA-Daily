'''



            * * * * *
                *
            *   *
            *   *
            * * *

'''

n = int(input("enter number"))

rem = n // 2
mid = rem + 1
# print(mid)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == mid or i == n and j <= mid or j == 1 and i >= n-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")

