'''
* 
  * * 
    * * * 
      * * * * 
        * * * * * 

'''

n = int(input("Enter Number : "))

for i in range(1, n+1):

        for s in range(1, i):
            print(" ", end=" ")

        for j in range(1, i+1):
            print("*", end=" ")

        print(end="\n")