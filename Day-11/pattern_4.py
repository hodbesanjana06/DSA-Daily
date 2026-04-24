'''
Multiplication table matrix.......................

        1  2  3  4  5
        2  4  6  8  10
        3  6  9  12 15
        4  8  12 16 20
        5  10 15 20 25




'''

n = int(input("enter number"))
temp=1


for i in range(1 , n+1):
    for j in range(1 , n+1):
        if i == 1:
            # print(temp , end=" ")
            print(f"{temp:3}", end=" ")
            temp+=1
        else:
            # print(i*j , end=" ")
            print(f"{i*j:3}", end=" ")
    print(end="\n")