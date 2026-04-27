'''
square of number

          1    4    9   16
         25   36   49   64
         81  100  121  144 
         
        169  196  225  256

'''

print("------------------------")
n = int(input("enter number : "))
print("------------------------")
temp =1

for i in range(1 , n+1):
    for j in range(1 , n+1):
        # print(temp*temp , end=" ")
        print(f"{temp*temp:4}", end=" ")
        temp+=1
    print(end="\n")