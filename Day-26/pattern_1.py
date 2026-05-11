'''
Cross X and + combined

*   *   *
  * * *
* * * * *
  * * *
*   *   *


'''

n = int(input("Enter Number : "))
rem = n // 2
mid = rem + 1


for i in range(1 , n+1):
    for j in range(1, n+1):
        if i == mid or j == mid or i == j or j == n-i+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print(end="\n")