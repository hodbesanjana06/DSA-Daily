num = 12213
temp = num
reminder = 0
rev = 0

while num > 0:
    reminder = num % 10
    rev = rev * 10 + reminder
    num = num // 10

if rev == temp:
    print("Palindrom Number ", temp)
else:
    print("Not Palindrom ", rev)