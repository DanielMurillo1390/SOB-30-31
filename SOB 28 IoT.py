# a is our main variable as it allow us to print the specific shape.
a="*" 
# n is the counter that will allow us to go from 0 to 5 and then form 5 to 0
n=0
# this FOR loop will print the first 5 rows
for i in range (6):
   
    print(a*n)
    n+=1
# this FOR loop will print the last 5 rows
for i in range(6):

    print(a*n)
    n-=1
