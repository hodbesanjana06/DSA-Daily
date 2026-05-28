'''

1 * 2 * 3 
* 4 * 5 * 
6 * 7 * 8 
* 9 * 1 * 
2 * 3 * 4 

'''

n = int(input("Enter Number : "))
temp = 1
num = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if temp == 1:

            if num == 10:
                num = 1
                print(num, end=" ")
                num +=1
                temp =0
            else:
                print(num, end=" ")
                num += 1
                temp =0
        else:
            print("*", end=" ")
            temp = 1
    print(end="\n")
            