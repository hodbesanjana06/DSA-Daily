'''

l = int(input("Enter Length : "))
w = int(input("Enter Width : "))
print("Area of Rectangle : ", l * w, end="\n")

r= int(input("Enter Radius : "))
pi = 3.14

print("Area of Circle : ", pi * r * r)


'''


# _________________________________________________________

'''

s = input("Enter string : ")
new_str = ""
for i in s:
    if i not in "aeiouAEIOU" :
        new_str += i
    
print("remove Vowels :", new_str)


remove = ""
for i in new_str:
    if i not in remove:
        remove += i

print("Remove Duplicate : ", remove)

'''

# ___________________Slip 2__________________
'''
s = input("Enter String : ")
new_str =""
for i in s:
    if i.isalnum():
        new_str += i
    else:
        new_str += "#"

print("Modify String : ", new_str)

'''

'''n = int(input("Enter Number : "))

for i in range(1 , n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print(end="\n")
    '''


# ___________________SLIP 3__________________________
'''
t = (10 , 20, 30, 40)
print("Tuple Lenght : ",len(t))
'''


'''
n =  2
for i in range(1, 11):
    print(i*2, end="\n")
'''

# _______________________________
l = [10 , 20 , 30 , 40 ]
print("List : \n ", l)
t = tuple(l)
print("Convert into tuple \n ",t)


n  = int(input("Enter Number 1 : "))
n2  = int(input("Enter Number 2 : "))
n3  = int(input("Enter Number 3 : "))

max_num = max(n , n2 , n3)
min_num = min(n, n2, n3)

print("MAX : ")