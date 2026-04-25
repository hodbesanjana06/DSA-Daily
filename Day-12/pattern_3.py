
'''


        0 0 1 0 0
        0 0 2 0 0
        3 3 3 3 3
        0 0 4 0 0
        0 0 5 0 0


'''

n = int(input("enter number"))
rem = n//2
mid = rem+1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == mid or j == mid:
            print(i, end=" ")
        else:
            print("0", end=" ")
    print(end="\n")