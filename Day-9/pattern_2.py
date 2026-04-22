'''

25  24  23  22  21 
20  19  18  17  16
15  14  13  12  11
10  9   8   7   6
5   4   3   2   1

'''

n = int(input("enter number"))

t=n * n

for i in range(1 , n+1):
    for j in range(1, n+1):
        print(f"{t:3}", end=" ")
        t=t-1
    
    print(end="\n")