'''
print column - wise

        1 5 9  13
        2 6 10 14
        3 7 11 15
        4 8 12 16

        
'''

n = int(input("enter number : "))


for i in range(1 , n+1):
    temp =i
    for j in range(1 , n+1):
        print(temp , end=" ")
        temp+=n
    print(end="\n")