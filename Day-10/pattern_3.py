'''

        1  2  3  4  5
        6  0  0  0  7
        8  0  0  0  9
       10  0  0  0  11
       12  13 14 15 13


'''


n = int(input("enter number"))
temp=1
o=0

for i in range(1, n+1):
    for j in range(1 , n+1):
        if j == 1 or j == n or i == 1 or i == n :
            print(f"{temp:3}", end=" ")
            temp+=1
        else:
            print(f"{o:3}", end=" ")
    print(end="\n")