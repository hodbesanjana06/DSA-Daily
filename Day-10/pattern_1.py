'''

       
            0 0 0 0 1
            0 0 0 2 0
            0 0 3 0 0
            0 4 0 0 0
            5 0 0 0 0

'''

n = int(input("Enter Number"))

temp=1
for i in range(n, 0 , -1):
    for j in range(1 , n+1):
        if j == i:
            print(temp, end=" ")
            temp+=1
        else:
            print("0", end=" ")
    print(end="\n")


