a=5
b=10
print(a+b)
#how to know the type of the variables
print(type(a))
c='10'
d='20'
print(c+d)
"""in order to convert the string in to integer, we use int method"""
print(int(c)+int(d))
f=-10.567
print(abs(f))
"""abs method converts the negative values to positive values"""
print(round(f,2))
print(dir(a))
#arithmatic opretions
#+ Addition
#-Substraction
#*Multiplication
#/ Division
#// Floor Division Which eliminates the  decimal
#** exponent
print("Addition is",(a+b))
print("substraction is",(a-b))
print("Division is", (a/b))
print("Multiplication is",(a*b))
print("Exponent value is",(a**b))
print(a%b)
print("Floor division is:",(a//b))
#Comparison operators
#<= less than
#>= greater than
#== equal to(not assignment operator)
#!=(Not equal to)
#< (Less than)
#> (Greater than)
print("Enter value1 to do comparison")
value1=input()
print("Enter value2 to do comparison")
value2=input()
print("Enter value3 to comparison")
value3=input()
if((value1>value2) and (value1>value3)):
    print("value1 is greater",value1)
elif((value2>value3) and (value2>value1)):
    print("value2 is greater",value2)
elif((value3>value1) and (value3>value1)):
    print("Value3 is greater",value3)
elif((a==b) or (b==a)):
    print("a and b are equal",b,a)
elif((b==c) or (c==b)):
    print("b and c are equal",b,c)
elif((c==a) or(c==b)):
    print("a &c are equal")
else:
    print("a,b and c are equal")
