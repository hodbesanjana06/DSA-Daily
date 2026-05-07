'''


            2
            3 5
            7 11 13
            17 19 23 29


'''


n = int(input("enter number : "))

num = 2

for i in range(1, n+1):             
    for j in range(1, i+1):
        while True:
            c = 0
            for p in range(1 , num+1):
                if num % p == 0:
                    c += 1

            if c == 2:
                print(num , end=" ")
                num += 1
                break
            num +=1
    print(end="\n")