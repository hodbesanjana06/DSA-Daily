'''

* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * * 

'''

n = int(input("Enter Number : "))
rem = n // 2
mid = rem + 1

for i in range(1 , n+1):
    for j in range(1, n+1):
        if i % 2 != 0:
            print("*", end=" ")
        else:
            if j == 1 or j == n or j == mid:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print(end="\n")