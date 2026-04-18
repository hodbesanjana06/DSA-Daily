'''
Square Pattern Problem

5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1


'''
n = int(input("Enter Number ")) 
for i in range(1 , n+1):
    for j in range(5 , 0, -1):
        print(j , end=" ")
    
    print(end="\n")

    
