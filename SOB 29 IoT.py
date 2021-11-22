#2
#Modify your program from (1) to use the new list instead of ranges for printing.
#Test to see if you get a pyramid with an apex of 10 *’s.

L=["*","*","*","*","*","*","*","*","*","*"]
n=0
for i in (L):
   
    print(n*L[n-1])
    n+=1
for i in (L):

    print(n*L[n-1])
    n-=1

#Now, modify your program so in each new row (frame) has a single * that moves
#forward in position, leaving clear space behind it as illustrated below:
print("*********************************************************************************")  
b=" "
n=0

for i in (L):
   
    print(n*b + L[n])
    n+=1
for i in (L):

    print(n*b + L[n-1])
    n-=1
#3
#Repeat the process three times to create a long zig-zag pattern in the console. Your
#program might need adjusting to achieve this
print("*********************************************************************************")
b=" "
n=0
for i in range (0,3):
    for i in (L):
   
        print(n*b + L[n-1])
        n+=1
    for i in (L):

        print(n*b + L[n-1])
        n-=1
