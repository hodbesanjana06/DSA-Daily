'''
        1           1
          2        2 
            3     3
              4  4 
                5
               4  4 
             3      3
           2          2
         1              1






'''

n = int(input("Enter number: "))

for i in range(1, 2*n):
    if i <= n:
        val = i
    else:
        val = 2*n - i

    for j in range(1, 2*n):
        if j == i or j == 2*n - i:
            print(val, end=" ")
        else:
            print(" ", end=" ")
    print()