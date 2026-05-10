
'''


    *
    *
* *   * *
    *
    *




'''

n = int(input("Enter Number: "))

mid = n // 2 + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if (i == mid and j != mid) or (j == mid and i != mid):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()