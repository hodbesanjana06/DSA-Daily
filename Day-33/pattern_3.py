'''

*
**
***
****
*****
******
*****
****
***
**
*


'''

n = int(input("Enter Number : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")

    print(end="\n")


for i in range(2, n+1):
    for j in range(i, n+1):
        print("*", end="")

    print(end="\n")