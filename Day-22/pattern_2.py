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

n = int(input("enter number :"))
max=4
t=max

for i in range(1, n+1):

    for j in range(1, i):
        print(" ", end=" ")
    
    for j in range(i, n+1):
        print(j , end=" ")
    print(end="\n")


for i in range(n-1, 0 , -1):
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(i , n+1):
        print(j , end=" ")
        

    print(end="\n")
    