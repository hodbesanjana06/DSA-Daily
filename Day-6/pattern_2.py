'''
Square Pattern Problem

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


'''
n = int(input("Enter Number"))

for i in range(n , 0 , -1):
    temp = i
    for j in range(1 , i+1):
        print(temp , end=" ")
        temp = temp -1

    print(end="\n")
