#scenario 1 from loopsanditerationstasks
a=[1,5,6,7,4]
for num in a:
    print(num)
#How to print the nu,bers in a list in reverse way using loops
length=len(a)
print("printing the numbers in a reverse order using for loop")
for i in range(length-1,-1,-1):
    print(a[i])
print("enter a number to search in the list")
userinput=int(input())
print("  ")
for j in a:
    if(j==userinput):
        break;
        print("Found")
    print(j)
print("Break scenario is done")
#Continue
#scenario3
for k in a:
    if(k==userinput):
        print(k,"Found")
        continue
    print(k)
print("Continue scenario is done")
#Scenario5
#print numbers from 1 to 20
for m in range(1,10,2):
    print(m)
#scenario 6  print a multiplication table using for loop
print("Enter a number for multiplication table")
table=int(input())
for x in range(1,11):
    print(table,"*",x,"=",(table*x))
print("***********")
#scenario 7 print("Enter a multiplication table using while loop")
print("Using while loop")
p1=1
while (p1<=10):
    print(table,"*",p1,"=",(table*p1))
    p1=p1+1;
print("***********")
#infinite loop
o=1
