'''

         1  6  11  16  21
         2  7  12  17  22
         3  8  13  18  23
         4  9  14  19  24
         5  10 15  20  25


'''

n = int(input("Enter number"))


for i in range(1, n+1):
    t=i
    for j in range(1, n+1):
        # print(t, end=" ")
        print(f"{t:3}", end=" ")
        t+=5
    print(end="\n")