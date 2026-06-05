'''


'''

n = int(input("Enter Number : "))
for i in range(1, n+1):
    t = 1

    for j in range(i,n+1):
        print(t, end=" ")
        t += 1
    

    for s in range((i-1)*2):
        print(" ", end=" ")

    for j in range(n - i + 1, 0, -1):
        print(j, end=" ")

    print()