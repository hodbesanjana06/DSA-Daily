'''

1   0   1 
  1 0 1   
0 0 1 0 0 
  1 0 1   
1   0   1 

'''

n = int(input("Enter Number : "))
rem = n // 2
mid = rem + 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or (j==n-i+1):
            print("1", end=" ")
        elif (i == mid) or (j == mid):
            print("0", end=" ")
        else:
            print(" ", end=" ")

    print(end="\n")