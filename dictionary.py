a={}
print(type(a))
a={"studentname":"Sai","student id":101}
print(a)
a["studentname"]="Munna"
a["studentlocation"]="PTC"
print(a)
#a.get("student id")
a.update({"studentname":"Devi","student id":105})
print(a)
del a["studentname"]
print(a)
del a["student id"],a["studentlocation"]
print(a)
a1=a.update({"studentname":"Sai","student id":101,"studentlocation":"PTC"})
print(a)
print(len(a))
print(a.get("studentname"))
print("keys of the dictionary are")
print(a.keys())
print("Values of the dictionary are")
print(a.values())
print("if you want to print the values and keys then")
print(a.items())
"""What if you want to give the items that are not present"""
print(a.get("phonenumber","notfound"))
"""How to printthe keys using for loop"""
print("print the keys of the dictionary")
for key in a.keys():
    print(key)
print("print the values of the dictionary")
for val in a.values():
    print(val)
print("print the items of the list using loop")
for key,values in a.items():
    print(key,values)
print(a)
deletedvalue=a.pop("student id")
print("Deleted value is ",deletedvalue)
