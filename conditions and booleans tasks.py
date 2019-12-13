
#memory locations of the variables
#finding out the number as even number or odd number
a=1;
print(id(a))
b=1;
print(id(b))
if(id(a)==id(b)):
    print("Both the variables are stored under same location")
else:
    print("Both the variables are not stored under same location")
"""When i use the variables with same values in the consecutive lines,then
 the same memory location will be assigned"""
"""python shell is showing the same memory locations for the above code"""
"""python idle is showing the different memory locations for the above code"""
print(a is b)
#write a program to find whether the given number is even or odd
print("enter a number to find whether given number is even or odd")
number=int(input())
if((number%2==0)):
    print("given number is a even number")
elif((number%2)!=0):
    print("given number is an odd number")
