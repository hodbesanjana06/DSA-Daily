'''


        * * * * *
        * 
        * * * * *
                *
        * * * * *       


'''

n = int(input("enter odd number only ")) 

rem = n // 2
mid = rem+1

for i in range(1 , n+1):
    for j in range(1, n+1):
        if (i == 1) or (i == n) or (i == mid) or ((j == 1) and (i < mid)) or ((j == n) and (i > mid) ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        
    print("\n")