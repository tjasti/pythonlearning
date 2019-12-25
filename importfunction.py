import samplefunction1
import sys
print("Printing the system path")
print(sys.path)
sys.path.append('C:\\pythonprograms')
from additionmethod import addition
#print(sys.path)
num1=int(input("enter a num1 for addition"))
num2=int(input("enter num2 for addition"))
addition(num1,num2)
