'''
Wave Number Pattern 

1   2   3   4   5   
  5   4   3   2   1 
1   2   3   4   5   
  5   4   3   2   1 
1   2   3   4   5   

'''
n = int(input("Enter Number : "))

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(1, 6):
            print(j, " ",end=" ")
    else:
        for j in range(5 , 0 , -1):
            print(" ",j,end=" ")

    print(end="\n")
            
