'''


            1
            2 3
            3 4 5
            4 5 6 7
            5 6 7 8 9
        
'''
n = int(input("enter number : "))

for i in range(1, n+1):
    t=i
    for j in range(1 , i+1):
        print(t , end=" ")
        t+=1
    print(end="\n")