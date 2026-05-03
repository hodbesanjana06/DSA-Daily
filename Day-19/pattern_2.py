'''


        1 0 0 0 1
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        1 0 0 0 1


'''

n = int(input("enter number"))

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == 1 and j ==1) or (i == 1 and j == n) or (i == n and j == n) or (i == n and j == 1) :
            print("1", end=" ")
        else:
            print("0", end=" ")

    print(end="\n") 