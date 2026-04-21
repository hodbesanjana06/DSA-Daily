'''

                5
              4 5
            3 4 5
          2 3 4 5
        1 2 3 4 5     

'''
n = int(input("Enter Number "))

for i in range(n+1, 0, -1):
    for s in range(1, i):
        print(" ", end=" ")
    for j in range(i ,n+1):
        print(j , end=" ")
    
    print(end="\n")

