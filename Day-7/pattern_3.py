'''

                 1
               2 3
             3 4 5
           4 5 6 7
         5 6 7 8 9   

'''

n = int(input("enter number"))

for i in range(1 , n+1):
    for s in range(n-i):
        print(" ", end=" ")
    temp=i
    for j in range(1 , i+1):
        print(temp , end=" ")
        temp = temp + 1
    
    print(end="\n")