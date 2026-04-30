''''

            * * * * *
                *
                *
                *
            * * * * *



'''
n = int(input("enter number only odd : "))

rem = n // 2
mid = rem + 1

for i in range(1 , n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")