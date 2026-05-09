'''

*             *
* *         * *
* * *     * * *
* * * * * * * *


'''


n = int(input("enter number : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")

    for s in range(1 , (n - i)* 2+1):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*", end=" ")
    print("\n")
