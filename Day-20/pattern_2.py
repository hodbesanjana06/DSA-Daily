'''


        1 2 3 4 5
        2   3   2
        3 3 3 3 3 
        4   3   4
        5 4 3 2 1


'''


n = int(input("enter the nuber "))
max = n

rem = n // 2
mid = rem + 1


for i in range(1, n+1):
    temp = 1

    for j in range(1, n+1):
        if i == 1:
            print(temp, end=" ")
            temp+=1
        elif i == n:
            print(max, end=" ")
            max= max -1
        elif j == 1 or j == n:
            print(i ,end=" ")
        elif i == mid or j == mid:
            print(mid , end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")