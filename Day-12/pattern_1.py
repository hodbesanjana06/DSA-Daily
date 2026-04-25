'''

       1 1 1 1 1
       2 0 0 0 2
       3 0 0 0 3
       4 0 0 0 4
       5 5 5 5 5


'''

n = int(input("Enter Number"))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1:
            print("1", end=" ")
        elif i == n:
            print(n ,end=" ")
        elif j == 1 or j == n :
            print(i , end=" ")
        else:
            print("0" , end=" ")
    print(end="\n")

