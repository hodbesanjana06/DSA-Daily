'''

0 0 1 0 0 
0 0 2 0 0 
0 0 3 0 0 
0 0 4 0 0 
0 0 5 0 0 

'''

n = int(input("Enter number : "))
r = n // 2
mid = r +1 
print(mid)
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == mid :
            print(i, end=" ")
        else:
            print("0", end=" ")

    print(end="\n")