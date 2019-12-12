#In this, we will be discussing about lists,tuples and sets
"""difference between Lists and Tuples"""
"""We can make modifications to the lists,where as tuples cannot be modified"""
"""sets cannot allow the duplicates of data"""
subjects=['Maths','science','social']
"""Mthods of a lis"""
#append
#remove
#pop method
#Index
subjects.append("English")
print(subjects)
#append method adds the item to the end
subjects.insert(4,"Science")
#insert method inserts the item at the particular location
print(subjects)
#pop method removes the last item from the list
subjects.pop()
print(subjects)
a=[7,2,3,5,8]
a.remove(2)
print("after removing the item",a)
"""Remove method will remove the item from the list"""
print(subjects)
subjectsreverselist=subjects.reverse()
print(subjects)
"""Reverse method doesn't directly returns the reversed list"""
subjects2=['Arts','Hindi']
subjects.extend(subjects2)
print(subjects)
print("Before sorting the values are",subjects)
subjectssorted=subjects.sort(reverse=False)
"""Sorting"""
print("After sorting the values are",subjects)
"""In python3 When i use the sort,reverse they are returning none"""
"""In order to avoid the above issue, I am storing the sorted values in to a variable and using the actual variable"""
subjects3=subjects.copy()
"""Copy"""
print(subjects3)
print(subjects)
"""Index will return the index of the mentioned item,if it is not present in the list,it will return an error"""
print(subjects.index('science'))
"""Count will return the number of times an item is present"""
print(subjects.count('science'))
"""*****************************Tuples**************************************************"""
a1=("English","Statistics","History")
"""Methods of a tuple:
Count
index"""
print("Index method of an item in tuple",a1.index("English"))
a1=("English")
print(a1)
#a2=a1.copy()
#print(a2)#Returns error,because it does not allow any modifications on the Tuples
#******************************Sets*****************************************
print("Sets")
a3={"English","hindi","science","History","English"}
print(a3)
"""Sets does not print the duplicates and everytime the order will change"""
a3.add("Geography")
print(a3)
a4={"Maths","Python"}
print(a3.update(a4))
print(a3)
a3.remove("Python")
print(a3)
a4.add("science")
print(a4)
print("Intersection")
"""Intersection will return the same elements from both the sets"""
print(a3.intersection(a4))
print(a3,a4)
print("Union")
print(a3.union(a4))
"""Union will return the unique items from both the lists"""
print(a4.difference(a3))
"""difference returns the items that are present in a4 and not present in 3"""
print(a3)
#How to create empty lists,sets and tuples
list1=list()
print(list1)
tuple1=tuple()
print(tuple1)
set1=set()
print(set1)
print("Another way of creating blank lists,tuples,sets")
list2=[]
print(list2)
tuple2=()
print(tuple2)
set2={}
"""We cannot use the above method because it considers as a dictionary"""
print(a)
g=sorted(a)
print(g)
"""sorted method is used to sort the items"""
#How to print the items of a list using loops
"""Loops***************************"""
print("Using for loops")
for i in a:
    print(i)
