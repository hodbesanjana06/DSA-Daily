'''


*     * * * * 
*     *       
*     *       
* * * * * * * 
      *     * 
      *     * 
* * * *     * 



'''


n = int(input("Enter Number : "))
rem = n // 2
mid = rem + 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == mid or j == mid or (i==1 and j > mid) or (i == n and j < mid) or (j == 1 and i < mid) or (j == n and i > mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print(end="\n")

