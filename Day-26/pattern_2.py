'''


    1
    2
1 2 3 4 5
    4
    5




'''

n = int(input("Enter Number : "))

rem = n // 2
mid = rem + 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == mid  :
            print(j, end=" ")
        elif j == mid:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")