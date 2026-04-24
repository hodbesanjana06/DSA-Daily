''''


        1 2 1 2 1
        2 1 2 1 2
        1 2 1 2 1
        2 1 2 1 2
        1 2 1 2 1


'''

n = int(input("Enter number"))
t=1

for i in range(1 , n+1):
    for j in range(1, n+1):
        if t == 1:
            print(t, end=" ")
            t=2
        else:
            print(t, end=" ")
            t=1
    print(end="\n")
