'''

1 2 3 4 5 
1 * * * 5 
1 * 3 * 5 
1 * * * 5 
1 2 3 4 5 


'''

n = int(input("Enter Number : "))

rem = n // 2
mid = rem + 1 

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or (i == mid and j == mid) or j == 1 or j == n :
            print(j, end=" ")
    
        else:
            print("*", end=" ")

    print(end="\n")