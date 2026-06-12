'''

1 1 1 1 1 
2 1 1 1 2 
3 1 1 1 3 
4 1 1 1 4 
5 5 5 5 5 


'''

n = int(input("Enter Number : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n:
            print(i, end=" ")
        elif j == 1 or j == n:
            print(i , end=" ")
        else:
            print("1", end=" ")

    print(end="\n")

