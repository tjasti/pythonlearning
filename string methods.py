#String methods
string="Hello World"
#String upper
#String lower
#String replace
#find index
#contains
#how to do slicing with the strings
"""Below method will convert the string to upper case"""
print(string.upper())
#String lower
print(string.lower())
"""The above method will convert all the characters to lowercase letters"""
"""Find method will find the index of the given string,if the given string is not found , it will return -1"""
print(string.find("Wo"))
print(string.count('o'))
"""count method will count the occurences of the characters"""
print(len(string))
print(string.replace("o", "_"))
"""replace method will replace the old characters with new ones"""
print(string)
print(string.replace("Hello","Hi"))
"""in step 22, it did not replace the content in the actual string that is string,because replace method
returns the value which has to be stored in some variable"""
print(string)
string=string.replace("Hello","Hi")
print(string)
#print(dir(string))
#print(help(str))
