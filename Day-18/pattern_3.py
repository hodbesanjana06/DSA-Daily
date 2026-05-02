'''
Spiral Pattern

            * * * * *
                    *
            * * *   *   
            *   *   *
            *   * * *    



'''

n = int(input("enter odd number only : "))

rem = n // 2
mid = rem + 1

for i in range(1 , n+1):
    for j in range(1 , n+1):
        if i == 1 or j == n or i == mid and j <= mid or j == 1 and i >= mid or j == mid and i >= mid or i == n and j>= mid :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")