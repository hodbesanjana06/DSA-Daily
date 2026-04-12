number = [6,2,10,9,5]

max=number[0]
min=number[0]

for i in number:
    if max < i:
        max=i

for i in number:
    if min > i:
        min=i


print("Max is : ", max)
print("Min is : ", min)