''''


* * * * * * * 
*     |     * 
*     |     * 
* - - * - - * 
*     |     * 
*     |     * 
* * * * * * * 


'''


n = int(input("Enter Number : "))
rem = n // 2
mid = rem + 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == 1 or i == n or j == n or (i == mid and j == mid):
            print("*", end=" ")
        elif i ==  mid:
            print("-", end=" ")
        elif j == mid:
            print("|", end=" ")
        
        else:
            print(" ", end=" ")
    print(end="\n")