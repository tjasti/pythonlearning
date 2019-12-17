#Scenario1
def firstmethod():
    pass
print(firstmethod)
#print(id(firstmethod))
"""In order to create a blank method we use pass keyword, so that it will not throw any errors when you call the method"""
"""when you call method with out the parameters,it will give the memory location of that"""
#scenario3
#create a function with print or return inside it
def secondmethod():
    print("This is my second method")
secondmethod()
def secondmethod1():
    return "this is my second method2"
print(secondmethod1())
#scenario4:create a method with parameters
#description for scenario 4 is addition of two numbers
def add(number1,number2):
    sum=number1+number2
    print("Addition of two numbers is",sum)
print("Enter a number to perform the addition operation")
num1=int(input())
print("Enter another number to perform the addition number")
num2=int(input())
add(num1,num2)
#scenario 5:create a function with namespace
def strings(string1,string2="World"):
    print('{},{}'.format(string1,string2))
#Calling function
print("calling the string method")
strings("Hello")
#replacing the values in the string2
def strings1(string1,string2="World"):
    print('{},{}'.format(string1,string2))
#Calling function
print("calling the string method")
strings1("Hello","Good Morning")
#scenario 8:"""create a lep year program with methods to find out whether the given program is leap year or not"""
def leapyear(year):
    if((year%4==0) and ((year%100)!=0 or (year%400)==0)):
        print("it is a leap year")
    else:
        print("Not aleap year")


print("enter a year to finf whether the given year is a leap year or not")
leapyear1=int(input())
leapyear(leapyear1)
