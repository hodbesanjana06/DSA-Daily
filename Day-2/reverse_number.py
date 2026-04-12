num = 1234
print("original Num : ", num)

reminder=0
rev=0

while num > 0:
    reminder = num % 10
    rev = rev * 10 + reminder
    num = num // 10
print("Recerse Num : ", rev)  