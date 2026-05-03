'''

1 2 3 4 5
2       2
3       3
4       4
5 4 3 2 1



'''
n = int(input("enter the nuber "))
for i in range(1, n+1):
    temp = 1

    for j in range(1, n+1):
        if i == 1 or  i == n :
            print(temp, end=" ")
            temp+=1
        elif i == n:
            print(temp, end=" ")
            temp+=1
        elif j == 1 or j == n:
            print(i ,end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")