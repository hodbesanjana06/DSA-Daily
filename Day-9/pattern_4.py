'''
 


1 1 1 1 1 
1       1
1       1
1       1
1 1 1 1 1 


'''

n = int(input("Enter Number"))

for i in range(1 , n+1):
    for j in range(1, n+1):
        if j == 1 or j == n or i == 1 or i == n :
            print("1", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")