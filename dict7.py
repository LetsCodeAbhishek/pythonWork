#Dictionary

"""
A dictionary is an unordered collection of key-value pairs.
Defined using curly braces {}
Keys are unique, and each key maps to a value.

Values in a dictionary can be of any data type and can be duplicated, 
whereas keys can’t be repeated and must be immutable.
"""

d = {1:"Aunty", 2:"Abhi", 3:"Sunny"}
print(d)
print(type(d))

#Create a Dictionary
#In Python, a dictionary can be created by placing a sequence of elements 
# within curly {} braces, separated by a ‘comma’.

# create dictionary using { }
d = {1:"Abhi", 2:"Sun",3:"Yo"}
print(d)

# create dictionary using dict() constructor
d2 = dict(a ="abhi", b="sun", c="Ravi")
print(d2) 

#Accessing Dictionary Items
d = {1:"Abhi", "name":"Sun","y":"Yo"}

# Access using key
print(d["y"])
print(d[1])

# Access using get()
print(d.get("name"))
print(d.get(1))

#Adding and Updating Dictionary Items

    # Adding a new key-value pair
d["age"] = 22
d[13] = 23
d[14] = 23
d[15] = 23
print(d)

    # Updating an existing value
d["y"] = "Python"
d[1] = "Abhishek"
print(d)

#Removing Dictionary Items
"""
del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair.

"""    
    # Using del to remove an item
del d[13]
del d["y"]
print(d)

    ## Using pop() to remove an item and return the value
d.pop("name")
print(d)

    # Using popitem to removes and returns
    # the last key-value pair.
d.popitem()
d.popitem() # delete last key
print(d)


    ## Clear all items from the dictionary
d.clear()
print(d)


#Iterating Through a Dictionary
# We can iterate over keys [using keys() method] , values [using values() method] 
# or both [using item() method] with a for loop.


d = {1:"Abhi", 2:"Sunny", 3:"Ravi"}

    # Iterate over keys
for key in d:
    print(key)

    # Iterate over values
for value in d.values():
    print(value)

    # Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

for key, value in d.items():
    print(f"{value}: {key}")

#Nested Dictionaries

d = {1:"Abhi", "A":"Sunny", 2:{11:"A", 12:"BB", "D":"welcome"}}
print(d)
print(d[2])
print(d[2][12])
