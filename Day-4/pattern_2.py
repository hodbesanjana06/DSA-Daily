'''
square number pattern 

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4 


'''
n=int(input("Enter the number : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end=" ")
    print(end="\n")