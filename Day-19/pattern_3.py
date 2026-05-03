'''


        1 2 3 4 5
        2 3 4 5 4
        3 4 5 4 3 
        4 5 4 3 2 
        5 4 3 2 1


'''
n = int(input("Enter the number : "))
for i in range(1, n+1):
    temp=i
    max=n
    for j in range(1, n+1):
        if temp > 5:
            max-=1
            print(max, end=" ")
        else:
            print(temp , end=" ")
            temp+=1
    print(end="\n")