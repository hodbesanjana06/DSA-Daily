'''

1 
2 3 
4 5 6 
6 5 4 
3 2 
1 

'''

n = int(input("Enter number : "))
t=1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(t, end=" ")
        t+=1

    print(end="\n")

t -=1
for i in range(1 , n+1):
    for j in range(i , n+1):
        print(t, end=" ")
        t-=1

    print(end="\n")
