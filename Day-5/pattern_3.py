'''
Traiangle Pattern Problem

0
0 1
0 1 2 
0 1 2 3
0 1 2 3 4


'''
n = int(input("enter number "))
for i in range(1 , n+1):
    for j in range(0, i):
        if j == i:
            j=j+1
        else:
            print(j, end="")
    print(end="\n")
