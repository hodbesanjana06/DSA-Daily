'''

            1 
            1 0
            1 0 1
            1 0 1 0
            1 0 1 0 1
            1 0 1 0 1 0

'''

n = int(input("enter number"))

for i in range(1, n+1):
    temp=1
    for j in range(1,i+1):
        if j == 1:
            print(temp , end=" ")
            temp=0
        else:
            if temp == 0:
                print(temp , end=" ")
                temp =1
            else:
                print(temp, end=" ")
                temp=0
            
    print(end="\n")