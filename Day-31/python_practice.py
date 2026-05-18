# slip 7______________________________________

'''

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

'''



'''

def count_letters(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

# Calling Function
count_letters("Hello World")

'''



# slip 7 _____________________________________________

'''

numbers = {10, 5, 25, 3, 18}

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

'''


'''

a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("NOT b:", ~b)

'''

# slip 8 _______________________________________

'''
d1 = {"a":1, "b":2}
d2 = {"c":10, "d":20}
print(d1 | d2 )
'''


'''
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total marks:", total)
print("Average:", average)

# Grade calculation
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")

'''


# slip 9 _______________________________________

'''
largest and smallest num from list 
max()
min()

'''

'''
text = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for i in text:
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


'''

# slip 10---------------------------------------

'''
def count_digits(num):
    
    return len(str(num))

# Example
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

'''


num = int(input("Enter a number: "))

temp = num
n = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")



# slip 11---------------------------------------

'''
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

'''


'''
i = 1

while i <= 50:
    print(i)
    i += 2
    
'''

# slip 12--------------------------------
'''
text = input("Enter a string: ")

lower = ""
upper = ""

for ch in text:
    if ch.islower():
        lower += ch
    else:
        upper += ch

result = lower + upper

print("Result:", result)

'''

'''
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")

# Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

'''


# slip 13 _______________________________

'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("First number:", a)
print("Second number:", b)
'''


'''
numbers = [1, 2, 3, 2, 4, 2, 5]
remove_item = 2

while remove_item in numbers:
    numbers.remove(remove_item)

print(numbers)

'''


# slip 14 _______________________________

'''
numbers = [10, 20, 30, 40, 50]

# swap first and last
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)



n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''


# slip 15 --------------------------------

'''

numbers = [10, 20, 30, 40, 50]

for item in numbers[::-1]:
    print(item, end=" ")
'''


'''
sentence = input("Enter a sentence: ")

# count words
words = sentence.split()
word_count = len(words)

# reverse sentence
reverse_sentence = sentence[::-1]

print("Number of words:", word_count)
print("Reversed sentence:", reverse_sentence)

'''

# 16--------------------------------

'''

year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
'''


'''

numbers = [1, 2, 3, 4, 5]

squared = []

for x in numbers:
    squared.append(x * x)



print(squared[::-1])
'''
# 17________________________________________

'''
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

'''

'''

t = (2, 4, 6, 1, 4, 7, 8, 2, 7)

print(tuple(sorted(t)))

'''

# 18_**********EASY______________________________

'''
max of 3 number

'''

'''
my_set = {1, 2, 3, 4, 5}

print(len(my_set))

'''


# 19___________________________________

'''
num = int(input("Enter a number: "))

if num == 2:
    print("Prime")
elif num % 2 == 0 or num == 1:
    print("Not Prime")
else:
    print("Prime")



t = ('P', 'y', 't', 'h', 'o', 'n')
print("".join(t)[::-1])

'''
# 20-----------------------------

'''text = input("Enter a string: ")

print(text[::-1])
'''

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 != 0:
        print(num, end=" ")
'''



# 21*****************EASY____________________________

'''
 max of 3 numbers

'''

'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2

print(result)

'''


# 22***********HALF EASY(20 marks)_____________________
'''
text = input("Enter a string: ")

result = text.swapcase()

print(result)

'''

'''
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

'''



# 23********half simple______________________


'''
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

'''


'''
t = (10, 20, 30, 40, 50, 60, 70, 80)

result = (t[3], t[5])

print(result)
'''


# 24************EASY_____________________

'''

numbers = [10, -5, 3, -2, 8, -1, 0, 7]

positive = []
negative = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)

'''


'''

text = input("Enter a string: ")
sub = input("Enter substring: ")

if sub in text:
    print("Substring is present")
else:
    print("Substring is not present")
'''


# 26************EASY__________________________

'''
numbers = [1, 2, 3, 4, 5]

print("Sum =", sum(numbers))


'''

'''
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is in range")
else:
    print("Number is not in range")

'''

# 27***********EASY________________________

'''

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

'''

'''
text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


'''


# 28**********EASY_________________

'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

'''


'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

'''


# 29___________________


num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



text = input("Enter a string: ")

print(text.swapcase())





