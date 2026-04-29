'''


            1
            1 2
            1 2 3
            1 2
            1



'''
n = int(input("enter odd number only"))

rem = n//2 
mid = rem+1

for i in range(1, n+1):
    if i <= mid:
        for j in range(1, i+1):
            print(j , end=" ")
        print(end="\n")
    else:

        for j in range(1,n-i+2):
            print(j , end=" ")
        print(end="\n")

   