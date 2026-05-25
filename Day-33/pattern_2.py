'''

1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 


'''


n = int(input("Enter Number : "))

for i in range(1 , n+1):
    for j in range(i , n+1):
        print(j, end=" ")

    print(end="\n")

for i in range(1, n):
    for j in range(n-i , n+1):
        print(j , end=" ")

    print(end="\n")