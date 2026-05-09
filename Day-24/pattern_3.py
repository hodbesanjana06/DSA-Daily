'''


1             1 
1 2         1 2 
1 2 3     1 2 3 
1 2 3 4 1 2 3 4 


'''

n = int(input("Enter nunber : "))

for i in range(1 , n+1):
    for j in range(1, i+1):
        print(j, end=" ")

    for s in range(1, (n-i)* 2+1):
        print(" ", end=" ")

    for j in range(1, i+1):
        print(j, end=" ")

    print(end="\n")


