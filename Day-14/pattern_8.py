'''



        1 2 3 4 5
          6 7 8
            9


'''

n = int(input("enter number"))
rem = n//2
mid = rem+1
temp=1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= mid :
            if j < i or j > n-i+1:
                print(" ", end=" ")
            else:
                # print(temp, end=" ")
                print(f"{temp:1}", end=" ")
                temp+=1
    print(end="\n")