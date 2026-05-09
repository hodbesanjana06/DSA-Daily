'''


1       0 
  1   0   
    1     
  1   0   
1       0 



'''

n = int(input("enter number : "))
rem = n // 2
mid = rem + 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if (j == i and j <= mid )or (j == n-i+1 and j <= mid):
            print("1", end=" ")
        elif (j == i and j > mid) or (j == n-i+1 and j > mid):
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")