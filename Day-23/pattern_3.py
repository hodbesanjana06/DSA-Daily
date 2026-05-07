'''


        1  2  3  4  5
        10 9  8  7  6
        11 12 13 14 15
        20 19 18 17 16




'''

n = int(input("enter number : "))




for i in range(1, n+1):
    o = (i-1) * n + 1
    e = i * n
   
    for j in range(1 , n+1):
        if i % 2 == 0:
            # print(e , end="  ")
            print(f"{e:3}", end=" ")
            e -= 1
        
        else:
            print(f"{o:3}", end=" ")
            o += 1
        
       

    print(end="\n")
    o +=6
