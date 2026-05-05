'''

    1
    2 1
    1 2 1
    2 1 2 1
    1 2 1 2 1


'''

n = int(input("enter number"))

for i in range(1, n+1):
    temp=1
    t=2


    for j in range(1, i+1):
        if i % 2 == 0:
            if t == 2:
                print(t, end=" ")
                t=1
            else:
                print(t , end=" ")
                t=2
        else:
            if temp == 1:
                print(temp , end=" ")
                temp=2
            else:
                print(temp, end=" ")
                temp=1

    print(end="\n")