'''

1 2 3 4 5 6 
  2       6 
    3     6 
      4   6 
        5 6 
          6 

'''

n = int(input("Enter Number : "))

for i in range(1, n+1):
    for j in range(1,n+1):
        if i == 1 or i == j or j == n:
            print(j , end=" ")
        else:
            print(" ", end=" ")

    print(end="\n")