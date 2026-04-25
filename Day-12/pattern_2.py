'''


        1 0 0 0 0
        2 1 0 0 0
        3 2 1 0 0
        4 3 2 1 0 
        5 4 3 2 1
        

'''

n = int(input("Enter number"))

for i in range(1 , n+1):
    temp=i
    for j in range(1 , n+1):
        
        if j<=i:
            print(temp , end=" ")
            temp=temp-1
        else:
            print("0", end=" ")
            
    print(end="\n")
