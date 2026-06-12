'''

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 

'''
n = int(input("Enter Number : "))

odd = 1
even = 2

for i in range(1, n+1):

    if i % 2 != 0:
        value = odd
        odd += 2
    else:
        value = even
        even += 2

    for j in range(1, n+1):
        print(value, end=" ")

    print()