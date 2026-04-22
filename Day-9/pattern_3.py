'''

2
2 4
2 4 6 
2 4 6 8
2 4 6 8 10

'''

n = int(input("enter number"))
 

for i in range(1, n+1):
    
    t=2
    for j in range(1 , i+1):
        print(t , end=" ")
        t+=2
    print(end="\n")