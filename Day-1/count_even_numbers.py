number = [2,5,4,7,8,13,12]
print(number)
count=0


for i in number:
    if i % 2 ==0:
        count=count+1

print("Count of Even Numbers :", count)