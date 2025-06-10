#Lists
"""
A list is a collection of items in a defined order.
It can hold different data types — numbers, strings, even other lists.
Lists are mutable — you can change, add, or remove elements.

"""

#Lists Store References, Not Values
"""
The list a itself is a container with references (addresses) to the actual values.
Python internally creates separate objects for 10, 20, “GfG”, 40 and True, then stores their memory addresses inside a (list).
This means that modifying an element doesn’t affect other elements but can affect the referenced object.

"""

l1 = [12, "Abhi", 3.14, True]

print(l1)
print(l1[1])
print(type(l1[1]))
print(type(l1))
print(type(l1[2]))


#Creating a List

    #Using Square Brackets
a =[1,1.2,"Yo man"]
print(a)

    #Using list() Constructor
a = list((1,2,3,2.3,2.4,"Abhi"))
print(a)

    #Creating List with Repeated Elements
i = [2] * 5
j = [1] * 4

print(i)
print(j)

#Accessing List Elements
#Elements in a list can be accessed using indexing. 

a = [10,20,30,40,50]
print(a[0]) # first element
print(a[-1]) # last element


#Adding Elements into List
    #append(): Adds an element at the end of the list.
a2 = [5,10]
a2.append(15)
print(a2)

    #extend(): Adds multiple elements to the end of the list.
a2.extend([20,25,30])
print(a2)

    #insert(): Adds an element at a specific position.
a2.insert(0,0)
print(a2)


#Updating Elements into List
a1 = [10,20,30,50]
print(a1)
a1[3] = 40 # updating Element
print(a1)

#Removing Elements from List
j1 = [10,20,30,30,40,50,]

    #remove(): Removes the first occurrence of an element.
j1.remove(30)
print(j1)

    #pop(): Removes the element at a specific index or the last element if no index is specified.
j1.pop() # last will be deleted
j1.pop(3)
print(j1)

    #del statement: Deletes an element at a specified index.
del j1[2]
print(j1)

#Iterating Over Lists

aa = [1,"Abhi",2,"Aunty"]
for i in aa:
    print(i)

#Nested Lists in Python
# A nested list is a list within another list, which is useful for representing matrices or tables.
#  We can access nested elements by chaining indexes.

matrix = [
    [1,2,3],
    [2,4,6],
    [3,6,9]
]

print(matrix[2])
print(matrix[2][2])


