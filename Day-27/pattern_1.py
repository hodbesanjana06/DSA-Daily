'''

    * * *     
  *       *   
*           * 
*           * 
*           * 
  *       *   
    * * *     


'''


n = int(input("Enter Number : "))

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if (
            # top & last  secction  
            (i == 1 and j > 2 and j < n-1) or
            (i == 2 and (j == 2 or j == n-1)) or

            # i+1 and n - 1 curve points
            (i == n and j > 2 and j < n-1) or
            (i == n-1 and (j == 2 or j == n-1)) or

            # middle straite line
            (j == 1 and i > 2 and i < n-1) or
            (j == n and i > 2 and i < n-1)
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()