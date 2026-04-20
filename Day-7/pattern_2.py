'''

                1
              2 2
            3 3 3
          4 4 4 4
        5 5 5 5 5
'''
n = int(input("Enter Number"))

for i in range(1 , n+1):
    for s in range(n-i):
        print(" ", end=" ")
    for j in range(1 , i+1):
        print(i , end=" ")

    print(end="\n")