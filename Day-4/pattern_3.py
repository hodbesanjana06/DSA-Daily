'''
square number pattern 

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1


'''
temp=1
n = int(input("Enter Number : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if temp == 1:
            print(temp , end=" ")
            temp=0
        else:
            print(temp , end=" ")
            temp=1
    print(end="\n")
