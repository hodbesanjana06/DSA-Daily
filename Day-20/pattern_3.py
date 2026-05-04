'''
checkboard pattern

            *  *  *  *  *
              *  *  *  *
            *  *  *  *  *
              *  *  *  *
            *  *  *  *  *



'''


n = int(input("enter the nuber"))

for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(0, n-1):
                print(" *", end=" ")
    else:
            for j in range(1, n+1):
                print("* ",end=" ")

    print(end="\n")