'''
                1
              1 3
            1 3 5
          1 3 5 7
        1 3 5 7 9        

'''
n = int(input("Enter number"))

for i in range(1, n+1):

    for s in range(n-i):
        print(" ", end=" ")

    for j in range(1 , 2*i , 2):
        print(j , end=" ")

    print(end="\n")

