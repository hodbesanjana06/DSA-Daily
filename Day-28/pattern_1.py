'''

Checker Cross Board

*  *  *  
 *  * 
*  *  *  
 *  * 
*  *  *  


'''

n = int(input("Enter Number : "))

for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(1, n+1-3):
            print(" *", end=" ")
    else:
        for j in range(1, n+1-2):
            print("* ", end=" ")
        
    print(end="\n")