'''

            1 
            1 1
            1   1
            1     1
            1 1 1 1 1 

'''


n = int(input("Enter number"))

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == i or j == 1 or i == n:

            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")