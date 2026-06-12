'''

1 1 1 1 1 
1 2 2 2 1 
1 3 3 3 1 
1 4 4 4 1 
1 1 1 1 1 


'''

n = int(input("Enter Number : "))

for i in range(1 , n+1):
    for j in range(1 , n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("1", end=" ")

        else:
            print(i , end=" ")

    print(end="\n")