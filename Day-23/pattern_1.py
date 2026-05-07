'''

                1 2 3 4 5
                  2   4
                    3
                  2   4
                1 2 3 4 5

'''

n = int(input("Enter Number : "))
t=n

for i in range(1, n+1):
    for j in range(1 , n+1):
        if i == 1 or i == n or j == i:
            print(j , end=" ")
        elif j == n-i+1:
            print(j , end=" ")
            
        else:
            print(" ", end=" ")

    print(end="\n")