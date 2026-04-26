'''

          *       *
            *   *
              *
              * 
              *

'''
n = int(input("Enter odd number: "))
rem = n//2
mid = rem+1


for i in range(1, n+1):
    for j in range(1 , n+1):
        if i <= mid:

            if j == i or j == n-i+1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j == mid:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    
    print("\n")