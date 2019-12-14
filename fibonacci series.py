#intialize a[0],a[1] values first as 1,1

#printing the fibonacci series using lists
print("Enter a number")
num=int(input())
if num==1:
    a=[1]
    print(a)
elif num==2:
    a=[1.1]
    print("Fib series is",a)
else:
    a=[1,1]
    for i in range(2,num,1):
        a.append(a[i-1]+a[i-2])
print(a)
#print(a[0],a[1])
#for i in range(1,num,1):
    #a.insert((i+1),a[i+2])=a[i]+a[i-1]
    #print(a[i])
    #Printing fibonacci series with three variables
a=1
b=1
print(a)
print(b)
for i in range(1,5,1):
    c=int(a)+int(b)
    print(int(c))
    a=b
    b=c
