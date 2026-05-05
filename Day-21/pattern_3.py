'''


        1
        2  4
        8  16  32 
        64 128 256 512



'''

n = int(input("enter number :"))
t=1

for i in range(1, n+1):
    for j in range(1, i+1):
            print(t, end=' ')
            t=t*2

    print(end="\n")