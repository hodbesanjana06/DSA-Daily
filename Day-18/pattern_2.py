'''


            *      *     
            * *    *    
            *  *   *  
            *    * *
            *      *


'''

n = int(input("enter number noly odd : "))

rem = n // 2
mid = rem + 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")